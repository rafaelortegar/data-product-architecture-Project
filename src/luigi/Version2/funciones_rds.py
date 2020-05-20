import os
import psycopg2
import sqlalchemy
import pandas as pd
import pandas.io.sql as psql
from sqlalchemy import create_engine

class conectaAtablaRawMetro(object):
    
    def __init__(self,host,database,user,password,table,port):
        creds = pd.read_csv("../../../credentials_postgres.csv")
        self.host = creds.host[0]
        self.database = creds.database[0]
        self.user = creds.user[0]
        self.password = creds.password[0]
        self.table = 'raw.metro' 
        self.port = creds.port[0]
        
        
    def dbaspandas(self):
        connection = psycopg2.connect(user=self.user,
                              password=self.password,
                              host=self.host,
                              port=self.port,
                              database=self.database)
        cursor = connection.cursor()
        
        df = psql.read_sql('SELECT * FROM raw.metro;', connection)
        # close connection
        cursor.close()
        connection.close()
        return len(df)
        
    
class conectaAtablaCleanedMetro(object):
    
    def __init__(self,host,database,user,password,table,port):
        creds = pd.read_csv("../../../credentials_postgres.csv")
        self.host = creds.host[0]
        self.database = creds.database[0]
        self.user = creds.user[0]
        self.password = creds.password[0]
        self.table = 'cleaned.metro' 
        self.port = creds.port[0]
        
        
    def dbaspandas(self):
        creds = pd.read_csv("../../../credentials_postgres.csv")
        connection = psycopg2.connect(user=creds.user[0],
                              password=creds.password[0],
                              host=creds.host[0],
                              port=creds.port[0],
                              database=creds.database[0])        
        
        
        
        #connection = psycopg2.connect(user=self.user,
        #                      password=self.password,
        #                      host=self.host,
        #                      port=self.port,
        #                      database=self.database)
        cursor = connection.cursor()
        
        df = psql.read_sql('SELECT * FROM cleaned.metro;', connection)
        # close connection
        cursor.close()
        connection.close()
        return df
    
    
    