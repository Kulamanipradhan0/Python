import  os
import shutil

etl_repo_home="H:\PycharmProjects\PyTraining\Lessons\Module\Os\TestingOSModule"
#Creating Base directory
mifid2_base_dir="mifid"

mifid2tr_dl_dirs=['mifid2-tr/mifid2-tr-etl-trade',
               'mifid2-tr/mifid2-tr-etl-correction',
               'mifid2-tr/mifid2-tr-etl-regulator-response',
               'mifid2-tr/mifid2-tr-etl-reference-data',
               'mifid2-tr/mifid2-tr-etl-automation']

mifid2tr_rg_dirs=['mifid2-tr\mifid2-tr-reports-trade',
                  'mifid2-tr\mifid2-tr-reports-correction',
                  'mifid2-tr\mifid2-tr-reports-automation']

mifid2cpr_dl_dirs=['mifid2-cpr\mifid2-cpr-etl-position',
                   'mifid2-cpr\mifid2-cpr-etl-correction',
                   'mifid2-cpr\mifid2-cpr-etl-regulator-response',
                   'mifid2-cpr\mifid2-cpr-etl-reference-data',
                   'mifid2-cpr\Mifid2-cpr-etl-automation']

mifid2cpr_rg_dirs=['mifid2-cpr\mifid2-cpr-reports-position',
                   'mifid2-cpr\mifid2-cpr-reports-correction',
                   'mifid2-cpr\Mifid2-cpr-reports-automation']

try:
    os.chdir(etl_repo_home)
except:
    print("Not able to Change the directory to ETL repository Home")
    exit()

if os.path.isdir(mifid2_base_dir):
    shutil.rmtree(mifid2_base_dir)
try:
    os.makedirs(mifid2_base_dir)
    os.chdir(mifid2_base_dir)
except:
    print("Not able to Create base directory 'mifid' in ETL repository Home")
    exit()

for dirlist in mifid2tr_dl_dirs,mifid2tr_rg_dirs,mifid2cpr_dl_dirs,mifid2cpr_rg_dirs:
    for dir in dirlist:
        if os.path.isdir(dir):
            shutil.rmtree(dir)

for dirlist in mifid2tr_dl_dirs,mifid2tr_rg_dirs,mifid2cpr_dl_dirs,mifid2cpr_rg_dirs:
    for dir in dirlist:
        os.makedirs(dir)


