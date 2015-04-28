import networkx as nx
import os.path

def composeWeights(G,H):
	edgesH=H.edges()
	edge_intersect=list(set(G.edges()) & set(edgesH))#get the intersection of edges of G & H
	edge_persH=[1]*len(edgesH)
	edge_pers_attrH=dict(zip(edgesH,edge_persH))
	nx.set_edge_attributes(H,'persistence',edge_pers_attrH)
	nodesH=H.nodes()
	node_intersect=list(set(G.nodes()) & set(nodesH))#intersection of nodes b/w G & H
	node_persH=[1]*len(nodesH)
	node_pers_attrH=dict(zip(nodesH,node_persH))
	nx.set_node_attributes(H,'persistence',node_pers_attrH)
	K=nx.compose(G,H)
	for i in xrange(len(edge_intersect)):
		source=edge_intersect[i][0]
		target=edge_intersect[i][1]
		K[source][target]['weight']=G[source][target]['weight']+H[source][target]['weight']
		K[source][target]['persistence']=G[source][target]['persistence']+\
		H[source][target]['persistence']
	for i in xrange(len(node_intersect)):
		node_id=node_intersect[i]
		K.node[node_id]['persistence']=G.node[node_id]['persistence']+\
		H.node[node_id]['persistence']
	return K

def combineAll(bucket):
	bucket=str(bucket)
	folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks/overlapping_changesets_by_'+\
	bucket+'_hour/'
	B=nx.Graph()
	for file in os.listdir(folder):
		if file!='.DS_Store': #weird MAC thing
			G=nx.read_gml(folder+file)
			G=nx.Graph(G)
			B=composeWeights(B,G)
	#return B
	nx.write_yaml(B,'../results/'+bucket+'hourBigNetworkNodeEdgePers.yaml')

combineAll(8)
