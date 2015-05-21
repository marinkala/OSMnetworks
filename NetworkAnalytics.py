import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import collections as c


def getGraph(bucket):
	folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/intersecting_roads/'
	G=nx.read_yaml(folder+str(bucket)+'hourBigNetworkNodeEdgePers.yaml')
	return G

def plotDegDist(G):
	deg=G.degree()
	h,b=np.histogram(deg.values(),max(deg.values())-min(deg.values()))
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Node Degree')
	plt.ylabel('Relative Frequency')
	plt.title('Degree Distribution')
	plt.show()
	
def getStrength(G):
	A=nx.adjacency_matrix(G)
	strength=A.sum(axis=1)
	return strength
	
def plotStrenghDist(G):
	strength=getStrength(G)
	h,b=np.histogram(strength,100)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=(max(strength)-min(strength))[0,0]/float(100)) 
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Node Strength')
	plt.ylabel('Relative Frequency')
	plt.title('Strength Distribution')
	plt.show()
	
def plotWeightDist(G):
	weights=nx.get_edge_attributes(G,'weight').values()
	h,b=np.histogram(weights,125)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Edge Weight')
	plt.ylabel('Relative Frequency')
	plt.title('Edge Weight Distribution')
	plt.show()
	
def plotRatioDist(G):
	strength=getStrength(G)
	deg=G.degree().values()
	deg_mat=np.matrix(deg).T
	ratio=strength/deg_mat
	h,b=np.histogram(ratio,100)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=3.1398)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Node Strength to Degree Ratio')
	plt.ylabel('Relative Frequency')
	plt.title('Ratio Distribution')
	plt.show()
	
def plotEdgePersistenceDist(G):
	weights=nx.get_edge_attributes(G,'persistence').values()
	bins=max(weights)-min(weights)
	h,b=np.histogram(weights,bins)
	h1=h/float(sum(h))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	plt.xlabel('Edge Persistence')
	plt.ylabel('Relative Frequency')
	plt.title('Edge Persistence Distribution')
	plt.show()

def plotNodePersistenceDist(G):
	pers=nx.get_node_attributes(G,'persistence').values()
	h,b=np.histogram(pers,max(pers)-min(pers))
	h1=h/float(len(pers))
	plt.bar(b[:len(b)-1],h1, width=1)
	plt.xlim(xmin=min(pers),xmax=max(pers))
	plt.ylim(ymin=0)
	plt.xlabel('Node Persistence')
	plt.ylabel('Relative Frequency')
	plt.title('Node Persistence Distribution')
	plt.show()

def basicStats(G):
	print 'number of nodes: ', len(G)
	print 'number of edges: ', G.number_of_edges()
	comps=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)
	print 'relative size of largest component: ', len(comps[0])/float(len(G))
	print 'diameter: ', nx.diameter(comps[0])
	print 'clustering coefficient: ', nx.transitivity(G)
	print 'degree assort: ', nx.degree_assortativity_coefficient(G)
	print 'weigthed degree assort: ', nx.degree_assortativity_coefficient(G, weight='weight')

def logPlot(bucket):
	folder1='/Users/Ish/Dropbox/OSM/results/TwoWeeks/overlapping_changesets/'
	folder2='/Users/Ish/Dropbox/OSM/results/TwoWeeks/intersecting_roads/'
	G1=nx.read_yaml(folder1+str(bucket)+'hourBigNetworkNodeEdgePers.yaml')
	G2=nx.read_yaml(folder2+str(bucket)+'hourBigNetworkNodeEdgePers.yaml')

	strength1=getStrength(G1)
	str1=[s[0,0] for s in strength1]
	freq1=c.Counter(str1)
	y1=freq1.values()
	x1=freq1.keys()
	logx1=np.log(x1)
	logy1=np.log(y1)
	coeffs1=np.polyfit(logx1[1:],logy1[1:],deg=1,w=logy1[1:])
	poly1=np.poly1d(coeffs1)
	#a=np.exp(coeffs[1])
	b1=coeffs1[0]
	eq1=r'$y=\propto x^{'+str(round(b1,2))+'}$'

	strength2=getStrength(G2)
	str2=[s[0,0] for s in strength2]
	freq2=c.Counter(str2)
	y2=freq2.values()
	x2=freq2.keys()
	logx2=np.log(x2)
	logy2=np.log(y2)
	coeffs2=np.polyfit(logx2[1:],logy2[1:],deg=1,w=logy2[1:])
	poly2=np.poly1d(coeffs2)
	#a=np.exp(coeffs[1])
	b2=coeffs2[0]
	eq2=r'$y=\propto x^{'+str(round(b2,2))+'}$'

	plt.figure()
	plt.loglog(x1,y1,'o',alpha=0.5) #excludes rt_count of 0, since log=-inf
	plt.loglog(x2,y2,'o',alpha=0.5) #excludes rt_count of 0, since log=-inf
	plt.xlabel('Node strength')
	plt.ylabel('Frequency')
	plt.xlim(xmin=0)
	plt.ylim(ymin=0)
	yfit1 = lambda x: np.exp(poly1(np.log(x)))
	yfit2 = lambda x: np.exp(poly2(np.log(x)))
	plt.loglog(x1,yfit1(x1),'r-',linewidth=2,label=eq1)
	plt.loglog(x2,yfit2(x2),'r--',linewidth=2,label=eq2)
	plt.legend()
	leg=plt.gca().get_legend()
	plt.setp(leg.get_texts(), fontsize='18') 
	leg.draw_frame(False)

	'''a = axes([0.45, 0.38, .42, .42])
	bins=range(1,81,2)
	plt.hist(glob, bins, normed=1, alpha=0.5, label='Global/Global')
	plt.hist(loc, bins, normed=1, alpha=0.5, label='Global/ \n Geo-Vulnerable')
	plt.ylim(ymax=0.362)
	plt.legend(loc='upper right')
	plt.gca().get_legend().draw_frame(False)
	plt.title('Histogram')
	setp(a, yticks=[0.1,0.2,0.3], xticks=[0,20,40,60,80])'''
	plt.savefig('/Users/Ish/Dropbox/OSM/results/TwoWeeks/8HbigNetsStrengthLog.jpg')
	plt.close()

#G=getGraph(8)
#basicStats(G)
#plotDegDist(G)
#plotStrenghDist(G)
#plotWeightDist(G)
#plotEdgePersistenceDist(G)
logPlot(8)