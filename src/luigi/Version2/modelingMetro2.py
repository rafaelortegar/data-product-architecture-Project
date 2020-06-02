import luigi
import logging
import psycopg2
import sqlalchemy
import pickle
import boto3

import pandas.io.sql as psql
import pandas as pd

from sqlalchemy import create_engine
from luigi.contrib.s3 import S3Target

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

from featureEngineering2 import featureEngineering2
from metadataFeatureEngineering import metadataFeatureEngineering
from metadataTestFeatureEng import metadataTestFeatureEng
import modelado

logger = logging.getLogger('luigi-interface')


class modelingMetro2(luigi.Task):
    """
    Function to train model from the mexico city metro data set on the database on postgres.
    It stores the metadata from uploading into the specified S3 bucket on AWS. Note: user MUST have the credentials 
    to use the aws s3 bucket.
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'modelingMetro_task_06_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3') # default='dpaprojs3')
    #==============================================================================================================
    
    # Indica que para iniciar loadCleaned proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return featureEngineering2(bucket=self.bucket, date=self.date) # , metadataCleaned(bucket = self.bucket, date=  self.date)

    def _requires(self):
        return {'a': metadataTestFeatureEng(bucket=self.bucket,date=self.date), 'b': [metadataFeatureEngineering(bucket=self.bucket,date=self.date)]}

    def run(self):
        creds = pd.read_csv("../../../credentials_postgres.csv")
        creds_aws = pd.read_csv("../../../credentials.csv")
        
        # Conectamos al bucket
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') # , region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3')
        obj = s3_resource.Bucket(self.bucket) # metemos el bucket S3 en una variable obj
        
        # conectamos a la RDS
        connection = psycopg2.connect(user=creds.user[0],
                                  password=creds.password[0],
                                  host=creds.host[0],
                                  port=creds.port[0],
                                  database=creds.db[0])
        
        cursor = connection.cursor()
        
        # Leemos los datos de la RDS
        df = psql.read_sql('SELECT * FROM semantic.metro;', connection)
        print(df.shape) 
        
        # Hacemos el modelado
        modelos = modelado.ModelBuilder()
        print("modelos...",modelos)
        print("aqui ya hizo model builder")
        modelos = modelos.build_model(df)
        
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Modelado completado!! :)")
        
#        # Escribe un JSON con la información descargada de la API, aqui esta el output
#        with self.output().open('w') as picklemodelo:
#            pickle.dump(modelos,file)
#        file = self.output().open('wb')
#        pickle.dump(modelos, file)
#        file.close()
#        
        with self.output().open('w') as output_path:
            pickle.dump(modelos,output_path)
        
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Modelado completado!! :)")
        #connection = self.output().connect()
        #connection.autocommit = self.autocommit
        #cursor = connection.cursor()
        #sql = self.query
        
        ########################################################################        
        # commit and close connection
        cursor.close()
        connection.commit()
        connection.close()
        
    # Envía el output al S3 cop especificado con el nombre de output_path
    def output(self):
        output_path = "s3://dpaprojs3/modelingMetro_task_06_01/metro_{}.pkl".format(self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path, format=luigi.format.Nop)




if __name__ == '__main__':
    luigi.modelingMetro2()
