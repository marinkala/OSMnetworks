import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as date

def plotFreq(quant, bucket): #degree, strength
	if quant=='degree':
		quantString='Degs'
	if quant=='strength':
		quantString='Strength'
	bucket=str(bucket)
	folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/'
	y=np.fromfile(folder+'AvgNet'+quantString+'/overlapping_changesets_by_'+bucket\
	+'_hour_avg'+quantString+'.txt',sep=',')
	time=pd.date_range(start='1/12/2010',end='1/26/2010',freq=bucket+'H')
	fig=plt.figure()
	ax = plt.gca()
	plt.plot(time[:-1], y)
	locs,labels=plt.xticks()
	plt.setp(labels,rotation=-20)
	locator = date.AutoDateLocator()
	locator.intervald['HOURLY'] = [12] 
	plt.ylabel('Average network '+ quant)
	plt.title('Overlapping changesets by '+ bucket+' hours networks')
	plt.savefig(folder+'Figures/'+bucket+'HourAvg'+quantString+'.jpg')
	
def plotRatio(bucket): #degree, strength
	bucket=str(bucket)
	folder='/Users/Ish/Dropbox/OSM/results/TwoWeeks/'
	strength=np.fromfile(folder+'AvgNetStrength/over_chan_'+bucket\
	+'_hour_avgStrength.txt',sep=',')
	degree=np.fromfile(folder+'AvgNetDegs/over_chan_'+bucket\
	+'_hour_avgDegs.txt',sep=',')
	ratio=np.divide(strength, degree)
	y=np.nan_to_num(ratio)
	time=pd.date_range(start='1/12/2010',end='1/26/2010',freq=bucket+'H')
	fig=plt.figure()
	plt.plot(time[:-1], y)
	locs,labels=plt.xticks()
	plt.setp(labels,rotation=20)
	plt.ylabel('Average strength to degree ratio')
	plt.title('Overlapping changesets by '+ bucket+' hours networks')
	plt.savefig(folder+'Figures/'+bucket+'HourAvgRatio.jpg')

plotFreq('degree', 1)