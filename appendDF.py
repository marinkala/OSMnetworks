import TimeNetworksAnalytics as TN
import pandas as pd

bucket=8
df=pd.DataFrame.from_csv('/Users/Ish/Dropbox/OSM/results/Haiti/TwoWeeks/overlapping_changesets/\
TimeSliceNetStats'+str(bucket)+'H2weeks.csv')

reps=1000
df['compSizeCM']=TN.compSizeConfig(bucket, reps)
df['clustCM']=TN.clusteringConfig(bucket, reps)
df['singlCM']=TN.singlConfig(bucket, reps)
df['weightAssortCM']=TN.weightAssortConfig(bucket,reps)

df.to_csv('/Users/Ish/Dropbox/OSM/results/Haiti/TwoWeeks/overlapping_changesets/\
TimeSliceNetStats'+str(bucket)+'H2weeks.csv', encoding='utf-8')