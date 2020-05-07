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
    bucket = luigi.Parameter()

    #Dado que es el iniio del pipeline, no requiere ninguna task antes
    def requires(self):
        return None

    # este código se va a ejecutar cuando se mande llamar a este task
    def run(self): 
        ses = boto3.session.Session(profile_name='rafael-dpa-proj', region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3') #Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # metemos el bucket S3 en una variable obj

        print("Iniciando extracción de datos...")
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
        print("Extracción de los datos completa")

    # Envía el output al S# bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.json". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)


############################################################# METADATA  EXTRACT TASK ##################################
class metadataExtract(luigi.Task):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket. Requires extractToJson
    """
    task_name = 'raw_api'
    date = luigi.Parameter()
    bucket = luigi.Parameter()

    # Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date)

    # Esta sección indica lo que se va a correr:
    def run(self):
        print("Inicia la carga de los metadatos del extract...")
        # Lee nuevamente el archivo JSON que se subió al S3 bucket, para después obtener metadatos sobre la carga
        file_to_read = self.task_name + '/metro_' + self.date + '.json'

        #Lee las credenciales de los archivos correspondientes
        creds = pd.read_csv("../../credentials/credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials/credentials.csv")

        print("Conectando al S3 Bucket...")
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
#        df = pd.DataFrame(columns=["fecha_ejecucion", "fecha_json", "usuario", "ip_ec2", "ruta_bucket", "status", "columns_read"])
        
        #función de EC2 para describir la instancia en la que se está trabajando
        information_metadata_ours = clientEC2.describe_instances()
        
        
        
        # Columns read indica la cantidad de columnas leidas
        columns_read = len(json_content['records'])
        fecha_ejecucion = pd.Timestamp.now()
        user = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('KeyName')
        fecha_json = self.date
        ip_ec2 = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('PrivateIpAddress')
        ruta_bucket = self.bucket
        status = 'Loaded'
        
#        client.get('Reservations')[0].get('Instances')[0].get('KeyName')

        print("Conectandose a la instancia S3 con los datos RAW...")
        #Se conecta a la postgres en el RDS con las credenciales correspondientes
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])


        # Allows Python code to execute PostgreSQL command in a database session.
        cursor = connection.cursor()
        

        # Inserta los metadatos en la tabla metadata_extract
        text = "INSERT INTO metadata_extract  VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (
        fecha_ejecucion, fecha_json, user, ip_ec2, ruta_bucket, columns_read)
        print(text)
        
        cursor.execute(text) #Execute a database operation (query or command).

        
        connection.commit() # This method sends a COMMIT statement to the MySQL server, committing the current transaction. 
        cursor.close()# Close the cursor now (rather than whenever del is executed). The cursor will be unusable from this point forward
        connection.close() # For a connection obtained from a connection pool, close() does not actually close it but returns it to the pool and makes it available for subsequent connection requests.
        print("Carga de metadatos de Extract completada! :)")

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
        creds = pd.read_csv("../../credentials/credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials/credentials.csv")
        print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
        s3 = boto3.resource('s3', aws_access_key_id=creds_aws.Access_key_ID[0],
                            aws_secret_access_key=creds_aws.Secret_access_key[0])
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
            text = "INSERT INTO raw  VALUES ('%s', '%s', '%s', '%s', %d);" % (
            df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
            print(text)
            cursor.execute(text)
        connection.commit()
        cursor.close()
        connection.close()
        print("Carga de datos a la instancia RDS completada :)")

############################################################# METADATA LOAD TASK ####################################
class Metadata_load(luigi.Task):
    """
    Function to get metadata from the loading process of mexico city metro data set on the database on postgres.
    It stores the metadata from uploading into the specified S3 bucket on AWS. Note: user MUST have the credentials 
    to use the aws s3 bucket.
    """
    task_name = 'raw_api'
    date = luigi.Parameter()
    bucket = luigi.Parameter()
    
    #Dado que este metadata hace referencia a la carga de datos en el bucket s3, requiere que se haya finalizado la ejecución de CopyToPostgres
    def requires(self):
        return copyToPostgres(bucket=self.bucket, date=self.date)

    #Obtiene los metadatos de la carga de archivos a la postgres y los carga a metadata_load
    def run(self):
        
        creds = pd.read_csv("../../credentials/credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials/credentials.csv")

        cliente_rds = boto3.client('rds')


        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])
        
        
        cursor = connection.cursor()


        df = psql.read_sql("SELECT * FROM raw.metadata_load;", connection)
        
        # Lee de raw postgresql
        #Guarda postgresql
        # Esquema Clean


#def obtiene_df(db_name, db_user, db_pass, db_endpoint):
#    "Inserta el metadata del esquema CLEANED"
#    try:
#        #connection = connect(db_name, db_user, db_pass, db_endpoint)
#        #cursor = connection.cursor()
#        #dataframe = psql.read_sql("SELECT * FROM cleaned.incidentesviales LIMIT 500000;", connection)
#
#        engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format( 
#             user = db_user, 
#             password = db_pass,
#             host = db_endpoint,
#             port = "5432", 
#             database = db_name
#             )
#
#        #create sqlalchemy engine
#        engine = create_engine(engine_string)
#
#        #read a table from database
#        dataframe = pd.read_sql_table(table_name='incidentesviales', con=engine, schema='cleaned')
#    except (Exception) as error:
#        print("***** Failed getting df: {} *****".format(error))
#
#    return dataframe







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


############################################################# RUN ALL TASK ####################################

class run_all(luigi.Task):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """
    task_name='raw_api'
    date = luigi.Parameter()
    bucket = luigi.Parameter()

    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date)



