import pandas as pd

df=pd.DataFrame.from_csv('path')

dense=df[df.compSize>0.9]

degCent1Users=dense.degCent1.unique()
degCent2Users=dense.degCent2.unique()
degCent3Users=dense.degCent3.unique()
degCent4Users=dense.degCent4.unique()
degCent5Users=dense.degCent5.unique()


interDegUsers=list(set(degCent1Users) & set(degCent2Users) & set(degCent3Users) & set(degCent4Users) & set(degCent5Users))
allDegUsers=list(set(degCent1Users) | set(degCent2Users) | set(degCent3Users) | set(degCent4Users) | set(degCent5Users))

wholeList=[]
for i in xrange(len(dense)):
    userList=[dense.degCent1.iloc[i],dense.degCent2.iloc[i], dense.degCent3.iloc[i],dense.degCent4.iloc[i],dense.degCent5.iloc[i]]
    wholeList+=userList



