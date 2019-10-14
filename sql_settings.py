from sqlalchemy import create_engine
import pyodbc
import urllib
import os
import pyodbc
# import evn variables for DB connection 

# un = os.environ['DB_UN']
# up = os.environ['DB_UP']
conn_string = os.environ['CONN_STRING']

#conn="{ODBC Driver 13 for SQL Server};Server=tcp:resource1.database.windows.net,1433;Database=PqrUploadDeclarations;Uid=pqruploadapp@resource1;PWD=pqruploadazure1!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30 ;"

conn="Driver={ODBC Driver 13 for SQL Server};Server=tcp:resource1.database.windows.net,1433;Database=PqrUploadDeclarations;Uid=pqruploadapp@resource1;Pwd=pqruploadazure1!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"


params =urllib.parse.quote_plus(conn_string)


uri_azure_sql = "mssql+pyodbc:///?odbc_connect=%s" % params

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params) 


