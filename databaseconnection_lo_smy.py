"""
This will connect to the oracle database and create a dataframe and write the results to a csv file

"""
import oracledb
import csv
import pandas as pd
import pathlib
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("NewDusty")

def runquery():

    connection = oracledb.connect(
            user="penta",
            password="prodhf_7yrgd",
            dsn="PROD")

    print("Successfully connected to Oracle Database")

    cursor = connection.cursor()
    cursor.execute("select reg_hrs,th_hrs,dt_hrs, emp_id, job_id, work_date, cc from lo_smy where work_date >= '2023/07/01' and work_date <='2024/06/30' and emp_id = 3020")
    rows = cursor.fetchall()
  

    df=pd.DataFrame(rows)


    
    df.rename(columns={0:'REG_HRS',1:'TH_HRS',2:'DT_HRS',3:'EMP_ID',4:'JOB_ID', 5:'WORK_DATE', 6:'CC'}, inplace=True)



    file_path: pathlib.Path = DATA_DIR.joinpath("lo_smy_data_3020.csv")
    df.to_csv(file_path, index=False)
    


    connection.close()
    


   

runquery()

