import numpy as np
import copy
import random
import math
import networkx as nx

def sumMat(A):
	return A.sum()
	
def countMat(A):
	return A.size

def onDiagCounts(A):
	edges=sumMat(A)/2.0 #only count edges once - undirected
	posEdges=(countMat(A)-len(A))/2.0 #unly upper triange, excluding diagonal
	return edges, posEdges
	
def offDiagCounts(A):
	edges=sumMat(A)
	posEdges=countMat(A)
	return edges, posEdges
	
def flatten(parts):
	k=len(parts)
	flat=[]
	for i in xrange(k):
		flat+=parts[i]
	return flat
	
def reorder(A,parts):
	p=copy.deepcopy(parts)
	p[0].sort() #sorts within each partition
	p[1].sort()
	new_order=flatten(p) #flatten
	A1=A[:,new_order][new_order]
	return A1	

def myLog(num):
	if num==0:
		res=0
	else:
		res=np.log(num)
	return res
	
def logLikeSBM(A,parts):
	#here we assume len(parts)=2, but it can be more general?
	k=len(parts)
	#get the adhacency matrix and reorganize it to corresond to part
	A1=reorder(A,parts)
	border=len(parts[0]) #get the separating index
	sumTerms=0
	for u in xrange(k):
		for v in xrange(u,k): #v>=u to only counts egdes b/w groups once
			if u==v:
				if u==0: #inside first group
					Euv,Nuv=onDiagCounts(A1[:border,:border])
				else: #inside second group
					Euv,Nuv=onDiagCounts(A1[border:,border:])
			else:
				Euv,Nuv=offDiagCounts(A1[border:,:border])
			logTerm=Euv*myLog(Euv)+(Nuv-Euv)*myLog(Nuv-Euv)-Nuv*myLog(Nuv)
			sumTerms+=logTerm
	return sumTerms
	
def pickRandom(list):
	return random.randrange(0,len(list)) #index of the random 
	
def oneRound(A, parts):
	#assume node indexing starts with 0
	swapped=[[],[]]
	#gr1=list(set(parts[0]).difference(set([0,1,2,32,33])))
	#gr2=list(set(parts[1]).difference(set([0,1,2,32,33])))
	unswapped=copy.deepcopy(parts) #all nodes as they are partitioned
	#unswapped=[gr1,gr2]
	likes=[]
	partitions=[]
	p=[unswapped[0]+swapped[0],unswapped[1]+swapped[1]]
	partitions.append(p) #these two lines are for social partition, since with j=3
	likes.append(logLikeSBM(A,p)) #we'd never get into the loop
	while (len(unswapped[0])>0 and len(unswapped[1])>0):
	#both partition w/in unswapped have elements
		ind1=pickRandom(unswapped[0])
		ind2=pickRandom(unswapped[1])
		swapped[1].append(unswapped[0].pop(ind1))
		swapped[0].append(unswapped[1].pop(ind2))
		partition=[unswapped[0]+swapped[0],unswapped[1]+swapped[1]]
		partitions.append(partition)
		likes.append(logLikeSBM(A,partition))
	#find the index of max likelihood, return than like and partition
	maxL=max(likes)
	maxInd=likes.index(maxL)
	maxP=partitions[maxInd]
	return maxP, maxL
	
def randPart(n,j):
	nodes=range(n)
	parts=[[],[]]
	for i in xrange(j): #start with node 3 for social partition, as 0,1,2 already in 1
		ind=random.randrange(0,len(nodes))
		parts[0].append(nodes.pop(ind))
	parts[1]+=nodes	
	return parts
	
def KL(A,j,t):
	n=len(A)
	P=[]
	L=[]
	rounds=t
	part=randPart(n,j) #choose random partition of [j,n-j]
	P.append(part) 	
	L.append(logLikeSBM(A,part)) #compute its  logL
	for i in xrange(rounds): #should this be while?
		part,like=oneRound(A, P[-1]) #pass the last partition
		P.append(part)
		L.append(like)
	bestL=max(L)
	bestP=P[L.index(bestL)]
	return bestP,bestL
	
