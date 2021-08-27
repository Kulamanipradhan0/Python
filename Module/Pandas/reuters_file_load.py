import os,datetime,psycopg2 as pg
import pandas as pd
import dask.dataframe as dd

os.chdir("H:\Sprints\mifid\Temporary\BANCS_Identification")
filename='IDENTIFICATION_20210309.csv'
p_bsdate=20210109
p_bccentity='FCA'
seqnum=1


print('Started : ',datetime.datetime.now())
sitrds = pg.connect(host='10.248.150.213',
                    port='5444',
                    database='i200gut1',
                    user='grip_own',
                    password='changeme')
cursor = sitrds.cursor()
print("You are connected to SIT RDS atabase(User : grip_own)")

header_col=list(pd.read_csv(filename, nrows=1, sep='|').columns)
print(header_col)
df=pd.read_csv(filename,sep='|',header=1,quotechar='"',chunksize=10000)
df=pd.DataFrame(df)
#df=df.fillna('')
print(df.columns)

df=pd.read_csv('H:\Sprints\mifid\Temporary\BANCS_Identification\IDENTIFICATION_20210309.csv',sep='|',header=1,quotechar='"',chunksize=10000)

#print(df.info())
#print(df[['INSTRMNT_ID', 'OLD_SCRTY_ID', 'RANK', 'SEC_ID_SCHM', 'SEC_ID_SCHM_CD']])
