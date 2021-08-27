import  os

etl_repo_home="/opt/pentaho/repositories/grip-pentaho-di-reports/ETL/reports"
#Creating Base directory
mifid2_base_dir="mifid"


mifid2tr_rg_dirs=['mifid2-tr\mifid2-tr-reports-trade',
                  'mifid2-tr\mifid2-tr-reports-correction',
                  'mifid2-tr\mifid2-tr-reports-automation']



mifid2cpr_rg_dirs=['mifid2-cpr\mifid2-cpr-reports-position',
                   'mifid2-cpr\mifid2-cpr-reports-correction',
                   'mifid2-cpr\Mifid2-cpr-reports-automation']

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

for dirlist in mifid2tr_rg_dirs,mifid2cpr_rg_dirs:
    for dir in dirlist:
        if os.path.isdir(dir):
            print('Directory Already Exist : ',dir)
        else:
            os.makedirs(dir)


