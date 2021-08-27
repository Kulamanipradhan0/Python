import pandas as pd
from sqlalchemy import create_engine
import psycopg2, os
import io, datetime, sys, numpy as np
import threading, time,subprocess

p_bsdate = 20210301
p_bccentity = 'FCA'

starttime = datetime.datetime.now()
print('Processed : ', starttime)
print("----------")
#
db_engine = create_engine('postgresql+psycopg2://postgres:password@locahost:5432/postgres')

# Creating cursor and connection for required databases
db_engine_conn = db_engine.raw_connection()

print(df_metadata[['dbtype', 'cursor', 'schema_name']])
# Constructing complete filter condition
bsdate_cond = df_metadata['bsdate_col_name'] + " = " + str(p_bsdate)
df_metadata['bsdate_cond'] = np.where(pd.isnull(df_metadata['bsdate_col_name']) == True, '1=1', bsdate_cond)

activeind_cond = ' and ' + df_metadata['activeind_col_name'] + " = 'Y'"
df_metadata['activeind_cond'] = np.where(pd.isnull(df_metadata['activeind_col_name']) == True, '', activeind_cond)

# End of Constructing complete filter condition

def pg_copy_to(copy_sql, cursor, conn, output_filename, i):
    print('Process Started for : ', df_metadata['table_name'][i], datetime.datetime.now())
    subprocess.call(['pgsql\\bin\\psql', '-h','localhost','-p','5432','-U','postgres','-v', 'ON_ERROR_STOP=1', \
                     '-qAtX', '-c', '\copy ('+copy_sql+') \
                 to '+output_filename+" WITH DELIMITER ';' CSV HEADER",'postgres'])
    print('Process Completed for : ', df_metadata['table_name'][i], datetime.datetime.now())


print(len(df_metadata))

if __name__ == "__main__":
    threads = list()
    for i in range(len(df_metadata)):
        os.chdir('')
        output_filename = df_metadata['table_name'][i] + '_' + str(p_bsdate)+'.csv'
        # if df_metadata['schema_name'][i]=='grip_own':
        #     x=threading.Thread(target=pg_copy_to, args=(copy_to_sql,rds_grip_cursor,rds_grip_conn,output,i))
        #     threads.append(x)
        #     x.start()

        if df_metadata['schema_name'][i] == 'stage_own':
            x = threading.Thread(target=pg_copy_to, args=(df_metadata['select_sql'][i], output_filename, i))
            threads.append(x)
            x.start()
        if df_metadata['schema_name'][i] == 'dwh_own':
            x = threading.Thread(target=pg_copy_to, args=(df_metadata['select_sql'][i], output_filename, i))
            threads.append(x)
            x.start()
    for index, thread in enumerate(threads):
        thread.join()
