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
rds_grip_engine = create_engine('postgresql+psycopg2://grip_own:changeme@10.248.150.213:5444/i200gut1')
rdm_emir_engine = create_engine('postgresql+psycopg2://emir_usr:db533645fc7dfeffe578abdc7cb6423c@localhost:5100/i204rdt1')
# rdm_emir_engine = create_engine('postgresql+psycopg2://n75059:BD2jNpdP@10.248.1.221:5468/e203rdp1')
# rdm_mifid_engine = create_engine('postgresql+psycopg2://n75059:BD2jNpdP@10.248.1.221:5468/e203rdp1')
rdm_mifid_engine = create_engine('postgresql+psycopg2://mifid_own:pAoHF11r>)Fr@10.248.0.116:5462/i204rdt1')
rdm_sit_mifid_engine = create_engine('postgresql+psycopg2://mifid_own:pAoHF11r>)Fr@10.248.0.116:5462/i204rdt1')

# Creating cursor and connection for required databases
rdm_mifid_conn = rdm_mifid_engine.raw_connection()
rdm_mifid_cursor = rdm_mifid_conn.cursor()

# rds_grip_conn = rds_grip_engine.raw_connection()
# rds_grip_cursor=rds_grip_conn.cursor()

rdm_emir_conn = rdm_emir_engine.raw_connection()
rdm_emir_cursor = rdm_emir_conn.cursor()

get_table_list = "SELECT * FROM mifid_own.tb_datadump_config WHERE active_ind='Y' and dbtype='RDM'"
df_metadata = pd.read_sql_query(get_table_list, rdm_sit_mifid_engine)

df_metadata['cursor'] = np.where(df_metadata['dbtype'].eq('RDS'), 'rds_grip_cursor',
                                 np.where(df_metadata['schema_name'].eq('mifid_own'), 'rdm_mifid_cursor',
                                          'rdm_emir_cursor'))
df_metadata['conn'] = np.where(df_metadata['dbtype'].eq('RDS'), 'rds_grip_conn',
                               np.where(df_metadata['schema_name'].eq('mifid_own'), 'rdm_mifid_conn', 'rdm_emir_conn'))

print(df_metadata[['dbtype', 'cursor', 'schema_name']])
# Constructing complete filter condition
bsdate_cond = df_metadata['bsdate_col_name'] + " = " + str(p_bsdate)
df_metadata['bsdate_cond'] = np.where(pd.isnull(df_metadata['bsdate_col_name']) == True, '1=1', bsdate_cond)

activeind_cond = ' and ' + df_metadata['activeind_col_name'] + " = 'Y'"
df_metadata['activeind_cond'] = np.where(pd.isnull(df_metadata['activeind_col_name']) == True, '', activeind_cond)

bccentity_cond = ' and ' + df_metadata['bccentity_col_name'] + " = '" + p_bccentity + "'"
df_metadata['bccentity_cond'] = np.where(pd.isnull(df_metadata['bccentity_col_name']) == True, '', bccentity_cond)

df_metadata['select_sql'] = 'select * from ' + df_metadata['schema_name'] + '.' + df_metadata['table_name'] + ' ' \
                            + 'where ' + df_metadata['bsdate_cond'] + df_metadata['bccentity_cond'] + df_metadata[
                                'activeind_cond']


# End of Constructing complete filter condition

def pg_copy_to(copy_sql, cursor, conn, output_filename, i):
    print('Process Started for : ', df_metadata['table_name'][i], datetime.datetime.now())
    subprocess.call(['H:\\Softwares\\pgadmin1.22.1\\pgsql\\bin\\psql', '-h','10.248.1.221','-p','5468','-U','n75059','-v', 'ON_ERROR_STOP=1', \
                     '-qAtX', '-c', '\copy ('+copy_sql+') \
                 to '+output_filename+" WITH DELIMITER ';' CSV HEADER",'e203rdp1'])
    print('Process Completed for : ', df_metadata['table_name'][i], datetime.datetime.now())


print(len(df_metadata))

if __name__ == "__main__":
    threads = list()
    for i in range(len(df_metadata)):
        os.chdir('H:\Sprints\mifid\Temporary\BANCS_Identification')
        output_filename = df_metadata['table_name'][i] + '_' + str(p_bsdate)+'.csv'
        # if df_metadata['schema_name'][i]=='grip_own':
        #     x=threading.Thread(target=pg_copy_to, args=(copy_to_sql,rds_grip_cursor,rds_grip_conn,output,i))
        #     threads.append(x)
        #     x.start()

        if df_metadata['schema_name'][i] == 'core_own':
            x = threading.Thread(target=pg_copy_to, args=(df_metadata['select_sql'][i], rdm_emir_cursor, rdm_emir_conn, output_filename, i))
            threads.append(x)
            x.start()
        if df_metadata['schema_name'][i] == 'mifid_own':
            x = threading.Thread(target=pg_copy_to, args=(df_metadata['select_sql'][i], rdm_mifid_cursor, rdm_mifid_conn, output_filename, i))
            threads.append(x)
            x.start()
    for index, thread in enumerate(threads):
        thread.join()
