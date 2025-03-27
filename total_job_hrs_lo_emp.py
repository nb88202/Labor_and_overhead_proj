
import pathlib
import sys
import pandas as pd


PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("NewDusty")
file_path: pathlib.Path = DATA_DIR.joinpath("lo_smy_data_3020.csv")


     
df= pd.read_csv(file_path) 
df_no=df.fillna('X')
df_no2=df_no[df_no['JOB_ID']=='X']
#print(df_no2)
df_reg=df_no2[['REG_HRS','JOB_ID', 'WORK_DATE', 'CC']]
df_th=df_no2[['TH_HRS','JOB_ID', 'WORK_DATE', 'CC']]
df_dt=df_no2[['DT_HRS','JOB_ID', 'WORK_DATE', 'CC']]

df_reg2=df_reg[df_reg['REG_HRS']>0]
df_th2=df_th[df_th['TH_HRS']>0]

df_new = pd.concat([df_reg2,df_th2])

df_sorted=df_new.sort_values(by=['CC','WORK_DATE'])

print(df_sorted[0:40])


file_path: pathlib.Path = DATA_DIR.joinpath("results_3020_nojob.xlsx")
df_sorted.to_excel(file_path, index=False)



"""

df_new=df_lo[df_lo['EMP_ID']==3020]

#df_new_4=df_new[df_new['JOB_ID']=='22-019S']

df_new_v=df_new[df_new['REG_HRS']>0]
df_new_b=df_new_v[['EMP_ID','REG_HRS','JOB_ID','WORK_DATE']]
df_new_bb=df_new_b[df_new_b['JOB_ID']=='22-019S']
#print(df_new_bb)




#for one employee

df_X=df_lo[['EMP_ID', 'REG_HRS']]
df_X2=df_X.groupby('EMP_ID')['REG_HRS'].sum()
df_X3=df_X2.reset_index()
df_x4=df_X3[df_X3==3020]
dfx5=df_x4.dropna()
#print(df_X3[80:120])

# this will get the REG_HRS for all jobs
df4=df_lo2.drop('JOB_ID', axis=1)
df5=df4.drop('DT_HRS', axis=1)
df6=df5.drop('TH_HRS', axis=1)

df7=df6.groupby('EMP_ID')['REG_HRS'].sum()
df_8=df7.reset_index()

df9=df_8[df_8>0]
df10=df9.dropna()
print(df10[0:40])

#this will get the TH_HRS for all jobs

df44=df_lo2.drop('JOB_ID', axis=1)
df54=df44.drop('REG_HRS', axis=1)
df64=df54.drop('DT_HRS', axis=1)
df65=df64.dropna()

df75=df65.groupby('EMP_ID')['TH_HRS'].sum()
df77=df75
df78=df77.reset_index()
#print(df78[0:40])

#this will get the DT_HRS for all jobs

df444=df_lo2.drop('JOB_ID', axis=1)
df544=df444.drop('REG_HRS', axis=1)
df644=df544.drop('TH_HRS', axis=1)
df654=df644.dropna()
df6768=df654[df654['DT_HRS']>0]
df_h=df6768.dropna()

df_h2=df_h.groupby('EMP_ID')['DT_HRS'].sum()
df_h3=df_h2.reset_index()

#print(df_h3[0:40])





df2=pd.merge(df_emp,df_tc_base,how='left', on='EMP_ID')

df3=df2

df4=df3.drop('JOB_ID', axis=1)
df5=df4.groupby('EMP_ID')['HRS'].sum()
df_total=df5.reset_index()
df_total_hrs=df_total[df_total > 0]
df_total_hrs=df_total_hrs.dropna()

#print(df_total_hrs)




df_new=pd.merge(df_tc_base,df_jobs,how='left',on='JOB_ID')
df_3 = df_new.dropna()

df4=pd.merge(df_emp,df_3,how='left', on='EMP_ID')
df5=df4.dropna()

df6=df5.drop('JOB_ID', axis=1)
df7=df6.drop('ST_CD', axis=1)

df8=df7.groupby('EMP_ID')['HRS'].sum()

df_dc_hours=df8.reset_index()

#file_path: pathlib.Path = DATA_DIR.joinpath("results.csv")
#df8.to_excel(file_path, index=False)


"""