import pandas as pd

chunksize=10**4

for df in pd.read_csv('H:\Sprints\mifid\Temporary\REUPRD_20210709_FCA_MICS_P01_20210710042221.csv',sep=',',chunksize=chunksize, low_memory=False):
    df['dummy']=8
print(df.head(5))
