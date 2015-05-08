import networkx as nx
import numpy as np
import os.path

folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/'
out_folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/AvgNetDegs/'

for dir in os.listdir(folder):
	av_deg=[]
	if dir!='.DS_Store':
		for file in os.listdir(folder+dir):
			if file!='.DS_Store':
				G=nx.read_gml(folder+dir+'/'+file)
				G=nx.Graph(G)
				if len(G)>0:
					deg=nx.degree(G)
					avd=np.mean(deg.values())
				else:
					avd=0
				av_deg.append(avd)
		np.array(av_deg).tofile(out_folder+dir+'_avgDegs.txt',sep=',')
	
