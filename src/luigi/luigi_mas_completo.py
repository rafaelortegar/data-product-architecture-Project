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

################################## Extract to Json Task ###############################################################
class extractToJson(luigi.Task):
    """
    Function to extract data from the metro dataset from mexico city on the specified date. It uploads
    the raw data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3 bucket.
    """
    task_name = 'raw_api'
    date = luigi.Parameter()
    bucket = luigi.Parameter()

    def requires(self):
        return None

    def run(self):
        ses = boto3.session.Session(profile_name='gabster', region_name='us-west-2')
        s3_resource = ses.resource('s3')
        obj = s3_resource.Bucket(self.bucket)

        # Obtiene los datos en formato raw desde la liga de la api
        data_raw = requests.get(
            f"https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=afluencia-diaria-del-metro-cdmx&rows=10000&sort=-fecha&refine.fecha={self.date}")
        # data_raw.status_code
        # data_raw.headers['content-type']
        # data_raw.headers['Date']
        # data_raw.json()

        # Escribe un JSON con la información descargada de la API
        with self.output().open('w') as json_file:
            json.dump(data_raw.json(), json_file)

    # Envía el output al S# bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.json". \
            format(self.bucket, self.task_name, self.date)
        return luigi.contrib.s3.S3Target(path=output_path)


############################################################# METADATA  EXTRACT TASK ##################################
class metadataExtract(luigi.Task):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """
    task_name = 'raw_api'
    date = luigi.Parameter()
    bucket = luigi.Parameter()

    # Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date)

    # Esta sección indica lo que se va a correr:
    def run(self):
        # Lee nuevamente el archivo JSON que se subió al S# bucket, para después obtener metadatos sobre la carga
        file_to_read = self.task_name + '/metro_' + self.date + '.json'

        #Lee las credenciales de los archivos correspondientes
        creds = pd.read_csv("../../credentials/credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials/credentials.csv")

        # Obtiene el acceso al S3 Bucket con las credenciales correspondientes. Utiliza la paquetería boto3
        s3 = boto3.resource('s3', aws_access_key_id=creds_aws.Access_key_ID[0],
                            aws_secret_access_key=creds_aws.Secret_access_key[0])

        # Metemos el ec2 y el s3 actuales en un objeto, para poder obtener sus metadatos
        clientEC2 = boto3.client('ec2')
        clientS3 = boto3.client('s3')

        # El content object está especificando el objeto que se va a extraer del bucket S3
        # (la carga que se acaba de hacer desde la API)
        content_object = s3.Object(self.bucket, file_to_read)

        # Esta línea lee el archivo especificado en content_object
        file_content = content_object.get()['Body'].read().decode('utf-8')
        # Carga el Json content desde el archivo leído de la S3 Bucket
        json_content = json.loads(file_content)

        # Inicializa el data frame que se va a meter la información de los metadatos
        df = pd.DataFrame(columns=["fecha_ejecucion", "fecha_json", "usuario", "ip_ec2", "ruta_bucket", "status", "columns_read"])

        # Columns read indica la cantidad de columnas leidas
        columns_read = len(json_content['records'])
        fecha_ejecucion =
        clientEC2

        client.get('Reservations')[0].get('Instances')[0].get('KeyName')



        for i in range(len(json_content['records'])):
            a_row = pd.Series(
                [json_content['records'][i]["fields"]["fecha"], json_content['records'][i]["fields"]["anio"],
                 json_content['records'][i]["fields"]["linea"], json_content['records'][i]["fields"]["estacion"],
                 int(json_content['records'][i]["fields"]["afluencia"])])
            row_df = pd.DataFrame([a_row])
            row_df.columns = ["fecha", "anio", "linea", "estacion", "afluencia"]
            df = pd.concat([df, row_df], ignore_index=True)


        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])


        cursor = connection.cursor()

        for i in df.index:
            text = "INSERT INTO raw  VALUES ('%s', '%s', '%s', '%s', %d);" % (
            df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
            print(text)
            cursor.execute(text)
        connection.commit()
        cursor.close()
        connection.close()


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
        file_to_read = self.task_name + '/metro_' + self.date + '.json'
        creds = pd.read_csv("../../credentials/credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials/credentials.csv")
        s3 = boto3.resource('s3', aws_access_key_id=creds_aws.Access_key_ID[0],
                            aws_secret_access_key=creds_aws.Secret_access_key[0])
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
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])
        cursor = connection.cursor()
        for i in df.index:
            text = "INSERT INTO raw  VALUES ('%s', '%s', '%s', '%s', %d);" % (
            df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
            print(text)
            cursor.execute(text)
        connection.commit()
        cursor.close()
        connection.close()

############################################################# METADATA  LOAD TASK ####################################










############################################################# RUN ALL TASK ####################################





class run_all(luigi.Task):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """
    task_name=''
    date = luigi.Parameter()
    bucket = luigi.Parameter()

    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date)