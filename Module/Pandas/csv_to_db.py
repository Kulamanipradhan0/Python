# Imports
import pandas as pd
import os,io,datetime
import psycopg2 as pg

print('Started : ',datetime.datetime.now())
sitrds = pg.connect(host='localhost',
                    port='5432',
                    database='postgres',
                    user='postgres',
                    password='password')
cursor = sitrds.cursor()
print("You are connected to database(User : postgres)")

os.chdir("")
filename=''
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




def date_to_int(dfc):
    dfc=pd.to_datetime(dfc, format="%d-%b-%y",errors = 'coerce')
    dfc=dfc.dt.strftime('%Y%d%m')
    return dfc

# Create an iterable that will read "chunksize=1000" rows
# at a time from the CSV file
for df in pd.read_csv(filename,sep='|',header=1,names=srccolumns,quotechar='"',chunksize=200000, dtype='unicode'):
    output = io.StringIO() # For Python3 use StringIO

    print(df.head(10))
    df.to_csv(output, sep='\t', header=True, index=False)
    output.seek(0) # Required for rewinding the String object
    print("----------")
    copy_query = "COPY stage_own.<table name>"+" ("+tgt_col_list+") "+" FROM STDOUT csv DELIMITER '\t' NULL ''  ESCAPE '\\' HEADER "
    cursor.copy_expert(copy_query, output)
    sitrds.commit()
    print('Processed : ',datetime.datetime.now())
print('Finished : ',datetime.datetime.now())