############################################################# CLEANED ###################################
#aqui
class create_clean_schema(luigi.Task):
    """
    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """
    task_name = 'raw_api'
    date = luigi.Parameter()
    bucket = luigi.Parameter()

    def requires(self):
        return copyToPostgres(bucket=self.bucket, date=self.date)

   # Esta sección indica lo que se va a correr:
    def run(self):
        # Lee nuevamente el archivo JSON que se subió al S3 bucket
        file_to_read = self.task_name + '/metro_' + self.date + '.json'

        #Lee las credenciales de los archivos correspondientes
        creds = pd.read_csv("../../credentials/credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials/credentials.csv")

        # Obtiene el acceso al S3 Bucket con las credenciales correspondientes. Utiliza la paquetería boto3
        s3 = boto3.resource('s3', aws_access_key_id=creds_aws.Access_key_ID[0],
                            aws_secret_access_key=creds_aws.Secret_access_key[0])

        # Metemos el s3 actuales en un objeto, para poder obtener los datos
        clientS3 = boto3.client('s3')

        # El content object está especificando el objeto que se va a extraer del bucket S3
        # (la carga que se acaba de hacer desde la API)
        content_object = s3.Object(self.bucket, file_to_read)

        # Esta línea lee el archivo especificado en content_object
        file_content = content_object.get()['Body'].read().decode('utf-8')
        # Carga el Json content desde el archivo leído de la S3 Bucket
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

        #aqui empiecen el código
        #df

        df['fecha'] = pd.to_datetime(df['fecha'])
        
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])


        cursor = connection.cursor()

        #crear schema cleaned
 #       connection=psycopg2.connect(user=creds.user[0],
 #                                     password=creds.password[0],
 #                                     host=creds.host[0],
 #                                     port=creds.port[0],
 #                                     database=creds.db[0])
        cursor=connection.cursor()
        sql='DROP SCHEMA IF EXISTS cleaned cascade; CREATE SCHEMA cleaned;'
        try:
            cursor.execute(sql)
            connection.commit()
        except Exception as error:
            print ("error", error)
            cursor.close()
            connection.close()

        # text = "CREATE TABLE ..... "
