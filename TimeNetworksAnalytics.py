import networkx as nx
import numpy as np
import pandas as pd
import os.path
import cent_measures

def getFolder(bucket):
	folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/\
overlapping_changesets_by_'+bucket+'_hour/'
	return folder

def networkSize(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	n=[]
	name=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			name.append(file)
			G=nx.read_gml(folder+file)
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
	folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/'
	y=np.fromfile(folder+'AvgNet'+quantString+'/overlapping_changesets_by_'+bucket\
	+'_hour_avg'+quantString+'.txt',sep=',')
	return y
	
def diameter(bucket): #diameter of largest componenent
	bucket=str(bucket)	
	folder=getFolder(bucket)
	d=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0:
				d.append(nx.diameter(comps[0]))
			else:
				d.append(0)
	#np.array(d).tofile('largestCompDiameter.txt',sep=',')
	return d
	
def relCompSize(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	s=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0:
				s.append(len(comps[0])/float(len(G)))
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
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			if len(G)>0:
				s.append(len(nx.isolates(G))/float(len(G)))
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
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
			if len(G)>0:
				s.append(nx.transitivity(comps[0]))
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
			G=nx.read_gml(folder+file)
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
			G=nx.read_gml(folder+file)
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
			G=nx.read_gml(folder+file)
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
			G=nx.read_gml(folder+file)
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
			G=nx.read_gml(folder+file)
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
			G=nx.read_gml(folder+file)
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
			G=nx.read_gml(folder+file)
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
			G=nx.read_gml(folder+file)
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