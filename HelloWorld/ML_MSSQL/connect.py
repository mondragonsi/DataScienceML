#write a program that can connect to a MSSQL instance and execute a query
#and plot the results using plotly

import pyodbc
import plotly.express as px
import pandas as pd

# Connect to the database
conn = pyodbc.connect('Driver={SQL Server};')
cursor = conn.cursor()

# Execute the query

cursor.execute("SELECT * FROM [AdventureWorks2019].[Sales].[SalesOrderDetail]")

# Get the results


