import networkx as nx
import os.path
from TimeNetworksAnalytics import getJsonNet
from composeBigNetNodeEdgePers import getFolders

def temporal(in_folder, big_folder):
	#find mappers with persistence higher than 1
	#use that list to go through each time slice
	#if more than 50% of the time slices where for the same part of the day - output the mapper and time slices
	B=nx.read_yaml(big_folder)
	users=B.nodes(data=True)
	pers_users=[u[0] for u in users if u[1]['persistence']>1]
	same_time_prop=[0]*len(pers_users) #list to  hold the prop of the same times for each user
	for u in pers_users:
		night=0
		day=0
		evenining=0
		persistence=0
		for file in os.listdir(in_folder):
			if file!='.DS_Store': #weird MAC thing
				path=folder+file
				G=getJsonNet(path)
				G=nx.DiGraph(G)
				if G.has_node(u):
					persistence+=1
					period=str(file)[11:13]
					if period=='03':
						night+=1
					elif period=='11':
						day+=1
					else:
						evenining+=1
		if night/float(persistence)>0.33:
			print u, 'night'
		elif day/float(persistence)>0.33:
			print u, 'day'
		elif evenining/float(persistence)>0.33:
			print u, 'evenining'

in_folder, big_folder=getFolders(8,'h','changeset')