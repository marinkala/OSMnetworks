import pandas as pd
import TimeNetworksAnalytics as TN

bucket=4
df=pd.DataFrame()
time=pd.date_range(start='1/12/2010',end='1/26/2010',freq=str(bucket)+'H')
df['time']=time[:-1]
name, size=TN.networkSize(bucket)
df['name']=name
df['netSize']=size
df['diameter']=TN.diameter(bucket)
df['avgDegree']=TN.avgQuant('degree', bucket)
df['avgStrength']=TN.avgQuant('strength', bucket)
df['absCompSize']=TN.absCompSize(bucket)
df['compSize']=TN.relCompSize(bucket)
df['singlProp']=TN.singletons(bucket)
df['numComps']=TN.numComps(bucket)
df['nonSinglComps']=TN.nonSinglComps(bucket)
df['clustering']=TN.clustering(bucket)
df['compClust']=TN.clustComp(bucket)
df['assort']=TN.degreeAssort(bucket, None)
df['weightAssort']=TN.degreeAssort(bucket, 'weight')
df['harmCent']=TN.harmCent(bucket)
df['btwCent']=TN.btwCent(bucket)
#df['eigCent']=TN.eigCent(bucket)
df['pagerank']=TN.pagerank(bucket)
df['degCent1']=TN.degCent(bucket,0)
df['degCent2']=TN.degCent(bucket,1)
df['degCent3']=TN.degCent(bucket,2)
df['degCent4']=TN.degCent(bucket,3)
df['degCent5']=TN.degCent(bucket,4)
#expUsers=pd.Series.from_csv('/Users/Ish/Dropbox/OSM/results/ExperiencedUsers.csv', header=0).values.tolist()
'''df['harmCentExp']=df.harmCent.isin(expUsers)
df['btwCentExp']=df.btwCent.isin(expUsers)
df['pagerankExp']=df.pagerank.isin(expUsers)
df['degCent1exp']=df.degCent1.isin(expUsers)
df['degCent2exp']=df.degCent2.isin(expUsers)
df['degCent3exp']=df.degCent3.isin(expUsers)
df['degCent4exp']=df.degCent4.isin(expUsers)
df['degCent5exp']=df.degCent5.isin(expUsers)'''
df['expProp']=TN.propExp(bucket)
df['propCompExp']=TN.propCompExp(bucket)
df['expAssort']=TN.expAssortNew(bucket)


df.to_csv('/Users/Ish/Dropbox/OSM/results/TwoWeeks/intersecting_roads/TimeSliceNetStats'\
+str(bucket)+'H2weeks.csv', encoding='utf-8')