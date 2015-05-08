import networkx as nx
import numpy as np
import os.path

folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/'
out_folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/AvgNetStrength/'

for dir in os.listdir(folder):
	av_strength=[]
	if dir!='.DS_Store':
		for file in os.listdir(folder+dir):
			if file!='.DS_Store':
				G=nx.read_gml(folder+dir+'/'+file)
				G=nx.Graph(G)
				if len(G)>0:
					A=nx.adjacency_matrix(G)
					strength=A.sum(axis=1)
					avs=strength.mean()
				else:
					avs=0
				av_strength.append(avs)
		np.array(av_strength).tofile(out_folder+dir+'_avgStrength.txt',sep=',')
