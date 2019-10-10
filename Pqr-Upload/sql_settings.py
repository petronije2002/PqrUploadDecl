from sqlalchemy import create_engine
import pyodbc
import urllib
import os
import pyodbc
# import evn variables for DB connection 

un = os.environ['DB_UN']
up = os.environ['DB_UP']


# working example: Driver={ODBC Driver 17 for SQL Server};Server=tcp:resource1.database.windows.net,1433;Database=resource;Uid=pera@resource1;PWD=Petronijevicazure1!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
conn_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:resource1.database.windows.net,1433;Database=PqrUploadDeclarations;Uid=pqruploadapp@resource1;PWD=pqruploadazure1!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"


# conn_string = "Driver={{ODBC Driver 13 for SQL Server}};Server=tcp:resource1.database.windows.net,1433;Database=PqrUploadDeclarations;Uid={{{}}}@resource1;Pwd={{{}}};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(un,up)
# conn_string = "Driver={ODBC Driver 13 for SQL Server};" + "Server=tcp:resource1.database.windows.net,1433;Database=PqrUploadDeclarations;Uid={{{}}}@resource1;Pwd={{{}}};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(un,up)
params =urllib.parse.quote_plus(conn_string)


uri_azure_sql = "mssql+pyodbc:///?odbc_connect=%s" % params
# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params,pool_size=10, max_overflow=20) 


