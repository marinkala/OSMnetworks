import pandas as pd
import TimeNetworksAnalytics as TN

bucket=8
df=pd.DataFrame()
time=pd.date_range(start='1/12/2010',end='2/12/2010',freq=str(bucket)+'H')
df['time']=time[:-1]
name, size=TN.networkSize(bucket)
df['name']=name
df['netSize']=size
df['diameter']=TN.diameter(bucket)
df['compSize']=TN.relCompSize(bucket)
df['clustering']=TN.clustering(bucket)
df['assort']=TN.degreeAssort(bucket, 'None')
df['weightAssort']=TN.degreeAssort(bucket,'weight')
df['harmCent']=TN.harmCent(bucket)
df['btwCent']=TN.btwCent(bucket)
#df['eigCent']=TN.eigCent(bucket)
df['pagerank']=TN.pagerank(bucket)
df['degCent1']=TN.degCent(bucket,0)
df['degCent2']=TN.degCent(bucket,1)
df['degCent3']=TN.degCent(bucket,2)
df['degCent4']=TN.degCent(bucket,3)
df['degCent5']=TN.degCent(bucket,4)

df.to_csv('TimeSliceNetStats'+bucket+'H.csv', encoding='utf-8')