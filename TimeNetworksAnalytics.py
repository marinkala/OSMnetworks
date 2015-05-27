import networkx as nx
import numpy as np
import pandas as pd
import os.path
import cent_measures
from networkx.readwrite import json_graph
import json
import config_model


def getFolder(bucket):
	'''folder='/Users/Ish/Documents/OSM_Files/philippines/networks14days/\
overlapping_changesets_by_'+bucket+'_hour/' '''
	folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/\
intersecting_roads_by_'+bucket+'_hour/'
	return folder

def getJsonNet(path):
	data=open(path).read()
	parsed=json.loads(data)
	G=json_graph.node_link_graph(parsed, directed=True)
	return G

def getExpFolder(bucket):
	folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/overlapping_changesets/\
ExpAnnotNets/overlapping_changesets_by_'+bucket+'_hour/'
	return folder

def networkSize(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	n=[]
	name=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			name.append(file)
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			n.append(len(G))
	#np.array(n).tofile('networkSize.txt',sep=',')
	return name, n

def avgQuant(quant, bucket):
	if quant=='degree':
		quantString='Degs'
	if quant=='strength':
		quantString='Strength'
	bucket=str(bucket)
	folder='/Users/Ish/Dropbox/OSM/results/Philippines/TwoWeeks/intersecting_roads/'
	y=np.fromfile(folder+'AvgNet'+quantString+'/intersecting_roads_by_'+bucket\
	+'_hour_avg'+quantString+'.txt',sep=',')
	return y
	
def diameter(bucket): #diameter of largest componenent
	bucket=str(bucket)	
	folder=getFolder(bucket)
	d=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0:
				d.append(nx.diameter(comps[0]))
			else:
				d.append(0)
	#np.array(d).tofile('largestCompDiameter.txt',sep=',')
	return d
	
def absCompSize(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0:
				s.append(len(comps[0]))
			else:
				s.append(0)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def relCompSize(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0: #should it be not just non-empty? but with edges?
				s.append(len(comps[0])/float(len(G)))
			else:
				s.append(0)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def numComps(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0:
				s.append(len(comps))
			else:
				s.append(0)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s
	
def singletons(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				s.append(len(nx.isolates(G))/float(len(G)))
			else:
				s.append(-100)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def nonSinglComps(bucket):
	bucketStr=str(bucket)
	folder=getFolder(bucketStr)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0:
				s.append(len(comps)-len(nx.isolates(G)))
			else:
				s.append(-100)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def clustComp(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			i=3
			if len(comps)>i:
				s.append(nx.transitivity(comps[i]))
			else:
				s.append(-100)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def clustering(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	c=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				c.append(nx.transitivity(G))
			else:
				c.append(-100)
	#np.array(c).tofile('globalClustering.txt',sep=',')
	return c
	
def degreeAssort(bucket,weight):
	bucket=str(bucket)
	folder=getFolder(bucket)
	r=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if G.number_of_edges()>0:
				r.append(nx.degree_assortativity_coefficient(G, weight=weight))
			else:
				r.append(-100)
	#np.array(r).tofile('degreeAssort.txt',sep=',')
	return r
	
def harmCent(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	c=[]
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>1: #denominator of harm cent is num_nodes-1
				cent=cent_measures.harm_cent(G)
				c.append(sorted(cent, key=cent.get)[0])
				#slice.append(file)
			else:
				c.append(-100)
	#np.array(c).tofile('harmCent.txt',sep=',')
	#np.array(slice).tofile('harmCentSlices.txt',sep=',')
	return c
	
def btwCent(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	c=[]
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				cent=cent_measures.btw_cent(G)
				c.append(sorted(cent, key=cent.get)[0])
				#slice.append(file)
			else:
				c.append(-100)
	#np.array(c).tofile('btwCent.txt',sep=',')
	#np.array(slice).tofile('btwCentSlices.txt',sep=',')
	return c
	
def eigCent(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	c=[]
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				cent=cent_measures.eig_cent(G)
				c.append(sorted(cent, key=cent.get)[0])
				#slice.append(file)
			else:
				c.append(-100)
	#np.array(c).tofile('eigCent.txt',sep=',')
	#np.array(slice).tofile('eigCentSlices.txt',sep=',')
	return c

def pagerank(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	c=[]
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				cent=nx.pagerank(G)
				c.append(sorted(cent, key=cent.get)[0])
				#slice.append(file)
			else:
				c.append(-100)
	#np.array(c).tofile('eigCent.txt',sep=',')
	#np.array(slice).tofile('eigCentSlices.txt',sep=',')
	return c

def degCent(bucket, index):
	bucket=str(bucket)
	folder=getFolder(bucket)
	c=[]
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>index+1: #degree_centrality has s=1.0/(len(G)-1.0)
				cent=nx.degree_centrality(G)
				c.append(sorted(cent, key=cent.get)[index])
				#slice.append(file)
			else:
				c.append(-100)
	#np.array(c).tofile('eigCent.txt',sep=',')
	#np.array(slice).tofile('eigCentSlices.txt',sep=',')
	return c

def propInList(bucket, list):
	bucket=str(bucket)
	folder=getFolder(bucket)
	expProp=[] #proportion of users in some list - experienced, in wiki, and so forth
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			#G=getJsonNet(path)
			G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				names=G.nodes()
				users=pd.Series(names)
				exp=users.isin(list)
				expProp.append(sum(exp)/float(len(exp)))
				#slice.append(file)
			else:
				expProp.append(-100)
	return expProp

def propExp(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	expProp=[] #proportion of users in some list - experienced, in wiki, and so forth
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				expAttr=nx.get_node_attributes(G,'status')
				exp=sum(x=='Experienced' for x in expAttr.values())
				expProp.append(exp/float(len(expAttr)))
				#slice.append(file)
			else:
				expProp.append(-100)
	return expProp

def propCompList(bucket, list):
	bucket=str(bucket)
	folder=getFolder(bucket)
	expProp=[] #proportion of users in some list - experienced, in wiki, and so forth
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			#G=getJsonNet(path)
			G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			i=0
			if (len(comps)>i) and (len(comps[i])>1): 
			#non-empty graph and lagrest component is non-singleton
				names=comps[i].nodes()
				users=pd.Series(names)
				exp=users.isin(list)
				expProp.append(sum(exp)/float(len(exp)))
				#slice.append(file)
			else:
				expProp.append(-100)
	return expProp

def propCompExp(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	expProp=[] #proportion of users in some list - experienced, in wiki, and so forth
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			i=0
			if (len(comps)>i) and (len(comps[i])>1): 
			#non-empty graph and lagrest component is non-singleton
				expAttr=nx.get_node_attributes(comps[i],'status')
				exp=sum(x=='Experienced' for x in expAttr.values())
				expProp.append(exp/float(len(expAttr)))
				#slice.append(file)
			else:
				expProp.append(-100)
	return expProp

def expAssort(bucket):
	bucket=str(bucket)
	folder=getExpFolder(bucket)
	r=[] #proportion of users in some list - experienced, in wiki, and so forth
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gpickle(folder+file)
			G=nx.Graph(G)
			if G.number_of_edges()>0:
				r.append(nx.attribute_assortativity_coefficient(G, 'experienced'))
			else:
				r.append(-100)
	return r

def expAssortNew(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	r=[] #proportion of users in some list - experienced, in wiki, and so forth
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			G=nx.Graph(G)
			if G.number_of_edges()>0:
				r.append(nx.attribute_assortativity_coefficient(G, 'status'))
			else:
				r.append(-100)
	return r

def compSizeConfig(bucket, reps):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			#G=getJsonNet(path)
			G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				cmg=config_model.configModelGraphs(G,reps) #get reps number of graphs from config model - w/ the same deg dist
				sizes=np.zeros(reps)
				for i in xrange(reps): #for each of simulated graphs
					comps=sorted(nx.connected_component_subgraphs(cmg[i]), key = len, reverse=True)
					sizes[i]=len(comps[0])/float(len(G)) #no else needed - seede with 0s already
				s.append(sizes.mean())
			else:
				s.append(0)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def clusteringConfig(bucket, reps):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			#G=getJsonNet(path)
			G=nx.read_gml(path)
			G=nx.Graph(G)
			cmg=config_model.configModelGraphs(G,reps) #get reps number of graphs from config model - w/ the same deg dist
			clust=-100*np.ones(reps)
			for i in xrange(reps): #for each of simulated graphs
				if len(G)>0:
					clust[i]=nx.transitivity(cmg[i]) #seeded with -100 already for empty nets
			clust=clust[clust>-100] #only use the networks where clust could be calculated
			if len(clust)>0:
				s.append(clust.mean())
			else:
				s.append(-100)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def singlConfig(bucket, reps):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			#G=getJsonNet(path)
			G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				cmg=config_model.configModelGraphs(G,reps) #get reps number of graphs from config model - w/ the same deg dist
				singl=-100*np.ones(reps)
				for i in xrange(reps): #for each of simulated graphs
					singl[i]=len(nx.isolates(cmg[i]))/float(len(cmg[i]))
				s.append(singl.mean())
			else:
				s.append(0)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s

def weightAssortConfig(bucket, reps):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			#G=getJsonNet(path)
			G=nx.read_gml(path)
			G=nx.Graph(G)
			if G.number_of_edges()>0:
				cmg=config_model.weightConfigModelGraphs(G,reps) #get reps number of graphs from config model - w/ the same deg dist
				assort=-100*np.ones(reps)
				for i in xrange(reps): #for each of simulated graphs
					if cmg[i].number_of_edges>0:
						assort[i]=nx.degree_assortativity_coefficient(cmg[i], weight='weight')
				assort=assort[assort>-100] #only use the networks where assort could be calculated
				if len(assort)>0:
					s.append(assort.mean())
				else:
					s.append(-100)
			else:
				s.append(-100)
	#np.array(s).tofile('largestCompFracSize.txt',sep=',')
	return s


def newbOutDegree(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	newb=[]
	exp=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			newbs=list(n for n in G if G.node[n]['status']=='New')
			if len(newbs)>0:
				degree=G.out_degree()
				df=pd.DataFrame()
				df['names']=degree.keys()
				df['degs']=degree.values()
				newbAvgDeg=(df.degs[df.names.isin(newbs)]).mean()
				expAvgDeg=(df.degs[~df.names.isin(newbs)]).mean()
			else:
				newbAvgDeg=-100
				expAvgDeg=-100
			newb.append(newbAvgDeg)
			exp.append(expAvgDeg)
	#np.array(n).tofile('networkSize.txt',sep=',')
	return newb, exp