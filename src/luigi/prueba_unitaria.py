# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parametro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=mge luigi --module ex3_luigi S3Task --local-scheduler ...
#imports
import requests
import pandas
import json
import luigi
import boto3
import psycopg2
import sys

import pandas as pd
import luigi.contrib.s3
import os
import datetime
import pandas.io.sql as psql
from luigi.contrib.postgres import CopyToTable, PostgresQuery

################################## Extract to Json Task ###############################################################
class extractToJson(luigi.Task):
    """
    Function to extract data from the metro dataset from mexico city on the specified date. It uploads
    the raw data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3 bucket.
    """
    task_name = 'raw_api'
#    ece2 = boto3.client('ec2')
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3') # , region='us-west-2')

    #Dado que es el inicio del pipeline, no requiere ninguna task antes
    def requires(self):
        return None

    # este código se va a ejecutar cuando se mande llamar a este task
    def run(self): 
        creds_aws = pd.read_csv("../../credentials/credentials.csv")
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region='us-west-2') #profile_name='rafael-dpa-proj', region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3', aws_access_key_id=creds_aws.aws_access_key_id[0],
                            aws_secret_access_key=creds_aws.aws_secret_access_key[0]) #Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # metemos el bucket S3 en una variable obj

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Iniciando extracción de datos...")
        # Obtiene los datos en formato raw desde la liga de la api
        data_raw = requests.get(
            f"https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=afluencia-diaria-del-metro-cdmx&rows=10000&sort=-fecha&refine.fecha={self.date}")
        

        # Escribe un JSON con la información descargada de la API
        with self.output().open('w') as json_file:
            json.dump(data_raw.json(), json_file)
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Extracción de los datos completa!! :)")

    # Envía el output al S3 bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.json". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)

############################################################# COPY TO POSTGRESS TASK ###################################



class copyToPostgres(luigi.Task):
    """
    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """
    task_name = 'raw_api'
    date = luigi.Parameter()
    bucket = luigi.Parameter()

    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date)

    def run(self):
        print("Inicia la extracción de los datos cargados en RAW para cargarlos a postgres...")
        file_to_read = self.task_name + '/metro_' + self.date + '.json'
        creds = pd.read_csv("../../credentials_postgres.csv")
        session = boto3.Session(profile_name='default')
        dev_s3_client = session.client('s3')
        #creds_aws = pd.read_csv("../../credentials.csv")
        print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
        s3 = boto3.resource('s3')#, aws_access_key_id=creds_aws.aws_access_key_id[0],
                            #aws_secret_access_key=creds_aws.aws_secret_access_key[0])
        print("Conexión Exitosa! :)")
        content_object = s3.Object(self.bucket, file_to_read)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)

        df = pd.DataFrame(columns=["fecha", "anio", "linea", "estacion", "afluencia"])

        for i in range(len(json_content['records'])):
            a_row = pd.Series(
                [json_content['records'][i]["fields"]["fecha"], json_content['records'][i]["fields"]["anio"],
                 json_content['records'][i]["fields"]["linea"], json_content['records'][i]["fields"]["estacion"],
                 int(json_content['records'][i]["fields"]["afluencia"])])
            row_df = pd.DataFrame([a_row])
            row_df.columns = ["fecha", "anio", "linea", "estacion", "afluencia"]
            df = pd.concat([df, row_df], ignore_index=True)
        
        print("Inicia la conexión con la base de datos correspondiente en RDS...")
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])
        cursor = connection.cursor()
        print("Conexión realizada exitosamente! :) --> Cargando datos a la base...")
        for i in df.index:
            text = "INSERT INTO raw.metro  VALUES ('%s', '%s', '%s', '%s', %d);" % (
            df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
            print(text)
            cursor.execute(text)
        connection.commit()
        cursor.close()
        connection.close()
        print("Carga de datos a la instancia RDS completada :)")

