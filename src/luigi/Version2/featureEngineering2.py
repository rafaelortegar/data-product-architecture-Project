import luigi
import logging
import psycopg2
import sqlalchemy

import pandas.io.sql as psql
import pandas as pd

from sqlalchemy import create_engine
from luigi.contrib.postgres import PostgresQuery, PostgresTarget

import feature_builder as fb
from loadCleaned import loadCleaned
from metadataCleaned import metadataCleaned
from metadataTestCleaned import metadataTestCleaned
import pickle

logger = logging.getLogger('luigi-interface')
##############################################################      SEMANTIC       ####################################

############################################################## FEATURE ENGINEERING ####################################

class featureEngineering2(PostgresQuery):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket. Requires extractToJson
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'feature_engineering_04_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3') # default='dpaprojs3')
    #==============================================================================================================
    # Parameters for database connection
    #==============================================================================================================
    creds = pd.read_csv("../../../credentials_postgres.csv")
    creds_aws = pd.read_csv("../../../credentials.csv")
    print('Credenciales leídas correctamente')
    host = creds.host[0]
    database = creds.db[0]
    user = creds.user[0]
    password = creds.password[0]
    table = 'cleaned.metro'
    port = creds.port[0]
    query = """SELECT * FROM cleaned.metro;"""
    #=============================================================================================================
    # Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return loadCleaned(bucket=self.bucket, date=self.date) # , metadataCleaned(bucket = self.bucket, date=  self.date)

    def _requires(self):
        return {'a': metadataTestCleaned(bucket=self.bucket,date=self.date), 'b': [metadataCleaned(bucket=self.bucket,date=self.date)]}

    def run(self):
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()
        sql = self.query

        logger.info('Executing query from task: {name}'.format(name=self.task_name))
        cursor.execute(sql)
        self.output().touch(connection)
        
        connection.commit()
        connection.close()
        ###################################################################
        creds=self.creds
        connection = psycopg2.connect(user=creds.user[0],
                                          password=creds.password[0],
                                          host=creds.host[0],
                                          port=creds.port[0],
                                          database=creds.db[0])
        cursor = connection.cursor()
        df = psql.read_sql('SELECT * FROM cleaned.metro;', connection)

        df2 = fb.FeatureBuilder()
        df2 = df2.featurize(df)
        print(df2.shape)

        model_matrix = fb.FeatureBuilder.create_model_matrix(df)
        
        #file = open('model_matrix.pkl', 'wb')
        #pickle.dump(model_matrix, file)
        #file.close()  
        
        #file = open('model_matrix.pkl', 'wb')
        #data = pickle.dump(model_matrix,file)
        #file.close()

        #with open('model_matrix.pkl', 'wb') as f:
        #    pickle.dump(model_matrix, f)

        engine = create_engine('postgresql+psycopg2://postgres:12345678@database-1.cqtrfcufxibu.us-west-2.rds.amazonaws.com:5432/dpa')
        print("ya pasó engine")
        table_name= 'metro'
        print(table_name)
        scheme='semantic'
        print(scheme)
        print("Esperame tantito, toy pensando...")
        df2.to_sql(table_name, con=engine,scheme='semantic' , if_exists='replace')
        print(psql.read_sql('SELECT * FROM semantic.metro LIMIT 10;', connection))

        print("head:")
        print(df2.head(10))
        print("tail:")
        print(df2.tail(10))
   

if __name__ == '__main__':
    luigi.featureEngineering2()


