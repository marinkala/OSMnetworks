import networkx as nx
import re
import numpy as np

def deg_cent(G):
	degree=G.degree()
	n=float(G.number_of_nodes())
	deg_cent=dict.fromkeys(degree.keys())
	deg_cent.update((key, value/n) for key, value in degree.items())
	return deg_cent

def harm_cent(G):
	harm_cent={}
	sp=nx.shortest_path_length(G)
	for node in sp:
		pathl=sp[node].values()
		pathl.remove(0) #get rid of 0-length path to self
		inv_pathl=[x**(-1) for x in pathl] #1 over pathl
		harmc=sum(inv_pathl)/float((G.number_of_nodes()-1))
		harm_cent[node]=harmc
	return harm_cent
		
def eig_cent(G):
	eig_cent=nx.eigenvector_centrality_numpy(G)
	return eig_cent

def btw_cent(G):
	nx_btw=nx.betweenness_centrality(G, endpoints=True,normalized=False)
	#counts, including the end points and accounting for multiple geodesic paths
	n=float(G.number_of_nodes())
	btw_cent=dict.fromkeys(nx_btw.keys())
	btw_cent.update((key, value/n**2) for key, value in nx_btw.items())
	return btw_cent
	
def  eig_cent2(G):
	A=nx.adj_matrix(G,nodelist=G.nodes())
	eigenvalues,eigenvectors=np.linalg.eig(A)
	# eigenvalue indices in reverse sorted order
	ind=eigenvalues.argsort()[::-1]
	# eigenvector of largest eigenvalue at ind[0], normalized
	largest=np.array(eigenvectors[:,ind[0]]).flatten()
	norm=np.sign(largest.sum())*np.linalg.norm(largest)
	centrality=dict(zip(G,largest/norm))
	return centrality
