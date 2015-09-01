import networkx as nx
import os.path
from TimeNetworksAnalytics import getJsonNet

def getFolders(bucket,place, netType):
	if place=='h':
		place_string='haiti_earthquake'
		out_string='Haiti'
	else:
		place_string='philippines'
		out_string='Philippines'
	if netType=='changeset':
		netString='overlapping_changesets'
	else:
		netString='intersecting_roads'
	in_folder='/Users/Ish/Documents/OSM_Files/'+place_string+'/networks14days/'+netString+'_by_'+str(bucket)+'_hour/'
	out_folder='/Users/Ish/Dropbox/OSM/results/'+out_string+'/TwoWeeks/'+netString+'/'+str(bucket)+\
'hourBigNetworkNodeEdgePersDir.yaml'
	return in_folder, out_folder

def composeWeights(G,H): #H is the new network being appended to the overall net G
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
		K[node_id]['weight']=G[node_id]['weight']+H[node_id]['weight']
		K.node[node_id]['persistence']=G.node[node_id]['persistence']+\
		H.node[node_id]['persistence']
	return K

def combineAll(folder):
	#expFolder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/overlapping_changesets/ExpAnnotNets/\
#overlapping_changesets_by_'+bucket+'_hour/'
	B=nx.DiGraph()
	for file in os.listdir(folder):
		if file!='.DS_Store': #weird MAC thing
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.DiGraph(G)
			B=composeWeights(B,G)
	#return B
	nx.write_yaml(B,'/Users/Ish/Dropbox/OSM/results/Haiti/TwoWeeks/overlapping_changesets/'+str(bucket)+\
'hourBigNetworkNodeEdgePersDir.yaml')

in_folder, out_folder=getFolders(8,'h','changeset')
combineAll(folder)
