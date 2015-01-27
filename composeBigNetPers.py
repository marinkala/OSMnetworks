import networkx as nx
import os.path

def composeWeights(G,H):
	intersect=list(set(G.edges()) & set(H.edges()))
	edgesH=H.edges()
	persH=[1]*len(edgesH)
	pers_attrH=dict(zip(edgesH,persH))
	nx.set_edge_attributes(H,'persistence',pers_attrH)
	K=nx.compose(G,H)
	for i in xrange(len(intersect)):
		source=intersect[i][0]
		target=intersect[i][1]
		K[source][target]['weight']=G[source][target]['weight']+H[source][target]['weight']
		[source][target]['persistence']=G[source][target]['persistence']+\
		H[source][target]['persistence']
	return K

def combineAll(bucket):
	bucket=str(bucket)
	folder='C:\\Users\\Ish\\VMshared\\networks\\overlapping_changesets_by_'\
	+bucket+'_hour\\'
	B=nx.Graph()
	for file in os.listdir(folder):
		G=nx.read_gml(folder+file)
		G=nx.Graph(G)
		B=composeWeights(B,G)
	#return B
	nx.write_yaml(B,bucket+'hourBigNetwork.yaml')
