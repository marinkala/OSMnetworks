import numpy as np
import networkx as nx
import cent_measures

def under_model(G,reps):
	old_clustering=nx.clustering(G).values()
	degree=G.degree().values()

	clust_mat=np.zeros((reps,G.number_of_nodes()))
	for i in xrange(reps):
		C=nx.configuration_model(degree)
		C=nx.Graph(C) #remove parallel edges
		C.remove_edges_from(C.selfloop_edges()) #remove self-loops
		clustering=nx.clustering(C)
		clust_mat[i]=clustering.values()
	means=np.mean(clust_mat, axis=0) #mean over iterations for each node
	per25=np.percentile(clust_mat, 25, axis=0)
	per75=np.percentile(clust_mat, 75, axis=0) 
	return [old_clustering-means, old_clustering-per25, old_clustering-per75]
	
def under_weighted_model(G,reps):
	lmbda=1
	old_clustering=nx.clustering(G).values()
	degree=G.degree().values()

	clust_mat=np.zeros((reps,G.number_of_nodes()))
	for i in xrange(reps):
		C=nx.configuration_model(degree)
		C=nx.Graph(C) #remove parallel edges
		C.remove_edges_from(C.selfloop_edges()) #remove self-loops
		for e in C.edges():
			C.edge[e[0]][e[1]]['weight']=np.random.poisson()+1 #start with 1
		clustering=nx.clustering(C, weight='weight')
		clust_mat[i]=clustering.values()
	means=np.mean(clust_mat, axis=0) #mean over iterations for each node
	per25=np.percentile(clust_mat, 25, axis=0)
	per75=np.percentile(clust_mat, 75, axis=0) 
	return [old_clustering-means, old_clustering-per25, old_clustering-per75]

def configModelGraphs(G,reps):
	degree=G.degree().values()
	graphs=[]
	for i in xrange(reps):
		C=nx.configuration_model(degree)
		C=nx.Graph(C) #remove parallel edges
		C.remove_edges_from(C.selfloop_edges()) #remove self-loops
		graphs.append(C)
	return graphs
	
def weightConfigModelGraphs(G,reps):
	degree=G.degree().values()
	graphs=[]
	for i in xrange(reps):
		C=nx.configuration_model(degree)
		C=nx.Graph(C) #remove parallel edges
		C.remove_edges_from(C.selfloop_edges()) #remove self-loops
		for e in C.edges():
			C.edge[e[0]][e[1]]['weight']=np.random.poisson()+1 #start with 1
		graphs.append(C)
	return graphs

	



