import networkx as nx
import pandas as pd
import os.path

folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/'
out_folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/ExpAnnotNets/' #networks annotated with user experience

expUsers=pd.Series.from_csv('/Users/Ish/Dropbox/OSM/results/ExperiencedUsers.csv', header=0).values.tolist()

for dir in os.listdir(folder): #each time resolution
	if dir!='.DS_Store':
		if not os.path.exists(out_folder +dir): #if doesn't exist create a corresponding directory for the annotated nets
			os.makedirs(out_folder +dir)
		for file in os.listdir(folder+dir): #each network within that time resolution
			if file!='.DS_Store':
				G=nx.read_gml(folder+dir+'/'+file)
				G=nx.Graph(G)
				if len(G)>0:
					names=G.nodes()
					users=pd.Series(names)
					exp=users.isin(expUsers)
					expAttr=dict(zip(users.values,exp.values))
					nx.set_node_attributes(G,'experienced',expAttr)
				nx.write_gpickle(G,out_folder+dir+'/'+file.rstrip('gml')+'gpickle')
