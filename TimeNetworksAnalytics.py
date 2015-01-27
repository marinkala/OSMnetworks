import networkx as nx
import numpy as np
import os.path
import cent_measures


def networkSize(bucket):
	bucket=str(bucket)
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
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
	
def diameter(bucket):
	bucket=str(bucket)	
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
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
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
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
	
def clustering(bucket):
	bucket=str(bucket)
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
	c=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			if len(G)>0:
				c.append(nx.transitivity(G))
			else:
				c.append(0)
	#np.array(c).tofile('globalClustering.txt',sep=',')
	return c
	
def degreeAssort(bucket,weight):
	bucket=str(bucket)
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
	r=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			if len(G)>0:
				r.append(nx.degree_assortativity_coefficient(G, weight=weight))
			else:
				r.append(-100)
	#np.array(r).tofile('degreeAssort.txt',sep=',')
	return r
	
def harmCent(bucket):
	bucket=str(bucket)
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
	c=[]
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			if len(G)>0:
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
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
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
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
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
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
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
	folder='/Users/Ish/Documents/OSM-Files/haiti_earthquake/networks/\
overlapping_changesets/'+bucket+'_hour/'
	c=[]
	#slice=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			if len(G)>index:
				cent=nx.degree_centrality(G)
				c.append(sorted(cent, key=cent.get)[index])
				#slice.append(file)
			else:
				c.append(-100)
	#np.array(c).tofile('eigCent.txt',sep=',')
	#np.array(slice).tofile('eigCentSlices.txt',sep=',')
	return c