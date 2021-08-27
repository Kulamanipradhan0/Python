import os,datetime,psycopg2 as pg
import pandas as pd
import dask.dataframe as dd

os.chdir("")
filename='abc.csv'
p_bsdate=20210109
p_bccentity='FCA'
seqnum=1


print('Started : ',datetime.datetime.now())
sitrds = pg.connect(host='localhost' ,
                    port='5432',
                    database='postgres',
                    user='postgres',
                    password='password')
cursor = sitrds.cursor()
print("You are connected to database (postgres)")

header_col=list(pd.read_csv(filename, nrows=1, sep='|').columns)
print(header_col)
df=pd.read_csv(filename,sep='|',header=1,quotechar='"',chunksize=10000)
df=pd.DataFrame(df)
#df=df.fillna('')
print(df.columns)

df=pd.read_csv('abc.csv',sep='|',header=1,quotechar='"',chunksize=10000)

#print(df.info())
