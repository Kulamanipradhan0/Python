import  os

etl_repo_home="/opt/pentaho/repositories/grip-pentaho-di-reports/ETL/reports"
#Creating Base directory
mifid2_base_dir="mifid"

mifid2tr_dl_dirs=['mifid2-tr/mifid2-tr-etl-trade',
               'mifid2-tr/mifid2-tr-etl-correction',
               'mifid2-tr/mifid2-tr-etl-regulator-response',
               'mifid2-tr/mifid2-tr-etl-reference-data',
               'mifid2-tr/mifid2-tr-etl-automation']


mifid2cpr_dl_dirs=['mifid2-cpr\mifid2-cpr-etl-position',
                   'mifid2-cpr\mifid2-cpr-etl-correction',
                   'mifid2-cpr\mifid2-cpr-etl-regulator-response',
                   'mifid2-cpr\mifid2-cpr-etl-reference-data',
                   'mifid2-cpr\Mifid2-cpr-etl-automation']


try:
    os.chdir(etl_repo_home)
except:
    print("Not able to Change the directory to ETL repository Home")
    exit()

if os.path.isdir(mifid2_base_dir):
    os.chdir(mifid2_base_dir)
else:
    try:
        os.makedirs(mifid2_base_dir)
        os.chdir(mifid2_base_dir)
    except:
        print("Not able to Change the directory to ETL repository Home")
        exit()

for dirlist in mifid2tr_dl_dirs,mifid2cpr_dl_dirs:
    for dir in dirlist:
        if os.path.isdir(dir):
            print('Directory Already Exist : ',dir)
        else:
            os.makedirs(dir)


