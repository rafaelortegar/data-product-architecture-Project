import luigi
import pandas as pd
import boto3
import json
#import metadataExtract
#from luigi import extractToJson
#from luigi.Version2.metadataExtract import metadataExtract
#from luigi import extract
import psycopg2
from io import BytesIO
import pandas.io.sql as psql
from luigi.contrib.postgres import CopyToTable
from luigi.contrib.postgres import PostgresTarget

from modelingMetro2 import modelingMetro2


class metadataModeling(CopyToTable):
    """
    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'metadata_modelingMetro2_02_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
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
    table = 'raw.metro'
    columns = ["fecha_ejecucion", "fecha_json", "usuario", "ip_ec2", "nombre_bucket", "hiper_parámetros_modelo","error_de_modelado"]
    port = creds.port[0]
    #=============================================================================================================
#    def requires(self):
#        return {'a': metadataExtract(bucket=self.bucket,date=self.date), 'b': [metadataTestExtract(bucket=self.bucket,date=self.date)]}


    def requires(self):
        #def _requires(self):
        #    return metadataExtract(bucket=self.bucket,date=self.date)
        return modelingMetro2(bucket=self.bucket, date=self.date)# ,metadataExtract(bucket=self.bucket, date=self.date) # , metadataExtract(bucket=self.bucket, date=self.date) # , testExtract(bucket=self.bucket, date=self.date), metadataTestExtract(bucket=self.bucket, date=self.date)
        
            
    def rows(self):
        
        # Conectamos al bucket
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') # , region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3')
        obj = s3_resource.Bucket(self.bucket) # metemos el bucket S3 en una variable obj
        dev_s3_client = ses.client('s3')
        modelobuscado = "modelingMetro_task_06_01/metro_{}.pkl".format(self.date)
        print(modelobuscado)
        with BytesIO() as data:
            s3_resource.Bucket(self.bucket).download_fileobj(modelobuscado,data)
            data.seek(0)
            model = pickle.load(data)
        print("Voy a leer el pikle de la s3")
        print(model)
        
        
        with self.input().open('r') as json_file:
            data = json.load(json_file)
            filas_a_cargar = len(data['records'])
            print(filas_a_cargar)
            #seccion añadida despues de que ya corria
            creds2 = pd.read_csv("../../../credentials_postgres.csv")
            connection2 = psycopg2.connect(user=creds2.user[0],
                                      password=creds2.password[0],
                                      host=creds2.host[0],
                                      port=creds2.port[0],
                                      database=creds2.db[0])
            df = psql.read_sql('SELECT * FROM raw.metro;', connection2)
            filas_actuales=len(df)
            total_final = filas_a_cargar+filas_actuales
            data_info = {'datos_a_cargar': [filas_a_cargar], 'total_anterior':[filas_actuales], 'total_final':[total_final]}
            data_to_csv = pd.DataFrame(data=data_info)
            data_to_csv.to_csv('../../../columnas_leidas.csv')
            #fin de sección
            for line in data['records']:

                fecha_ingreso = line.get('fields').get('fecha')
                anio_ingreso = line.get('fields').get('anio')
                linea_ingreso = line.get('fields').get('linea')
                estacion_ingreso = line.get('fields').get('estacion')
                afluencia_ingreso = line.get('fields').get('afluencia')
                yield (fecha_ingreso,anio_ingreso,linea_ingreso,estacion_ingreso,afluencia_ingreso)
    
    
    def output(self):
        """
        Returns a PostgresTarget representing the inserted dataset.

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
    luigi.copyToPostgres()


