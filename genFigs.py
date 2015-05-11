import pandas as pd
import matplotlib.pyplot as plt

def getDF(bucket):
	df=pd.DataFrame.from_csv('/Users/Ish/Dropbox/OSM/results/TimeSliceNetStats'+str(bucket)+'H2weeks.csv')
	return df

def colToLabel(col):
	if col=='netSize':
		label='Network size'
	if col=='compSize':
		label='Relative size of largest connected component'
	if col=='absCompSize':
		label='Size of largest connected component'
	if col=='compClust':
		label='Largest connected component clustering'
	if col=='singlProp':
		label='Proportion of singletons'
	if col=='diameter':
		label='Diameter of largest component'
	if col=='avgDegree':
		label='Network average degree'
	if col=='avgStrength':
		label='Average node strength'
	if col=='clustering':
		label='Network clustering coefficient'
	if col=='assort':
		label='Degree assortativity'
	if col=='weightAssort':
		label='Weighted degree assortativity'
	if col=='expProp':
		label='Proportion of new users'
	if col=='propCompExp':
		label='Proportion of experienced users in largest component'
	if col=='expAssort':
		label='Attribute assortativity based on experience'
	return label

def colToFilter(col):
	if (col=='clustering') | (col=='compClust') | (col=='singlProp') | (col=='assort') | (col=='weightAssort') | (col=='expProp'):
		filt=True
	else:
		filt=False
	return filt

def getYlims(col):
	ymax=1
	if (col=='clustering') | (col=='expProp')| (col=='compClust') | (col=='singlProp'):
		ymin=0
	else:
		ymin=-1
	return ymin, ymax

def overTime(bucket, col):
	bucket=str(bucket)
	df=getDF(bucket)
	label=colToLabel(col)
	filtFlag=colToFilter(col)
	y=df[col]
	if col=='expProp':
		y=1-df[col]
	time=pd.date_range(start='1/12/2010',end='1/26/2010',freq=bucket+'H')
	time=time[:-1]
	if filtFlag:
		select=y[y>-100]
		time=time[y>-100]
		y=select
	fig=plt.figure()
	plt.plot(time, y)
	locs,labels=plt.xticks()
	plt.setp(labels,rotation=-20)
	plt.ylabel(label)
	plt.title('Overlapping changesets by '+ bucket+' hours networks')
	ymin=0
	ymax=max(y)
	if filtFlag:
		ymin,ymax=getYlims(col)
	plt.ylim(ymin=ymin, ymax=ymax)
	plt.xlim(xmin=pd.datetime(2010, 01,12), xmax=max(time))
	if ymin==-1:
		plt.hlines(y=0,xmin=pd.datetime(2010, 01,12), xmax=max(time),color='r',linestyles='--')
	plt.savefig('/Users/Ish/Dropbox/OSM/results/TwoWeeks/Figures/'+bucket+'H/'+bucket+'H'+col+'OverTime.jpg')

def overTimeScatter(bucket, col):
	bucket=str(bucket)
	df=getDF(bucket)
	label=colToLabel(col)
	filtFlag=colToFilter(col)
	y=df[col]
	if col=='expProp':
		y=1-df[col]
	time=pd.date_range(start='1/12/2010',end='1/26/2010',freq=bucket+'H')
	time=time[:-1]
	if filtFlag:
		select=y[y>-100]
		time=time[y>-100]
		y=select
	fig=plt.figure()
	plt.scatter(time, y)
	locs,labels=plt.xticks()
	plt.setp(labels,rotation=-20)
	plt.ylabel(label)
	plt.title('Overlapping changesets by '+ bucket+' hours networks')
	ymin=0
	ymax=max(y)
	if filtFlag:
		ymin,ymax=getYlims(col)
	plt.ylim(ymin=ymin, ymax=ymax)
	plt.xlim(pd.datetime(2010, 01,12), xmax=max(time))
	if ymin==-1:
		plt.hlines(y=0,xmin=pd.datetime(2010, 01,12), xmax=max(time),color='r',linestyles='--')
	plt.savefig('/Users/Ish/Dropbox/OSM/results/TwoWeeks/Figures/'+bucket+'H/'+bucket+'H'+col+'OverTimeScatter.jpg')

def vsSize(bucket, col):
	bucket=str(bucket)
	df=getDF(bucket)
	label=colToLabel(col)
	filtFlag=colToFilter(col)
	y=df[col]
	if col=='expProp':
		y=1-df[col]
	x=df.netSize
	if filtFlag:
		select=y[y>-100]
		x=x[y>-100]
		y=select
	fig=plt.figure()
	plt.scatter(x, y)
	plt.xlabel('Network size')
	plt.ylabel(label)
	plt.title('Overlapping changesets by '+ bucket+' hours networks')
	ymin=0
	ymax=max(y)
	if filtFlag:
		ymin,ymax=getYlims(col)
	plt.ylim(ymin=ymin, ymax=ymax)
	plt.xlim(xmin=0, xmax=max(x))
	if ymin==-1:
		plt.hlines(y=0,xmin=0, xmax=max(x),color='r',linestyles='--')
	plt.savefig('/Users/Ish/Dropbox/OSM/results/TwoWeeks/Figures/'+bucket+'H/'+bucket+'H'+col+'VsSize.jpg')

overTimeScatter(2,'weightAssort')