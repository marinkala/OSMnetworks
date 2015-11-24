import networkx as nx
import numpy as np
import pandas as pd
import os.path
import cent_measures
from networkx.readwrite import json_graph
import json
import config_model


def getFolder(bucket):
	'''folder='/Users/Ish/Documents/OSM_Files/philippines/networks14days/\
overlapping_changesets_by_'+bucket+'_hour/' '''
	folder='/Users/Ish/Documents/OSM_Files/haiti_earthquake/networks14days/\
overlapping_changesets_by_'+bucket+'_hour45Klatest/'
	return folder

def getJsonNet(path):
	data=open(path).read()
	parsed=json.loads(data)
	G=json_graph.node_link_graph(parsed, directed=True)
	return G

def getExpFolder(bucket):
	folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/overlapping_changesets/\
ExpAnnotNets/overlapping_changesets_by_'+bucket+'_hour/'
	return folder

def networkSize(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	nodes=[]
	edges=[]
	name=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			name.append(file)
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.DiGraph(G)
			nodes.append(G.number_of_nodes())
			edges.append(G.number_of_edges())
	return  name, nodes, edges


def clustering(bucket):
	bucket=str(bucket)
	folder=getFolder(bucket)
	c=[]
	trans=[]
	for file in os.listdir(folder):
		if file!='.DS_Store':
			path=folder+file
			G=getJsonNet(path)
			#G=nx.read_gml(path)
			G=nx.Graph(G)
			if len(G)>0:
				c.append(nx.average_clustering(G))
				trans.append(nx.transitivity(G))
			else:
				c.append(-100)
				trans.append(-100)
	return c, trans