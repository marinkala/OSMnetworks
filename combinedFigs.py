import pandas as pd
import matplotlib.pyplot as plt

def colToLabel(col):
	if col=='netSize':
		label='Network size'
	if col=='compSize':
		label='Largest component size'
	if col=='singlProp':
		label='Fraction of singletons'
	if col=='avgDegree':
		label='Network average degree'
	if col=='avgStrength':
		label='Average node strength'
	if col=='clustering':
		label='Network clustering'
	if col=='assort':
		label='Degree assortativity'
	if col=='weightAssort':
		label='Weighted assortativity'
	if col=='expProp':
		label='Fraction of new users'
	if col=='propCompExp':
		label='Proportion of experienced users in largest component'
	if col=='expAssort':
		label='Attribute assortativity based on experience'
	return label

def colToFilter(col):
	if (col=='netSize') | (col=='avgDegree') | (col=='avgStrength') | (col=='compSize') :
		filt=False
	else:
		filt=True
	return filt

def getYlims(col):
	ymax=1
	if (col=='assort') | (col=='weightAssort')| (col=='expAssort'):
		ymin=-1
	else:
		ymin=0
	return ymin, ymax

def overTime(event, col, bucket):
	label=colToLabel(col)
	filtFlag=colToFilter(col)
	if event=='haiti':
		oc=haitioc
		ir=haitiir
		co=haitico
		ortime=pd.date_range(start='01/12/2010',end='01/26/2010',freq=str(bucket)+'H')
		time1=ortime[:-1]
		title='Haiti Earthquake'
	else:
		oc=philoc
		ir=philir
		ortime=pd.date_range(start='11/08/2013',end='11/22/2013',freq=str(bucket)+'H')
		time1=ortime[:-1]
		title='Philippines Typhoon Yolanda'
	time2=time1 #the same time values for unfiltered stuff
	time3=time1
	y1=oc[col]
	y2=ir[col]
	y3=co[col]
	if col=='expProp':
		y1=1-oc[col]
		y2=1-ir[col]
	if filtFlag:
		time1=time1[y1>-100]
		y1=y1[y1>-100]
		time2=time2[y2>-100]
		y2=y2[y2>-100]
		time3=time3[y3>-100]
		y3=sy3[y3>-100]
	plt.plot(time1,y1,'c', label='Overlapping changesets')
	plt.plot(time2,y2,'m', label='Intersecting roads')
	plt.plot(time3,y3,'grey', linestyle='--',label='Coedited objects')
	locs,labels=plt.xticks()
	plt.setp(labels,rotation=-20)
	plt.ylabel(label)
	plt.title(title)
	ymin=0
	ymax=max(max(y1), max(y2))
	if (filtFlag) | (col=='compSize'):
		ymin,ymax=getYlims(col)
	plt.ylim(ymin=ymin, ymax=ymax)
	timeLim=max(max(time1), max(time2))
	plt.xlim(xmin=min(ortime), xmax=timeLim)
	if ymin==-1:
		plt.hlines(y=0,xmin=min(ortime), xmax=timeLim,color='r',linestyles='--')
	plt.legend()
	plt.show()

def configDiff(event,bucket):
	cols=['compSizeDiff','clustDiff', 'singlDiff', 'weightAssortDiff']
	ylabels=['Diff in component size','Diff in clusering',\
'Diff in fraction of singletons', 'Diff in weighted assortativity']
	if event=='haiti':
		oc=haitioc
		ir=haitiir
		title='Haiti Earthquake'
	else:
		oc=philoc
		ir=philir
		title='Philippines Typhoon Yolanda'
	bucket=str(bucket)
	title+=': Observed - Configuration model'
	for i in xrange(len(cols)):
		if event=='haiti':
			ortime=pd.date_range(start='01/12/2010',end='01/26/2010',freq=str(bucket)+'H')
			time1=ortime[:-1]
		else: 
			ortime=pd.date_range(start='11/08/2013',end='11/22/2013',freq=str(bucket)+'H')
			time1=ortime[:-1]
		time2=time1 #the same time values for unfiltered stuff
		y1=oc[cols[i]]
		y2=ir[cols[i]]
		time1=time1[y1>-100]
		y1=y1[y1>-100]
		time2=time2[y2>-100]
		y2=y2[y2>-100]
		plt.plot(time1,y1,'co-', label='Overlapping changesets')
		plt.plot(time2,y2,'mo-', label='Intersecting roads')
		locs,labels=plt.xticks()
		plt.setp(labels,rotation=-20)
		plt.ylabel(ylabels[i])
		plt.title(title)
		if cols[i]=='weightAssortDiff':
			ymin=-2
			ymax=2
		else:
			ymin=-1
			ymax=1
		plt.ylim(ymin=ymin, ymax=ymax)
		timeLim=max(max(time1), max(time2))
		plt.xlim(xmin=min(ortime), xmax=timeLim)
		plt.hlines(y=0,xmin=min(ortime), xmax=timeLim,color='r',linestyles='--', label='Expected under Configuration Model')
		if cols[i]=='compSizeDiff':
			loc=1
		else:
			loc=4
		plt.legend()
		plt.show()

bucket=8
haitioc=pd.DataFrame.from_csv('/Users/Ish/Dropbox/OSM/results/Haiti/TwoWeeks/overlapping_changesets/\
TimeSliceNetStats'+str(bucket)+'H2weeks.csv')
haitiir=pd.DataFrame.from_csv('/Users/Ish/Dropbox/OSM/results/Haiti/TwoWeeks/intersecting_roads/\
TimeSliceNetStats'+str(bucket)+'H2weeks.csv')
philoc=pd.DataFrame.from_csv('/Users/Ish/Dropbox/OSM/results/Philippines/TwoWeeks/overlapping_changesets/\
TimeSliceNetStats'+str(bucket)+'H2weeks.csv')
philir=pd.DataFrame.from_csv('/Users/Ish/Dropbox/OSM/results/Philippines/TwoWeeks/intersecting_roads/\
TimeSliceNetStats'+str(bucket)+'H2weeks.csv')
haitico=pd.DataFrame.from_csv('/Users/Ish/Dropbox/OSM/results/Haiti/TwoWeeks/coedited_objects/\
TimeSliceNetStats'+str(bucket)+'H2weeks.csv')

overTime('haiti', 'compSize',bucket)
#configDiff('phil', bucket)
