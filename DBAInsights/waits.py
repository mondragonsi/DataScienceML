import pyodbc
import pandas as pd
import numpy as np
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '192.168.1.30'
database = 'master'
username = 'dba'
password = '12345'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify
# ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server +
                      ';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

# Sample select query and set result to pandas dataframe
df = pd.read_sql_query(
    "SELECT session_id,wait_duration_ms,wait_type FROM sys.dm_os_waiting_tasks order by wait_duration_ms desc;", cnxn)
print(df)
print(df.describe())
print(df.info())
print(df.dtypes)

cnxn.close()
