# Imports
import pandas as pd
import os,io
import psycopg2 as pg

sitrds = pg.connect(host='localhost',
                     port='5432',
                     database='postgres',
                     user='postgres',
                     password='password')
cursor = sitrds.cursor()
print("You are connected to database")

os.chdir("")
filename='abc.csv'
p_bsdate=20210109
p_bccentity='FCA'
seqnum=1

# This CSV doesn't have a header so pass
# column names as an argument
srccolumns = [
    "root",
    "id",
    "timestamp",
    "version"
]
techcols = ["p_bsdate","p_bccentity","seqnum"]

target_column_list=["es_root","es_id","es_timestamp","es_version","es_businessdate","es_bccentity","es_sequencenum"]

tgt_col_list=','.join(target_column_list)

print(tgt_col_list)


def time_to_int(dfc):
    dfc=pd.to_datetime(dfc, format="%Y-%m-%dT%H:%M:%SZ",errors = 'coerce')
    dfc=dfc.dt.strftime('%Y%d%m')
    return dfc

# Create an iterable that will read "chunksize=1000" rows
# at a time from the CSV file
for df in pd.read_csv(filename,sep=';',header=1,names=srccolumns,chunksize=10**6):
    output = io.StringIO() # For Python3 use StringIO
    df['es_businessdate']=p_bsdate
    df['es_bccentity']=p_bccentity
    df['es_sequencenum']=seqnum

    print(df.head(10))
    df.to_csv(output, sep='\t', header=True, index=False)
    output.seek(0) # Required for rewinding the String object
    print("----------")
    copy_query = "COPY dwh_own.tb_d_abc"+" ("+tgt_col_list+") "+" FROM STDOUT csv DELIMITER '\t' NULL ''  ESCAPE '\\' HEADER "
    cursor.copy_expert(copy_query, output)
    sitrds.commit()
