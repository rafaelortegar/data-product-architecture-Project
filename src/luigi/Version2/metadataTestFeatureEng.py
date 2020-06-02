import luigi
import json
import boto3
import logging
import psycopg2
import pandas as pd

import pandas.io.sql as psql
import pandas as pd

from sqlalchemy import create_engine

from luigi.contrib.postgres import PostgresQuery, PostgresTarget

from testFeatureEngineering import testFeatureEngineering

logger = logging.getLogger('luigi-interface')

class metadataTestFeatureEng(PostgresQuery):
    """
    Function to load metadata from the loading process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket. Requires extractToJson
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'metadata_test_featureEng_05_02'
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
    table = 'test.metapruebasunit'
    port = creds.port[0]
    query = """INSERT INTO test.metapruebasunit("usuario","fecha_de_ejecucion","resultado","nombre_de_prueba","ip_ec2") VALUES(%s,%s,%s,%s,%s);"""
    #=============================================================================================================
    
    # Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return testFeatureEngineering(bucket=self.bucket, date=self.date) # , metadataCleaned(bucket = self.bucket, date=  self.date)
    
    def run(self):
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()
        
        clientEC2 = boto3.client('ec2')
        information_metadata_ours = clientEC2.describe_instances()
        #fecha_ejecucion = pd.Timestamp.now()
        fecha_json = self.date
        
        df = psql.read_sql("""SELECT * FROM semantic.metatestfeature ORDER BY time DESC LIMIT 1;""", connection) # debería ser la tabla anterior
        estatus = df['result'][0]
        fecha_ejecucion = df['time'][0]
        nombre_de_la_prueba = df['nombreprueba'][0]
        usuario = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('KeyName')
        ip_ec2 = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('PrivateIpAddress')
        
        #datos_a_insertar = {'usuario':[usuario],'fecha_de_ejecucion':[fecha_ejecucion],'resultado':[estatus],
        #                    'nombre_de_prueba':[nombre_de_la_prueba],'ip_ec2':[ip_ec2]}
        
        #df_a_subir = pd.DataFrame(data=datos_a_insertar)
        
        #engine = create_engine('postgresql+psycopg2://postgres:12345678@database-1.cqtrfcufxibu.us-west-2.rds.amazonaws.com:5432/dpa')
        #. \
        #    format(self.user,self.password, self.host, self.port,self.database)
            
        #table_name= self.table
        #scheme='raw'
        #df_a_subir.to_sql("raw.test", con=engine, schema='raw',if_exists='replace')
        #print(psql.read_sql('SELECT * FROM raw.metatestload ORDER BY time DESC LIMIT 1;', connection))
        sql = self.query
        logger.info('Executing query from task: {name}'.format(name=self.task_name))
        cursor.execute(sql,(usuario,fecha_ejecucion,estatus,nombre_de_la_prueba,ip_ec2))
        self.output().touch(connection)


        # commit and close connection
        connection.commit()
        #cursor.close()
        connection.close()
        
        
    def output(self):
        """
        Returns a PostgresTarget representing the executed query.

        Normally you don't override this.
        """
        return PostgresTarget(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            table=self.table,
            update_id=self.update_id,
            port=self.port
        )

if __name__ == '__main__':
    luigi.metadataTestFeatureEng()
