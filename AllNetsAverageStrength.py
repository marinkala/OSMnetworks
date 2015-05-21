import networkx as nx
import numpy as np
import os.path
from TimeNetworksAnalytics import getJsonNet

folder='/Users/Ish/Documents/OSM_Files/philippines/networks14days/'
out_folder='/Users/Ish/Dropbox/OSM/results/Philippines/TwoWeeks/intersecting_roads/AvgNetStrength/'

for dir in os.listdir(folder):
	av_strength=[]
	if dir.startswith('intersecting_roads'):
	#if dir!='.DS_Store':
		for file in os.listdir(folder+dir):
			if file!='.DS_Store':
				path=folder+dir+'/'+file
				G=getJsonNet(path)
				#G=nx.read_gml(path)
				G=nx.Graph(G)
				if len(G)>0:
					A=nx.adjacency_matrix(G)
					strength=A.sum(axis=1)
					avs=strength.mean()
				else:
					avs=0
				av_strength.append(avs)
		np.array(av_strength).tofile(out_folder+dir+'_avgStrength.txt',sep=',')
