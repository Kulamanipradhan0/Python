# Imports
import pandas as pd
import os,io
import psycopg2 as pg

sitrds = pg.connect(host='10.248.150.213',
                     port='5444',
                     database='i200gut1',
                     user='grip_own',
                     password='changeme')
cursor = sitrds.cursor()
print("You are connected to SIT RDS atabase(User : grip_own)")

os.chdir("H:\Sprints\mifid\\3. Sprint Changes\RERE_9144 ShortSellExemptLoadtoRDS")
filename='ESMAShortSellExemptionOutput_20210107.csv'
p_bsdate=20210109
p_bccentity='FCA'
seqnum=1

# This CSV doesn't have a header so pass
# column names as an argument
srccolumns = [
    "shs_relevantAuthority",
    "shs_isin",
    "shs_name",
    "shs_status",
    "shs_countryCode",
    "shs_modificationDate",
    "shs_modificationBDate",
    "shs_exemptionStartDate",
    "root",
    "id",
    "timestamp",
    "version"
]
techcols = ["p_bsdate","p_bccentity","seqnum"]

target_column_list=["es_relevantauthority","es_isin","es_name","es_status","es_countrycode","es_modificationdate","es_modificationbdate","es_exemptionstartdate","es_root","es_id","es_timestamp","es_version","es_businessdate","es_bccentity","es_sequencenum"]

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

    df['shs_modificationDate']=time_to_int(df['shs_modificationDate'])
    df['shs_modificationBDate']=time_to_int(df['shs_modificationBDate'])
    df['shs_exemptionStartDate']=time_to_int(df['shs_exemptionStartDate'])

    print(df['shs_exemptionStartDate'])
    print(df.head(10))
    df.to_csv(output, sep='\t', header=True, index=False)
    output.seek(0) # Required for rewinding the String object
    print("----------")
    copy_query = "COPY grip_own.tb_d_esma_exempted_share"+" ("+tgt_col_list+") "+" FROM STDOUT csv DELIMITER '\t' NULL ''  ESCAPE '\\' HEADER "
    cursor.copy_expert(copy_query, output)
    sitrds.commit()
