import luigi
import pandas as pd
import boto3
import json
#import metadataExtract
#from luigi import extractToJson
#from luigi.Version2.metadataExtract import metadataExtract
#from luigi import extract
import psycopg2
from luigi.contrib.postgres import CopyToTable

from extract import extractToJson
class copyToPostgres(CopyToTable):
    """
    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'load_task_03_01'
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
    columns = [("Fecha","TEXT"),("Ano","TEXT"),("Linea", "TEXT"),("Estacion", "TEXT"),("Afluencia""TEXT")]
    port = creds.port[0]
    #=============================================================================================================

    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date) #, metadataExtract(bucket=self.bucket, date=self.date), testExtract(bucket=self.bucket, date=self.date), metadataTestExtract(bucket=self.bucket, date=self.date)

    def rows(self):
        with self.input().open('r') as json_file:
            data = json.load(json_file)
            for line in data['records']:
#                ingresar = {'fecha':[data['records'][line].get('fields').get('fecha')],'anio':[data['records'][line].get('fields').get('anio')],
#                            'linea':[data['records'][line].get('fields').get('linea')],'estacion':[data['records'][line].get('fields').get('estacion')],
#                            'afluencia':[data['records'][line].get('fields').get('afluencia')]}
#                tupla_ingresar = (data['records'][line].get('fields').get('fecha'),data['records'][line].get('fields').get('anio'),
#                                  data['records'][line].get('fields').get('linea'),data['records'][line].get('fields').get('estacion'),
#                                  data['records'][line].get('fields').get('afluencia'))
                #fecha_ingreso = data['records'][line].get('fields').get('fecha')
                fecha_ingreso = line.get('fields').get('Fecha')
                anio_ingreso = line.get('fields').get('anio')
                linea_ingreso = line.get('fields').get('linea')
                estacion_ingreso = line.get('fields').get('estacion')
                afluencia_ingreso = line.get('fields').get('afluencia')
#                anio_ingreso = data['records'][line].get('fields').get('anio')
#                linea_ingreso = data['records'][line].get('fields').get('linea')
#                estacion_ingreso = data['records'][line].get('fields').get('estacion')
#                afluencia_ingreso = data['records'][line].get('fields').get('afluencia')
                yield (fecha_ingreso,anio_ingreso,linea_ingreso,estacion_ingreso,afluencia_ingreso)
#                yield line.strip('\n').split('\t')
        
#        with open('metro_2019-01-01.json') as json_file: 
#            data = json.load(json_file)
#            data['records'][0].get('fields')
#            len(data['records'])

#data['records'][line].get('fields').get('fecha')
#>>> data['records'][0]
#{'datasetid': 'afluencia-diaria-del-metro-cdmx', 'recordid': 'ec33a8dcf83dba40ce9b09e1f51f67acefe1a0ef', 'fields': {'anio': '2019',
#  'estacion': 'Pantitlán', 'fecha': '2019-01-01', 'linea': 'Linea 1', 'afluencia': '14452'}, 'record_timestamp': '2020-03-25T17:13:11.354000+00:00'}


#    def run(self):
#
#        # Los archivos que se usan por el pipeline
#        print("Inicia la extracción de los datos cargados en la S3 para cargarlos a postgres...")
#        file_to_read = 'test_extract_metadata_01_04/metro_' + self.date + '.json'
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
#        print("Archivo cargado correctamente...")
#
#        df = pd.DataFrame(columns=["fecha", "anio", "linea", "estacion", "afluencia"])
#
#        for i in range(len(json_content['records'])):
#            a_row = pd.Series(
#                [json_content['records'][i]["fields"]["fecha"], json_content['records'][i]["fields"]["anio"],
#                 json_content['records'][i]["fields"]["linea"], json_content['records'][i]["fields"]["estacion"],
#                 int(json_content['records'][i]["fields"]["afluencia"])])
#            row_df = pd.DataFrame([a_row])
#            row_df.columns = ["fecha", "anio", "linea", "estacion", "afluencia"]
#            df = pd.concat([df, row_df], ignore_index=True)
#        
#        filas_a_cargar =len(df)
#        #data_info = {'datos_a_cargar': [filas_a_cargar], 'total_anterior':[total_anterior]}
#        #total_anterior
#        #data_to_csv = pd.DataFrame(data=data_info)
#        #data_to_csv.to_csv(self.output().path,index=False)
#
#        print("Inicia la conexión con la base de datos correspondiente en RDS...")
#        connection = psycopg2.connect(user=creds.user[0],
#                                      password=creds.password[0],
#                                      host=creds.host[0],
#                                      port=creds.port[0],
#                                      database=creds.db[0])
#        cursor = connection.cursor()
#        print("Conexión realizada exitosamente! :) --> Cargando datos a la base...")
#
#        query_anterior = "SELECT COUNT(*) FROM raw.metro;"
#        total_anterior = cursor.execute(query_anterior)
#        print(total_anterior)
#
#        for i in df.index:
#            text = "INSERT INTO raw.metro  VALUES ('%s', '%s', '%s', '%s', %d);" % (
#            df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
#            print(text)
#            cursor.execute(text)
#        
#        query_final = "SELECT COUNT(*) FROM raw.metro;"
#        total_final = cursor.execute(query_final)
#        print(total_final)
#        connection.commit()
#        cursor.close()
#        connection.close()
#        print("Carga de datos a la instancia RDS completada :)")
#        data_info = {'datos_a_cargar': [filas_a_cargar], 'total_anterior':[total_anterior], 'total_final':[total_final]}
#        #total_anterior
#        #total_final
#        data_to_csv = pd.DataFrame(data=data_info)
#        data_to_csv.to_csv(self.output().path,index=False)
#        data_to_csv.to_csv('../../columnas_leidas.csv')
#
#
#    # Envía el output al S3 bucket especificado con el nombre de output_path
#    def output(self):
#        output_path = "s3://{}/{}/metro_{}.csv". \
#            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
#        return luigi.contrib.s3.S3Target(path=output_path)
#
if __name__ == '__main__':
    luigi.copyToPostgres()