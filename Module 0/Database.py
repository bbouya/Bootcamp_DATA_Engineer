# Creation du Database dans posgresql:

import psycopg2
import pandas as pd

# Establising the connection:

conn = psycopg2.connect(detabse = 'postgres', user = 'postgres' ,password = '1234',host = '127.0.0.1' ,port = (5432))

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing a query to create a Database
sql = '''CREAT database appstore_games'''

# Creating a database name
cursor.execute(sql)
print("DataBase created successfully ...... ")

# Closing the connection
conn.close()
