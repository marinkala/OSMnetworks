import networkx as nx
import os.path
from TimeNetworksAnalytics import getJsonNet
from composeBigNetNodeEdgePers import getFolders
from findTimeSlice import byEdge
import pickle

def temporal(in_folder, big_folder, persThresh, consistThresh):
	#find mappers with persistence higher than 1
	#use that list to go through each time slice
	#if more than 50% of the time slices where for the same part of the day - output the mapper and time slices
	B=nx.read_yaml(big_folder)
	users=B.nodes(data=True)
	pers_users=[u[0] for u in users if u[1]['persistence']>persThresh] 
	for u in pers_users:
		night=0
		day=0
		evenining=0
		persistence=0
		for file in os.listdir(in_folder):
			if file!='.DS_Store': #weird MAC thing
				path=in_folder+file
				G=getJsonNet(path)
				G=nx.DiGraph(G)
				if G.has_node(u):
					persistence+=1
					period=str(file)[11:13]
					if period=='03':
						night+=1
					elif period=='11':
						day+=1
					else:
						evenining+=1
		if night/float(persistence)>consistThresh:
			print u, 'night', night/float(persistence)
		elif day/float(persistence)>consistThresh:
			print u, 'day', day/float(persistence)
		elif evenining/float(persistence)>consistThresh:
			print u, 'evenining', evenining/float(persistence)

def spatial_major(in_folder, cliqueThresh):
	for file in os.listdir(in_folder):
		if file!='.DS_Store': #weird MAC thing
			path=in_folder+file
			G=getJsonNet(path)
			G=nx.Graph(G) #can't do cliques on directed nets
			if G.order()>0:
				n=nx.graph_clique_number(G)
				if n>cliqueThresh:
					print file
					for c in nx.k_clique_communities(G,n):
						print list(c)

def expand_out(in_folder, diamThresh): 
#filling in the puzzle by overlapping with someone else for changeset_overlap
#building out the road network for intersecting_roads
	for file in os.listdir(in_folder):
		if file!='.DS_Store': #weird MAC thing
			path=in_folder+file
			G=getJsonNet(path)
			G=nx.Graph(G) #need long chains - not directed
			if G.order()>0:
				giant=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
				diam=nx.diameter(giant)
				if diam> diamThresh:
					print file
					paths=nx.shortest_path(G)
					for x in paths.values():
						for i in xrange(len(x.values())):
							if len(x.values()[i])==diam+1: #diameter pat
								print x.values()[i]

def expand_out2(in_folder, compThresh): #directed
#filling in the puzzle by overlapping with someone else for changeset_overlap
#building out the road network for intersecting_roads
	for file in os.listdir(in_folder):
		if file!='.DS_Store': #weird MAC thing
			path=in_folder+file
			G=getJsonNet(path)
			G=nx.DiGraph(G) #need long chains - not directed
			if G.order()>0:
				giant=sorted(nx.strongly_connected_components(G), key = len, reverse=True)[0]
				if len(giant)/float(len(G))>compThresh:
					print file
					print "giant: ", giant
					print "not in giant: ", list(set(G.nodes())-set(giant))

def expand_out3(in_folder, compThresh): #undirected
#filling in the puzzle by overlapping with someone else for changeset_overlap
#building out the road network for intersecting_roads
	for file in os.listdir(in_folder):
		if file!='.DS_Store': #weird MAC thing
			path=in_folder+file
			G=getJsonNet(path)
			G=nx.Graph(G) #need long chains - not directed
			if G.order()>0:
				giant=sorted(nx.connected_components(G), key = len, reverse=True)[0]
				if len(giant)/float(len(G))>compThresh:
					print file
					print "giant: ", giant
					print "not in giant: ", list(set(G.nodes())-set(giant))

def reciprocity(big_folder, weightThresh):
	B=nx.read_yaml(big_folder)
	reciprocity=[]
	edges=[]
	for e in B.edges_iter():
	    if B.has_edge(e[1],e[0]):
	        if B[e[0]][e[1]]['weight']>weightThresh: # get the constant from a distribution?
	            if B[e[0]][e[1]]['weight']<=B[e[1]][e[0]]['weight']:
	                reciprocity.append(B[e[0]][e[1]]['weight']/float(B[e[1]][e[0]]['weight']))
	                edges.append((e[0],e[1]))
	return zip(edges, reciprocity)

def sideBySide(in_folder, big_folder, weightThresh):
	recEd=reciprocity(big_folder, weightThresh)
	#get edges where mapper1 responded to at least 50% of mapper2 edges
	edgeList=[x for x,y in recEd if y>0.5] 
	for e in edgeList:
		byEdge(e, in_folder)

def supervision(in_folder, big_folder, weightThresh):
	recEd=reciprocity(big_folder, weightThresh)
	#get edges where mapper1 responded to less than 50% of mapper2's edges
	edgeList=[x for x,y in recEd if y<0.33] 
	for e in edgeList:
		byEdge(e, in_folder)

def supervisor(big_folder):
	with open('/Users/Ish/Dropbox/OSM/results/Haiti/new_users', 'rb') as f:
		newList = pickle.load(f)
	B=nx.read_yaml(big_folder)
	initList=[]
	for e in B.edges_iter():
		if (e[1] in newList) & (e[0] not in newList):
			initList.append(e[0]) #save the experienced user who's edited after a new user
			print e
	initList=list(set(initList)) #get rid of the duplicates
	highNewProp=[]
	for m in initList: #for each mapper in the initial list
		succ=B.successors(m)
		new_succ=0
		new_succList=[]
		for s in succ:
			if s in newList:
				new_succ+=1
				new_succList.append(s)
		new_prop=new_succ/float(len(succ))
		if new_prop>0.5:
			highNewProp.append(m)
			highNewProp.append(new_succList)
	print highNewProp

def supervised(big_folder, weightThresh):
	with open('/Users/Ish/Dropbox/OSM/results/Haiti/new_users', 'rb') as f:
		newList = pickle.load(f)
	B=nx.read_yaml(big_folder)
	initList=[]
	for e in B.edges_iter():
		if (e[1] in newList) & (e[0] not in newList):
			if B[e[0]][e[1]]['weight']>weightThresh:
				if ~B.has_edge(e[1],e[0]): #new user doesn't respond back
					print e

in_folder, big_folder=getFolders(8,'h','changeset')
#temporal(in_folder, big_folder, 3, 0.75)
spatial_major(in_folder, 5)
#expand_out2(in_folder, 0.5) 
#sideBySide(in_folder, big_folder, 10)
#supervision(in_folder, big_folder, 3)
#supervisor(big_folder)
#supervised(big_folder, 4)