from sqlalchemy import create_engine
import psycopg2, os,pandas as pd
import io,datetime,sys
from dask import dataframe as ddf

starttime=datetime.datetime.now()
print('Processed : ',starttime)
print("----------")
#
engine = create_engine('postgresql+psycopg2://:@:/')
os.chdir("H:\Sprints\mifid\Temporary")
filename='REUPRD_20210709_FCA_MICS_P01_20210710042221.csv'
tablename='py_reuters_product'
delimiter=','

conn = engine.raw_connection()
cursor = conn.cursor()

# df=pd.read_csv(filename,sep=delimiter,quotechar='"',nrows=2000)
# print([df.columns[i] for i in range(0,len(df.columns))])

with open(filename,'r', encoding="utf-8") as f:
    copy_query = "COPY grip_own."+tablename+" FROM STDOUT csv DELIMITER '"+delimiter+"' HEADER QUOTE '"+'"'+"'"
    cursor.copy_expert(copy_query, f)
    conn.commit()

endtime=datetime.datetime.now()
print('Processed : ',endtime)
print('Total Processed Time : ',endtime-starttime)
