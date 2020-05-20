import luigi
import json
import boto3
import psycopg2
import pandas as pd

from luigi.contrib.postgres import CopyToTable
from ExtractTestCase1 import ExtractTestCase
from extract import extractToJson

class testExtract(CopyToTable):
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'test_extract_task_01_03'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================
    # Parameters for database connection
    #==============================================================================================================
    creds = pd.read_csv("../../../credentials_postgres.csv")
    creds_aws = pd.read_csv("../../../credentials.csv")
    print('Credenciales leídas correctamente test_extract')
    host = creds.host[0]
    database = creds.db[0]
    user = creds.user[0]
    password = creds.password[0]
    table = 'raw.metatestextract'
    columns = ["result", "time", "nombreprueba"] 
    port = creds.port[0]
    query = """SELECT * FROM raw.metatestextract"""
    #=============================================================================================================
    
    def requires(self):
        return extractToJson(bucket = self.bucket, date = self.date)

    def rows(self):
        
        with self.input().open('r') as json_file:
            data = json.load(json_file)
            #print("imprimiendo data")
            #print(data)
            columns_read = data['nhits']
            print(columns_read)
            status = 'Loaded'
            #datasetid = data['records'][0].get('datasetid')

            prueba = ExtractTestCase()
            #prueba.json_file= json_file  # file_content
            #prueba.pd_json= pd_json
            prueba.json_file = data
            print(prueba)
            #prueba.setUp()
            data_f = prueba.test_extract()
            df1= pd.DataFrame(data_f)
            print(df1)
            result = df1['estatus'][0]
            time = df1['hora_ejecucion'][0]
            nombreprueba = df1['prueba'][0]
            yield (result,time,nombreprueba)

if __name__ == '__main__':
    luigi.testExtract()



#      def run(self):
#       
#       
#        
#        
#        
#        # Los archivos que se usan por el pipeline
#        print("Inicia la extracción de los datos cargados en la S3 para cargarlos a postgres...")
#        file_to_read = 'metadataExtract_task_02_02/metro_' + self.date + '.json'
#        #archivoquenosirve = 'createTables_task_02_01/metro_' + self.date + '.csv'
#        print("El archivo a leer es: ",file_to_read)
#        
#        # Leyendo credenciales
#        creds = pd.read_csv("../../credentials_postgres.csv")
#        creds_aws = pd.read_csv("../../credentials.csv")
#        print("credenciales leídas correctamente")
#
#        # Conexión a la S3
#        print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
#        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
#        s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
#        dev_s3_client = ses.client('s3')
#        obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
#        print("Conexión Exitosa! :)")
#
#        #archivoquenosirve_object = s3_resource.Object(self.bucket, archivoquenosirve)
#        content_object = s3_resource.Object(self.bucket, file_to_read)
#        file_content = content_object.get()['Body'].read().decode('utf-8')
#        json_content = json.loads(file_content)
#        
#            
#        with open('contenido.json', 'w') as outfile:
#            json.dump(file_content, outfile)
#
#        file = 'contenido.json'
#        json_file = open(file, 'r')
#
#        #pd_json = pd.read_json(file)
#        #pd_json.shape[0] == 0
#        
#        prueba = ExtractTestCase()
#        #prueba.json_file= json_file  # file_content
#        #prueba.pd_json= pd_json
#        prueba.json_file = json_file
#        #prueba.setUp()
#        prueba.test_extract()
#
#        print("Archivo cargado correctamente...")
#        # para los outputs que no vamos a usar
#        vacio = ' '
#        data_vacia = {'vacio':[vacio]}
#        pandas_a_csv = pd.DataFrame(data=data_vacia)
#        pandas_a_csv.to_csv(self.output().path, index=False)
#        print("archivo creado correctamente")
#
#    def output(self):
#        output_path = "s3://{}/{}/metro_{}.csv". \
#            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
#        return luigi.contrib.s3.S3Target(path=output_path)