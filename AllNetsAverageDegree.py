import networkx as nx
import numpy as np
import os.path
from TimeNetworksAnalytics import getJsonNet

folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/'
out_folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/intersecting_roads/AvgNetDegs/'

for dir in os.listdir(folder):
	av_deg=[]
	if dir.startswith('intersecting_roads_by_12'):
	#if dir!='.DS_Store':
		for file in os.listdir(folder+dir):
			if file!='.DS_Store':
				path=folder+dir+'/'+file
				G=getJsonNet(path)
				#G=nx.read_gml(path)
				G=nx.Graph(G)
				if len(G)>0:
					deg=nx.degree(G)
					avd=np.mean(deg.values())
				else:
					avd=0
				av_deg.append(avd)
		np.array(av_deg).tofile(out_folder+dir+'_avgDegs.txt',sep=',')
	