#        connection=psycopg2.connect(user=creds.user[0],
#                                      password=creds.password[0],
#                                      host=creds.host[0],
#                                      port=creds.port[0],
#                                      database=creds.db[0]))
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])

        cursor=connection.cursor()
        sql1=("""
            CREATE TABLE cleaned.metro (
                fecha VARCHAR,
                anio VARCHAR, 
                linea VARCHAR,
                estacion VARCHAR,
                afluencia INT
                );
            """)
        try:
            cursor.execute(sql1)
            connection.commit()  
        except Exception as error:
            print ("Error could not create the table", error)   

        
        # text = "CREATE TABLE ..... "
        # create schema if not exists cleaned;

        # drop table if exists cleaned.etl_execution;

        # create table cleaned.etl_execution (
        # "name" TEXT,
        # "extention" TEXT,
        # "schema" TEXT,
        # "action" TEXT,
        # "creator" TEXT,
        # "machine" TEXT,
        # "ip" TEXT,
        # "creation_date" TEXT,
        # "size" TEXT,
        # "location" TEXT,
        # "status" TEXT,
        # "param_year" TEXT,
        # "param_month" TEXT,
        # "param_day" TEXT,
        # "param_bucket" TEXT
        # );

        # for i in df.index:
        #     text = "INSERT INTO cleaned  VALUES ('%s', '%s', '%s', '%s', %d);" % (
        #     df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
        #     print(text)
        #     cursor.execute(text)
        # connection.commit()
        # cursor.close()
        # connection.close()
############################################################# METADATA CLEAN TASK ####################################









############################################################# SEMANTIC ###################################


#X['Dia'] = pd.DatetimeIndex(X['Fecha']).day.astype('object')
#X['Mes'] = pd.DatetimeIndex(X['Fecha']).month.astype('object')
#X['Dia_Semana'] = (pd.DatetimeIndex(X['Fecha']).weekday + 1).astype('object')

