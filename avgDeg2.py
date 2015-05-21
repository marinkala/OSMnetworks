import networkx as nx
import numpy as np
import os.path
from TimeNetworksAnalytics import getJsonNet

folder='/Users/Ish/Dropbox/OSM-Networks-CSCW2016/scratch/co_editing_objects_8hour/'
out_folder='/Users/Ish/Dropbox/OSM/results/Haiti/TwoWeeks/coedited_objects/AvgNetStrength/'

for file in os.listdir(folder):
	av_deg=[]
	if file!='.DS_Store':
		path=folder+file
		G=getJsonNet(path)
		#G=nx.read_gml(path)
		G=nx.Graph(G)
		if len(G)>0:
			A=nx.adjacency_matrix(G)
			strength=A.sum(axis=1)
			avd=strength.mean()
		else:
			avd=0
		av_deg.append(avd)
		np.array(av_deg).tofile(out_folder+'_avgStrength.txt',sep=',')