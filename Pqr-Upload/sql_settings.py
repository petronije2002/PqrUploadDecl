from sqlalchemy import create_engine
import pyodbc
import urllib
import os
import pyodbc
# import evn variables for DB connection 

un = os.environ['DB_UN']
up = os.environ['DB_UP']
conn_string = os.environ['CONN_STRING']


params =urllib.parse.quote_plus(conn_string)


uri_azure_sql = "mssql+pyodbc:///?odbc_connect=%s" % params
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params,pool_size=10, max_overflow=20) 


