import networkx as nx
import os.path
from TimeNetworksAnalytics import getJsonNet
from composeBigNetNodeEdgePers import composeWeights

def getFolder(place, netType):
	if place=='h':
		place_string='haiti_earthquake'
	else:
		place_string='philippines'
	if netType=='changeset':
		netString='overlapping_changesets'
	else:
		netString='intersecting_roads'
	bucket=8
	folder='/Users/Ish/Documents/OSM_Files/'+place_string+'/networks14days/'+netString+'_by_'+str(bucket)+'_hour/'
	return folder

def byNode(user,folder):
	#folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/overlapping_changesets_by_'+bucket+'_hour/'

	timeList=[]
	for file in os.listdir(folder):
		if file!='.DS_Store': #weird MAC thing
			path=folder+file
			G=getJsonNet(path)
			G=nx.DiGraph(G)
			if user in set(G.nodes()):
				print file
				print G.node[user]['weight']
				timeList.append(file)
	return timeList

def byEdge(edge,folder):
	#folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/overlapping_changesets_by_'+bucket+'_hour/'

	timeList=[]
	for file in os.listdir(folder):
		if file!='.DS_Store': #weird MAC thing
			path=folder+file
			G=getJsonNet(path)
			G=nx.DiGraph(G)
			if G.has_edge(edge[0], edge[1]):
				print file
				print edge
				timeList.append(file)
	return timeList

def combineSelectSlices(timeList, folder):
	B=nx.DiGraph()
	for slice in timeList:
		path=folder+slice
		G=getJsonNet(path)
		G=nx.DiGraph(G)
		B=composeWeights(B,G)
	return B
	

folder=getFolder('h', 'changeset')
tl=byNode('rjhale1971',folder)
#B=combineSelectSlices(tl,folder)
#tl2=byEdge((u'Hans van Wijk', u'jgc'),folder)