import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def getGraph():
	folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/'
	G=nx.read_yaml(folder+'2hourBigNetworkNodeEdgePers.yaml')
	return G

def plotDegDist(G):
	deg=G.degree()
	h,b=np.histogram(deg.values(),max(deg.values())-min(deg.values()))
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Node Degree')
	plt.ylabel('Relative Frequency')
	plt.title('Degree Distribution')
	plt.show()
	
def getStrength(G):
	A=nx.adjacency_matrix(G)
	strength=A.sum(axis=1)
	return strength
	
def plotStrenghDist(G):
	strength=getStrength(G)
	h,b=np.histogram(strength,100)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=(max(strength)-min(strenght))/float(100)) 
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Node Strength')
	plt.ylabel('Relative Frequency')
	plt.title('Strength Distribution')
	plt.show()
	
def plotWeightDist(G):
	weights=nx.get_edge_attributes(G,'weight').values()
	h,b=np.histogram(weights,125)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Edge Weight')
	plt.ylabel('Relative Frequency')
	plt.title('Edge Weight Distribution')
	plt.show()
	
def plotRatioDist(G):
	strength=getStrength(G)
	deg=G.degree().values()
	deg_mat=np.matrix(deg).T
	ratio=strength/deg_mat
	h,b=np.histogram(ratio,100)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=3.1398)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Node Strength to Degree Ratio')
	plt.ylabel('Relative Frequency')
	plt.title('Ratio Distribution')
	plt.show()
	
def plotEdgePersistenceDist(G):
	weights=nx.get_edge_attributes(G,'persistence').values()
	h,b=np.histogram(weights,7)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Edge Persistence')
	plt.ylabel('Relative Frequency')
	plt.title('Edge Persistence Distribution')
	plt.show()

def plotNodePersistenceDist(G):
	pers=nx.get_node_attributes(G,'persistence').values()
	h,b=np.histogram(pers,max(pers)-min(pers))
	h1=h/float(len(pers))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=min(pers),xmax=max(pers))
	plt.ylim(ymin=0)
	plt.xlabel('Node Persistence')
	plt.ylabel('Relative Frequency')
	plt.title('Node Persistence Distribution')
	plt.show()

def basicStats(G):
	print 'number of nodes: ', len(G)
	print 'number of edges: ', G.number_of_edges()
	comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
	print 'relative size of largest component: ', len(comps[0])/float(len(G))
	print 'diameter: ', nx.diameter(comps[0])
	print 'clustering coefficient: ', nx.transitivity(G)
	print 'degree assort: ', nx.degree_assortativity_coefficient(G)
	print 'weigthed degree assort: ', nx.degree_assortativity_coefficient(G, weight='weight')

G=getGraph()
basicStats(G)
plotDegDist(G)
plotStrenghDist(G)