def overJ(A,t):
	n=len(A)
	jmax=int(math.ceil(n/2.0))+1
	P=[]
	L=[]
	for j in xrange(1,jmax): #start with 4 for the runs including social part
		part, like=KL(A,j,t)
		P.append(part)
		L.append(like)
	maxL=max(L)
	maxP=P[L.index(maxL)]
	return maxP, maxL
	
def getA():
	G=nx.read_edgelist('karate_club_edges.txt', nodetype=int)
	A=nx.adjacency_matrix(G)
	return A
	
def overT(repeats):
	A=getA()
	n=len(A)
	times=25
	spreadT=xrange(1,times+1)*np.ones(times,dtype=np.int8)*0.5*n
	L=np.zeros((repeats, len(spreadT))) #number of diff t's are # of columns
	P=np.zeros((repeats, len(spreadT)), dtype=object) #to store lists
	#number of iters to average over as # of rows
	for i in xrange(repeats):
		for t in xrange(len(spreadT)):
			p,l=overJ(A,t)
			L[i,t]=l
			P[i,t]=p
	maxL=L.max()
	ind=np.where(L==maxL)
	maxP=P[ind[0][0],ind[1][0]]
	avgL=L.mean(axis=0)
	return avgL,maxL,maxP
	
def offDiagFill(A,prob):
	shape=A.shape
	r=np.random.rand(int(shape[0]),int(shape[1])) #get rands of same dimensions
	A1=r<prob
	return A1
	
def onDiagFill(A,prob):
	n=len(A)
	ed,posEd=onDiagCounts(A)
	r=np.random.rand(posEd) #get rands for above diag
	t=r<prob #does it need to be int?
	count=0
	for i in xrange(n):
		for j in xrange(i+1,n):
			A[i,j]=t[count]
			A[j,i]=t[count]
			count+=1
	#no, need to do it only to upper diagonal and mirror it

def generateA(n1,n2,pin,pout):
	n=n1+n2
	A=np.zeros((n,n))
	border=n1
	k=2
	for u in xrange(k):
		for v in xrange(u,k): #v>=u to only counts egdes b/w groups once
			if u==v:
				if u==0: #inside first group
					onDiagFill(A[:border,:border],pin)
				else: #inside second group
					onDiagFill(A[border:,border:],pin)
			else:
				off=offDiagFill(A[:border,border:], pout)
				A[:border,border:]=off #and mirror that
				A[border:,:border]=off.T
	return A

def estimate(runs):
	n=500
	prob=2/float(n-1)
	pin_h=[]
	pout_h=[]
	l=[]
	p=[]
	for i in xrange(runs):
		A=generateA(30,20,0.2,0.05) #generate synthetic adjacency matrix
		part, like=overJ(A, 400) #fit SBM to the synthetic data
		A1=reorder(A,part)
		border=len(part[0]) #get the separating index
		Euu1,Nuu1=onDiagCounts(A1[:border,:border])
		pinh1=Euu1/float(Nuu1)
		Euu2,Nuu2=onDiagCounts(A1[border:,border:])
		pinh2=Euu2/float(Nuu2)
		Euv,Nuv=offDiagCounts(A1[:border,border:])
		pouth=Euv/float(Nuv)
		pin_h.append((pinh1+pinh2)/2.0)
		pout_h.append(pouth)
		l.append(like)
		p.append(part)
		print i
	return pin_h, pout_h, l,p

pin,pout,l,p=estimate(100)
pinh=np.array(pin)
pouth=np.array(pout)
like=np.array(l)
part=np.array(p)
pinh.tofile('pinh.txt',sep=',')
pouth.tofile('pouth.txt',sep=',')
part.tofile('part.txt',sep=',')
like.tofile('like.txt',sep=',')