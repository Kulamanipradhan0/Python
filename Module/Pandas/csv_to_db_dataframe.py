# Imports
import pandas as pd
import os,io,datetime
import psycopg2 as pg
import dask.dataframe as dd

print('Started : ',datetime.datetime.now())
sitrds = pg.connect(host='10.248.150.213',
    port='5444',
    database='i200gut1',
    user='grip_own',
    password='changeme')
cursor = sitrds.cursor()
print("You are connected to SIT RDS atabase(User : grip_own)")

os.chdir("H:\Sprints\mifid\Temporary\BANCS_Identification")
filename='IDENTIFICATION_20210309.csv'
p_bsdate=20210109
p_bccentity='FCA'
seqnum=1


# This CSV doesn't have a header so pass
# column names as an argument
srccolumns = ["INSTRMNT_ID","OLD_SCRTY_ID","RANK","SEC_ID_SCHM","SEC_ID_SCHM_CD","SEC_NUM","ACTV_IND","STCK_EXCHNG","INIT_ENTITY","OWNER_ENTITY","EXEC_ENTITY","EXPRY_DT",
      "MKT_PLC_CD","MRK_PLC","SEC_NAME","EFCTV_DT","IDENTIFICATION_VER","DM_LSTUPDDT","DM_BTNUMBER","DM_BTID","DM_USERID","DM_WSID"
      ]
techcols = ["p_bsdate","p_bccentity","seqnum"]

target_column_list=["BID_INSTRMNT_ID","BID_OLD_SCRTY_ID","BID_RANK","BID_SEC_ID_SCHM","BID_SEC_ID_SCHM_CD","BID_SEC_NUM","BID_ACTV_IND","BID_STCK_EXCHNG","BID_INIT_ENTITY",
    "BID_OWNER_ENTITY","BID_EXEC_ENTITY","BID_EXPRY_DT","BID_MKT_PLC_CD","BID_MRK_PLC","BID_SEC_NAME","BID_EFCTV_DT","BID_IDENTIFICATION_VER","BID_DM_LSTUPDDT",
    "BID_DM_BTNUMBER","BID_DM_BTID","BID_DM_USERID","BID_DM_WSID","BID_BUSINESSDATE","bid_bccentity","BID_sequencenum"]

tgt_col_list=','.join(target_column_list)

print(tgt_col_list)

def parse_dates(df):
    return pd.to_datetime(df['time'], format = '%d-%b-%y')


def date_to_int(dfc):
    dfc=pd.to_datetime(dfc, format="%d-%b-%y",errors = 'coerce')
    dfc=dfc.dt.strftime('%Y%d%m')
    return dfc

# Create an iterable that will read "chunksize=1000" rows
# at a time from the CSV file
df=dd.read_csv(filename,sep='|',header=1,names=srccolumns,quotechar='"', dtype='str')
df.assign(bid_businessdate=p_bsdate,bid_bccentity=p_bccentity,bid_sequencenum=seqnum)
print(df.head(2))
df['EXPRY_DT']=dd.to_datetime(df.EXPRY_DT,unit='ns')
df['EFCTV_DT']=dd.to_datetime(df.EFCTV_DT,unit='ns')
df['DM_LSTUPDDT']=dd.to_datetime(df.DM_LSTUPDDT,unit='ns')
print(df['EFCTV_DT'].head(2))
    
output = io.StringIO() # For Python3 use StringIO
df['bid_businessdate']=p_bsdate
df['bid_bccentity']=p_bccentity
df['bid_sequencenum']=seqnum

df['EXPRY_DT']=date_to_int(df['EXPRY_DT'])
df['EFCTV_DT']=date_to_int(df['EFCTV_DT'])
df['DM_LSTUPDDT']=date_to_int(df['DM_LSTUPDDT'])

print(df['EXPRY_DT'])
print(df.head(10))
df.to_csv(output, sep='\t', header=True, index=False)
output.seek(0) # Required for rewinding the String object
print("----------")
copy_query = "COPY grip_own.tb_d_bancs_identification"+" ("+tgt_col_list+") "+" FROM STDOUT csv DELIMITER '\t' NULL ''  ESCAPE '\\' HEADER "
cursor.copy_expert(copy_query, output)
sitrds.commit()
print('Processed : ',datetime.datetime.now())

print('Finished : ',datetime.datetime.now())


