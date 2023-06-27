import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '192.168.1.32\LAB'
database = 'AdventureWorks2019'
username = 'python_user'
password = '12345'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server +
                      ';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

# Sample select query
cursor.execute("SELECT @@SERVERNAME+'\\'+@@SERVICENAME;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
