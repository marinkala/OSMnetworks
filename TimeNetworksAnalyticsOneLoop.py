import networkx as nx
import numpy as np
import os.path
import cent_measures

def networkSize():
	folder='/Users/Ish/Documents/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	n=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			n.append(len(G))
	#np.array(n).tofile('networkSize.txt',sep=',')
	return n
	
def diameter():
	folder='/Users/Ish/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	d=[]
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		comps=nx.connected_component_subgraphs(G)
		if len(G)>0:
			d.append(nx.diameter(comps[0]))
		else:
			d.append(0)
	np.array(d).tofile('largestCompDiameter.txt',sep=',')
	
def relCompSize():
	folder='/Users/Ish/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	s=[]
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		comps=nx.connected_component_subgraphs(G)
		if len(G)>0:
			s.append(len(comps[0])/float(len(G)))
		else:
			s.append(0)
	np.array(s).tofile('largestCompFracSize.txt',sep=',')
	
def clustering():
	folder='/Users/Ish/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	c=[]
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		if len(G)>0:
			c.append(nx.transitivity(G))
		else:
			c.append(0)
	np.array(c).tofile('globalClustering.txt',sep=',')
	
def degreeAssort():
	folder='/Users/Ish/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	r=[]
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		if len(G)>0:
			r.append(nx.degree_assortativity_coefficient(G, weight='weight'))
		else:
			r.append('nan')
	np.array(r).tofile('degreeAssort.txt',sep=',')
	
def harmCent():
	folder='/Users/Ish/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	c=[]
	slice=[]
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		if len(G)>0:
			cent=cent_measures.harm_cent(G)
			c.append(sorted(cent, key=cent.get)[0])
			slice.append(file)
	np.array(c).tofile('harmCent.txt',sep=',')
	np.array(slice).tofile('harmCentSlices.txt',sep=',')
	
def btwCent():
	folder='/Users/Ish/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	c=[]
	slice=[]
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		if len(G)>0:
			cent=cent_measures.btw_cent(G)
			c.append(sorted(cent, key=cent.get)[0])
			slice.append(file)
	np.array(c).tofile('btwCent.txt',sep=',')
	np.array(slice).tofile('btwCentSlices.txt',sep=',')
	
def eigCent():
	folder='/Users/Ish/VMshared/networks/reEncoded/overlapping_changesets_by_8_hour_undirected/'
	c=[]
	slice=[]
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		if len(G)>0:
			cent=cent_measures.eig_cent(G)
			c.append(sorted(cent, key=cent.get)[0])
			slice.append(file)
	np.array(c).tofile('eigCent.txt',sep=',')
	np.array(slice).tofile('eigCentSlices.txt',sep=',')