#
#class create_semantic_schema(luigi.Task):
#    """
#    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
#    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
#    bucket.
#    """
#    task_name = 'raw_api'
#    date = luigi.Parameter()
#    bucket = luigi.Parameter()
#
#    def requires(self):
#        return extractToJson(bucket=self.bucket, date=self.date)
#
#   # Esta sección indica lo que se va a correr:
#    def run(self):
#        # Lee nuevamente el archivo JSON que se subió al S3 bucket
#        file_to_read = self.task_name + '/metro_' + self.date + '.json'
#
#        #Lee las credenciales de los archivos correspondientes
#        creds = pd.read_csv("../../credentials/credentials_postgres.csv")
#        creds_aws = pd.read_csv("../../credentials/credentials.csv")
#
#        # Obtiene el acceso al S3 Bucket con las credenciales correspondientes. Utiliza la paquetería boto3
#        s3 = boto3.resource('s3', aws_access_key_id=creds_aws.Access_key_ID[0],
#                            aws_secret_access_key=creds_aws.Secret_access_key[0])
#
#        # Metemos el s3 actuales en un objeto, para poder obtener los datos
#        clientS3 = boto3.client('s3')
#
#        # El content object está especificando el objeto que se va a extraer del bucket S3
#        # (la carga que se acaba de hacer desde la API)
#        content_object = s3.Object(self.bucket, file_to_read)
#
#        # Esta línea lee el archivo especificado en content_object
#        file_content = content_object.get()['Body'].read().decode('utf-8')
#        # Carga el Json content desde el archivo leído de la S3 Bucket
#        json_content = json.loads(file_content)
#
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
#        ## Modificaciones al df
#
#
#
#
#        ######
#
#
#        #aqui empiecen el código
#        #df
#
#        #df['fecha'] = pd.to_datetime(df['fecha'])
#        
#        connection = psycopg2.connect(user=creds.user[0],
#                                      password=creds.password[0],
#                                      host=creds.host[0],
#                                      port=creds.port[0],
#                                      database=creds.db[0])
#
#
#        cursor = connection.cursor()
#
#        #crear schema semantic
#        connection=connect()
#        cursor=connection.cursor()
#        sql='DROP SCHEMA IF EXISTS semantic cascade; CREATE SCHEMA semantic;'
#        try:
#            cursor.execute(sql)
#            connection.commit()
#        except Exception as error:
#            print ("error", error)
#            cursor.close()
#            connection.close()
#
#        # text = "CREATE TABLE ..... "
#    connection=connect()
#    cursor=connection.cursor()
#    sql1=("""
#        CREATE TABLE semantic.metro (
#            fecha VARCHAR,
#            anio VARCHAR, 
#            linea VARCHAR,
#            estacion VARCHAR,
#            afluencia INT
#            );
#        """)
#    try:
#        cursor.execute(sql1)
#        connection.commit()  
#    except Exception as error:
#        print ("I can't create tables", error)
# 
##class createTable(CopyToTable):
##
##    def run(self):
##        credentials = pd.read_csv("credentials_postgres.csv")
##        user = credentials.user[0]
##        password = credentials.password[0]
##        database = credentials.db[0]
##        host = credentials.host[0]
##        table = 'raw'
##
##        columns = [("fecha", "VARCHAR"),
##                   ("anio", "VARCHAR"), 
##                   ("linea", "VARCHAR"),
##                   ("estacion", "VARCHAR"),
##                   ("afluencia", "INT")]
##
#
#
#
#
#    cursor.close()
#    connection.close() 
#       
#        # create schema if not exists cleaned;
#
#        # drop table if exists cleaned.etl_execution;
#
#        #create table cleaned.etl_execution (
#        # "name" TEXT,
#        # "extention" TEXT,
#        # "schema" TEXT,
#        # "action" TEXT,
#        # "creator" TEXT,
#        # "machine" TEXT,
#        # "ip" TEXT,
#        # "creation_date" TEXT,
#        # "size" TEXT,
#        # "location" TEXT,
#        # "status" TEXT,
#        # "param_year" TEXT,
#        # "param_month" TEXT,
#        # "param_day" TEXT,
#        # "param_bucket" TEXT
#        # );
#
#
#
#    for i in df.index:
#           text = "INSERT INTO semantic  VALUES ('%s', '%s', '%s', '%s', %d);" % (
#           df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
#           print(text)
#           cursor.execute(text)
#    connection.commit()
#    cursor.close()
#    connection.close()
#
#
#''''
#Falta saber qué variables agregar en el modelo
#Para este ejemplo se agregarán dos variables enteras: var1, var2
#
#        for i in df.index:
#            text = "INSERT INTO semantic  VALUES ('%s', '%s', '%s', '%s', %d, %d, %d);" % (
#            df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i], df["var1"][i], df["var"][i])
#            print(text)
#            cursor.execute(text)
#        connection.commit()
#        cursor.close()
#        connection.close()
#''''
#
############################################################## METADATA LOAD TASK ####################################
#
#
#
#
#
#
#
#
#
############################################################## EMPEZAR MODELADO ###################################
#
#class SeparaBase(luigi.Task):
#    "Esta tarea separa la base en la Train & Test"
#
#    # Parametros del RDS
#    db_instance_id = luigi.Parameter()
#    db_name = luigi.Parameter()
#    db_user_name = luigi.Parameter()
#    db_user_password = luigi.Parameter()
#    subnet_group = luigi.Parameter()
#    security_group = luigi.Parameter()
#    # Parametros del Bucket
#    bucket = luigi.Parameter()
#    root_path = luigi.Parameter()
#
#    #Para la tarea actual
#    folder_path = '2.separacion_base'
#
#    def requires(self):
#        return PreprocesoBase(self.db_instance_id, self.db_name, self.db_user_name,
#                              self.db_user_password, self.subnet_group, self.security_group,
#                              self.bucket, self.root_path)
#
#
#    def run(self):
#
#        with self.input().open('r') as infile:
#             dataframe = pd.read_csv(infile, sep="\t")
#            #print('Pude leer el csv\n' , dataframe.head(5))
#            
#            
#            indice_ent = X['Fecha'] <= '2019-11-30'
#            
#            variables_a_eliminar = ['Fecha', 'Año', 'Afluencia']
#
#            x_mat = pd.get_dummies(X, columns = variables_categoricas, drop_first = True)
#        
#            x_ent = x_mat[indice_ent].drop(variables_a_eliminar, axis = 1)
#            x_pr = x_mat[~indice_ent].drop(variables_a_eliminar, axis = 1)
#            y_ent = categorias(x_mat['Afluencia'][indice_ent], 
#                           x_mat['Afluencia'][indice_ent])
#            y_pr = categorias(x_mat['Afluencia'][~indice_ent], 
#                          x_mat['Afluencia'][indice_ent])
#
#
#            vars_modelo = ['delegacion_inicio','mes','dia_semana','hora', 'tipo_entrada', 'incidente_c4_rec', 'target']
#            var_target = 'target'
#            [X_train, X_test, y_train, y_test] = funciones_mod.separa_train_y_test(dataframe, vars_modelo, var_target)
#
#            
#
#        
#
#
#       ses = boto3.session.Session(profile_name='default', region_name='us-east-1')
#       s3_resource = ses.resource('s3')
#       obj = s3_resource.Bucket(self.bucket)
#
#       with self.output()['x_ent'].open('w') as outfile1:
#            x_ent.to_csv(outfile1, sep='\t', encoding='utf-8', index=None)
#
#       with self.output()['x_pr'].open('w') as outfile2:
#            x_pr.to_csv(outfile2, sep='\t', encoding='utf-8', index=None)
#
#       with self.output()['y_ent'].open('w') as outfile3:
#            y_ent.to_csv(outfile3, sep='\t', encoding='utf-8', index=None)
#
#       with self.output()['y_pr'].open('w') as outfile4:
#            y_pr.to_csv(outfile4, sep='\t', encoding='utf-8', index=None)
#
##import os
##directorio = 'C:\\Users\\valen\\Documents\\Maestria-Data-Science\\Spring-2020\\MetodosGranEscala\\proyecto2\\data-product-architecture-Project\\modeloML'
##os.chdir(directorio)
##import luigi
##import numpy as np
##import pandas as pd
##from sklearn.impute import SimpleImputer
##from sklearn.linear_model import LogisticRegression
##from sklearn.metrics import confusion_matrix
##
##class MetroDataIngestion(luigi.Task):
##
##    def run(self):
##        X = pd.read_csv('afluencia-diaria-del-metro-cdmx.csv')
##        X.to_csv(self.output().path, index=False)
##
##    def output(self):
##        return luigi.LocalTarget("./Xtrain.csv")
##
###X = pd.read_csv('afluencia-diaria-del-metro-cdmx.csv')
##
##def rmse(y, pred):
##    return(np.sqrt(np.mean((y-pred)**2)))
##
##def categorias(x, y):
##    n = len(x)
##    z = np.array(x, dtype = str)    
##    q25 = np.quantile(y, 0.25)
##    q75 = np.quantile(y, 0.75)
##    z[x <= q25] = 'Bajo'
##    z[(x >= q25) & (x <= q75)] = 'Normal'
##    z[x >= q75] = 'Alto'
##    return(z)
##
##X['Fecha'] = pd.to_datetime(X['Fecha'])
##X['Dia'] = pd.DatetimeIndex(X['Fecha']).day.astype('object')
##X['Mes'] = pd.DatetimeIndex(X['Fecha']).month.astype('object')
##X['Dia_Semana'] = (pd.DatetimeIndex(X['Fecha']).weekday + 1).astype('object')
##
##indice_ent = X['Fecha'] <= '2019-11-30'
##
##variables_a_eliminar = ['Fecha', 'Año', 'Afluencia']
##
##variables_categoricas = X.dtypes.pipe(lambda x: x[x == 'object']).index
##
##num_cols = X.dtypes.pipe(lambda x: x[x != 'object']).index
##for x in num_cols:
##    imp = SimpleImputer(missing_values = np.nan, strategy = 'median')
##    imp.fit(np.array(X[x]).reshape(-1, 1))
##    X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))
##
##nominal_cols = X.dtypes.pipe(lambda x: x[x == 'object']).index
##for x in nominal_cols:
##    imp = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
##    imp.fit(np.array(X[x]).reshape(-1, 1))
##    X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))
##
##x_mat = pd.get_dummies(X, columns = variables_categoricas, drop_first = True)
##
##x_ent = x_mat[indice_ent].drop(variables_a_eliminar, axis = 1)
##x_pr = x_mat[~indice_ent].drop(variables_a_eliminar, axis = 1)
##y_ent = categorias(x_mat['Afluencia'][indice_ent], 
##                   x_mat['Afluencia'][indice_ent])
##y_pr = categorias(x_mat['Afluencia'][~indice_ent], 
##                  x_mat['Afluencia'][indice_ent])
##
##def modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc):
##
##    y_ent1 = np.where(y_ent == cat, 1, 0)
##    y_pr1 = np.where(y_pr == cat, 1, 0)
##
##    modelo = LogisticRegression()
##    modelo.fit(x_ent, y_ent1)
##
##    pred = modelo.predict_proba(x_pr)[:,1]
##    prob = pred.copy()
##    pred = np.where(pred >= sc, 1, 0)
##    TP = np.sum((pred == 1) & (y_pr1 == 1))
##    TN = np.sum((pred == 0) & (y_pr1 == 0))
##    FP = np.sum((pred == 1) & (y_pr1 == 0))
##    FN = np.sum((pred == 0) & (y_pr1 == 1))
##
##    accuracy = (TP+TN)/(TP+TN+FP+FN)
##
##    precision = TP/(TP+FP)
##
##    recall = TP/(TP+FN)
##
##    a = {'modelo':modelo, 'pred':pred, 'prob':prob, 
##         'accuracy':accuracy, 'precision':precision, 'recall':recall}
##    return(a)
##
##cat = 'Bajo'
##sc = 0.56
##modelo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)
##
##modelo['accuracy']
##modelo['precision']
##modelo['recall']
##pred_bajo = modelo['pred']
##prob_bajo = modelo['prob']
##
##cat = 'Normal'
##sc = 0.50
##modelo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)
##
##modelo['accuracy']
##modelo['precision']
##modelo['recall']
##pred_normal = modelo['pred']
##prob_normal = modelo['prob']
##
##cat = 'Alto'
##sc = 0.50
##modelo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)
##
##modelo['accuracy']
##modelo['precision']
##modelo['recall']
##pred_alto = modelo['pred']
##prob_alto = modelo['prob']
##
##def pred_final(pred_bajo, prob_bajo, 
##               pred_normal, prob_normal, 
##               pred_alto, prob_alto):
##
##    n = len(pred_normal)
##    pred_final = np.array(pred_normal, dtype = str)
##    pred = pd.DataFrame({'Bajo':pred_bajo, 
##                         'Normal':pred_normal, 
##                         'Alto':pred_alto})
##    prob = pd.DataFrame({'Bajo':prob_bajo, 
##                         'Normal':prob_normal, 
##                         'Alto':prob_alto})
##    
##    for i in np.arange(1, n+1):
##        if pred.iloc[i-1, :].sum() == 1:
##            pred_final[i-1] = pred.iloc[i-1, :].idxmax()
##        else:
##            pred_final[i-1] = prob.iloc[i-1, :].idxmax()
##    
##    return(pred_final)
##
##pred_f = pred_final(pred_bajo, prob_bajo, 
##               pred_normal, prob_normal, 
##               pred_alto, prob_alto)
##
##conf = pd.DataFrame(confusion_matrix(y_pr, pred_f), 
##                    index = ['real Bajo', 'real Normal', 'real Alto'], 
##                    columns = ['pred Bajo', 'pred Normal', 'pred Alto'])
##conf
##
##accuracy = np.sum(np.diag(conf))/np.sum(conf).sum()
##accuracy
##
#
#
if __name__ == '__main__':
    luigi.run_all()