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
import sklearn
import sys
import pandas as pd
import luigi.contrib.s3
import os
import datetime
import pandas.io.sql as psql
from luigi.contrib.postgres import CopyToTable, PostgresQuery
import sqlalchemy
from sqlalchemy import create_engine
import csv
# from luigi import flatten

import feature_builder as fb

################################## Extract to Json Task ###############################################################
class extractToJson(luigi.Task):
    """
    Function to extract data from the metro dataset from mexico city on the specified date. It uploads
    the raw data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3 bucket.
    """
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'extractToJson_task_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter() # default='dpaprojs3')
    #==============================================================================================================

    #Dado que es el inicio del pipeline, no requiere ninguna task antes
    def requires(self):
        return None

    # este código se va a ejecutar cuando se mande llamar a este task
    def run(self): 
        creds_aws = pd.read_csv("../../credentials.csv")
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') # , region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3')
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
        

        # Escribe un JSON con la información descargada de la API, aqui esta el output
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


############################################################# METADATA  EXTRACT TASK ##################################
class metadataExtract(luigi.Task):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket. Requires extractToJson
    """
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'metadataExtract_task_02_02'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3') # default='dpaprojs3')
    #==============================================================================================================

    # Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return extractToJson(self.bucket, self.date)

    # Esta sección indica lo que se va a correr:
    def run(self):
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Inicia la carga de los metadatos del extract...")

        # Lee nuevamente el archivo JSON que se subió al S3 bucket, para después obtener metadatos sobre la carga
        file_to_read = 'extractToJson_task_01/metro_'+ self.date +'.json'
        print("El archivo a buscar es: ",file_to_read)

        #Lee las credenciales de los archivos correspondientes
        creds = pd.read_csv("../../credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials.csv")
        print('Credenciales leídas correctamente')

        # Conexión a la S3
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
        dev_s3_client = session.client('s3')

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Conectando al S3 Bucket...")
        # Obtiene el acceso al S3 Bucket con las credenciales correspondientes. Utiliza la paquetería boto3
        
        # Metemos el ec2 y el s3 actuales en un objeto, para poder obtener sus metadatos
        clientEC2 = boto3.client('ec2')
        clientS3 = boto3.client('s3')
        print("Inicializados el EC2 y el S3")

        # El content object está especificando el objeto que se va a extraer del bucket S3
        # (la carga que se acaba de hacer desde la API)
        content_object = s3_resource.Object(self.bucket, file_to_read)
        print("s3 encontrada exitosamente")

        # Esta línea lee el archivo especificado en content_object
        file_content = content_object.get()['Body'].read().decode('utf-8')
        #columns_read = content_object.get()['Body'].read().decode('utf-8')['facet_groups']['facets']['count']
        print("contenido leído exitosamente")
        # Carga el Json content desde el archivo leído de la S3 Bucket
        json_content = json.loads(file_content)
        print("contenido cargado exitosamente")

        # Inicializa el data frame que se va a meter la información de los metadatos
#        df = pd.DataFrame(columns=["fecha_ejecucion", "fecha_json", "usuario", "ip_ec2", "ruta_bucket", "status", "columns_read"])
        
        #función de EC2 para describir la instancia en la que se está trabajando
        information_metadata_ours = clientEC2.describe_instances()
        print("ec2 descrita correctamente")
        
        
        
        # Columns read indica la cantidad de columnas leidas
        columns_read = len(json_content['records'])
        fecha_ejecucion = pd.Timestamp.now()
        user = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('KeyName')
        fecha_json = self.date
        ip_ec2 = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('PrivateIpAddress')
        nombre_bucket = self.bucket
        status = 'Loaded'
        print("variables a cargar listas")
        
#        client.get('Reservations')[0].get('Instances')[0].get('KeyName')

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Conectandose a la instancia RDS con los datos RAW...")
        #Se conecta a la postgres en el RDS con las credenciales correspondientes
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])


        # Allows Python code to execute PostgreSQL command in a database session.
        cursor = connection.cursor()
        

        # Inserta los metadatos en la tabla metadata_extract
        text = "INSERT INTO raw.metadataextract  VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (
        user,fecha_ejecucion, fecha_json,ip_ec2, nombre_bucket, columns_read)
        print(text)
        
        cursor.execute(text) #Execute a database operation (query or command).

        
        connection.commit() # This method sends a COMMIT statement to the MySQL server, committing the current transaction. 
        cursor.close()# Close the cursor now (rather than whenever del is executed). The cursor will be unusable from this point forward
        connection.close() # For a connection obtained from a connection pool, close() does not actually close it but returns it to the pool and makes it available for subsequent connection requests.
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Carga de metadatos de Extract completada! :)")
        
        # para los outputs que no vamos a usar
        vacio = ' '
        data_vacia = {'vacio':[vacio]}
        pandas_a_csv = pd.DataFrame(data=data_vacia)
        pandas_a_csv(output().path, index=False)
        #with self.output().open('w') as json_file:
        #    json.dump(data_raw.json(), json_file)

    
    # Envía el output al S3 bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.csv". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)

############################################################ CREATE TABLES #############################################
class createTables(luigi.Task):
    """
    Function to create tables on RDS. Note: user MUST have the credentials to use the aws s3
    bucket and the RDS instance.
    """    

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'extractToJson_task_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    def requires(self):
        return extractToJson(self.bucket, self.date), metadataExtract(self.bucket, self.date)


    def run(self):

        print("Iniciando conexión a la S3 de datos...")
        creds = pd.read_csv("../../credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials.csv")
        print("credenciales leídas correctamente")

        # Conexión a la S3
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
        dev_s3_client = ses.client('s3')
        print("conexión a la s3 exitosa :)")

        file_to_read = 'extractToJson_task_01/metro_' + self.date + '.json'
        print("El archivo a leer es: ",file_to_read)

        # Obtiene los datos en formato raw desde la liga de la api
        data_raw = requests.get(
            f"https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=afluencia-diaria-del-metro-cdmx&rows=10000&sort=-fecha&refine.fecha={self.date}")
        

        # Escribe un JSON con la información descargada de la API, aqui esta el output
        with self.output().open('w') as json_file:
            json.dump(data_raw.json(), json_file)
        #data_raw = s3_resource.Object(self.bucket, file_to_read)

        print("Iniciando la conexión con la base de datos en RDS que contiene los datos extraídos...")
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])
        
        print("Creando los schemas...")
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS raw;
            CREATE TABLE IF NOT EXISTS raw.metro(
                Fecha VARCHAR, 
                Ano VARCHAR, 
                Linea VARCHAR, 
                Estacion VARCHAR,
                Afluencia INT            
            );
            CREATE TABLE IF NOT EXISTS raw.metadataextract(
                usuario VARCHAR,
                fecha_ejecucion DATE,
                fecha_json DATE,
                ip_ec2 VARCHAR,
                nombre_bucket VARCHAR,
                columns_read INT
                
            );
            CREATE TABLE IF NOT EXISTS raw.metadataload(
                usuario VARCHAR,
                fecha_ejecucion DATE,
                fecha_json DATE,
                ip_ec2 VARCHAR,
                nombre_bucket VARCHAR,
                columns_loaded INT
    
            );
            CREATE SCHEMA IF NOT EXISTS cleaned;
            CREATE TABLE IF NOT EXISTS cleaned.metro (
                fecha DATE, 
                anio VARCHAR, 
                linea VARCHAR, 
                estacion VARCHAR,
                afluencia INT
            );
            CREATE SCHEMA IF NOT EXISTS semantic;
            CREATE TABLE IF NOT EXISTS semantic.metro(
                fecha DATE, 
                anio VARCHAR, 
                linea VARCHAR, 
                estacion VARCHAR,
                afluencia INT            
            );
            """)
            print("si se crearon los schemas")
            connection.commit()
            cursor.close()
            connection.close()  
        except Exception as error:
            print ("Error, no pudo crear las tablas", error)  

            cursor.close()
            connection.close()
        
        print("Schemas y tablas creados correctamente :)")
        
        # para los outputs que no vamos a usar
        #vacio = ' '
        #data_vacia = {'vacio':[vacio]}
        #pandas_a_csv = pd.DataFrame(data=data_vacia)
        #pandas_a_csv(output().path, index=False)
        
        # Escribe un JSON con la información descargada de la API, aqui esta el output
        #with self.output().open('w') as json_file:
        #    json.dump(data_raw.json(), json_file)
        print("archivo creado correctamente")

    
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

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'load_task_03_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date) #, createTables(self.bucket, self.date)

    def run(self):

        # Los archivos que se usan por el pipeline
        print("Inicia la extracción de los datos cargados en la S3 para cargarlos a postgres...")
        file_to_read = 'extractToJson_task_01/metro_' + self.date + '.json'
        #archivoquenosirve = 'createTables_task_02_01/metro_' + self.date + '.csv'
        print("El archivo a leer es: ",file_to_read)
        
        # Leyendo credenciales
        creds = pd.read_csv("../../credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials.csv")
        print("credenciales leídas correctamente")

        # Conexión a la S3
        print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
        dev_s3_client = ses.client('s3')
        obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
        print("Conexión Exitosa! :)")

        #archivoquenosirve_object = s3_resource.Object(self.bucket, archivoquenosirve)
        content_object = s3_resource.Object(self.bucket, file_to_read)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        print("Archivo cargado correctamente...")

        df = pd.DataFrame(columns=["fecha", "anio", "linea", "estacion", "afluencia"])

        for i in range(len(json_content['records'])):
            a_row = pd.Series(
                [json_content['records'][i]["fields"]["fecha"], json_content['records'][i]["fields"]["anio"],
                 json_content['records'][i]["fields"]["linea"], json_content['records'][i]["fields"]["estacion"],
                 int(json_content['records'][i]["fields"]["afluencia"])])
            row_df = pd.DataFrame([a_row])
            row_df.columns = ["fecha", "anio", "linea", "estacion", "afluencia"]
            df = pd.concat([df, row_df], ignore_index=True)
        
        filas_a_cargar =len(df)
        #data_info = {'datos_a_cargar': [filas_a_cargar], 'total_anterior':[total_anterior]}
        #total_anterior
        #data_to_csv = pd.DataFrame(data=data_info)
        #data_to_csv.to_csv(self.output().path,index=False)

        print("Inicia la conexión con la base de datos correspondiente en RDS...")
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])
        cursor = connection.cursor()
        print("Conexión realizada exitosamente! :) --> Cargando datos a la base...")

        query_anterior = "SELECT COUNT(*) FROM raw.metro;"
        total_anterior = cursor.execute(query_anterior)
        print(total_anterior)

        for i in df.index:
            text = "INSERT INTO raw.metro  VALUES ('%s', '%s', '%s', '%s', %d);" % (
            df["fecha"][i], df["anio"][i], df["linea"][i], df["estacion"][i], df["afluencia"][i])
            print(text)
            cursor.execute(text)
        
        query_final = "SELECT COUNT(*) FROM raw.metro;"
        total_final = cursor.execute(query_final)
        print(total_final)
        connection.commit()
        cursor.close()
        connection.close()
        print("Carga de datos a la instancia RDS completada :)")
        data_info = {'datos_a_cargar': [filas_a_cargar], 'total_anterior':[total_anterior], 'total_final':[total_final]}
        #total_anterior
        #total_final
        data_to_csv = pd.DataFrame(data=data_info)
        data_to_csv.to_csv(self.output().path,index=False)


    # Envía el output al S3 bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.csv". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)


############################################################# METADATA LOAD TASK ####################################
class metadataLoad(luigi.Task):
    """
    Function to get metadata from the loading process of mexico city metro data set on the database on postgres.
    It stores the metadata from uploading into the specified S3 bucket on AWS. Note: user MUST have the credentials 
    to use the aws s3 bucket.
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'metadata_load_04_02'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3') # default='dpaprojs3')
    #==============================================================================================================

    # Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return copyToPostgres(bucket=self.bucket, date=self.date)

    # Esta sección indica lo que se va a correr:
    def run(self):
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Inicia la carga de los metadatos del extract...")
        # Lee nuevamente el archivo JSON que se subió al S3 bucket, para después obtener metadatos sobre la carga
        file_to_read = 'load_task_03_01/metro_' + self.date + '.csv'

        creds = pd.read_csv("../../credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials.csv")
        print("credenciales leídas correctamente")

        # Conexión a la S3
        print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
        print("Conexión Exitosa! :)")

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Conectando al S3 Bucket...")
        
        # Metemos el ec2 y el s3 actuales en un objeto, para poder obtener sus metadatos
        clientEC2 = boto3.client('ec2')
        clientS3 = boto3.client('s3')
        print("Inicializados el EC2 y el S3")

        # El content object está especificando el objeto que se va a extraer del bucket S3
        # (la carga que se acaba de hacer desde la API)
        content_object = s3_resource.Object(self.bucket, file_to_read)
        print("s3 encontrada exitosamente")

        # Esta línea lee el archivo especificado en content_object
        file_content = pd.read_csv(content_object)    # content_object.get()['Body'].read().decode('utf-8') # Esto está de más
        print("contenido leído exitosamente")
        # Carga el Json content desde el archivo leído de la S3 Bucket
        #json_content = json.loads(file_content) # Esto está de más
        print("contenido cargado exitosamente")
        
        #función de EC2 para describir la instancia en la que se está trabajando
        information_metadata_ours = clientEC2.describe_instances()
        print("ec2 descrita correctamente")
        
        columnas_leidas = file_content # pd.read_csv('../../columnas_leidas.csv')
        print("csv leido correctamente")
        
        
        # Columns read indica la cantidad de columnas leidas
        columns_loaded = columnas_leidas['datos a cargar'][0]
        print("se cargaron:", columns_loaded, " columnas.")
        print(columns_loaded)
        fecha_ejecucion = pd.Timestamp.now()
        user = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('KeyName')
        fecha_json = self.date
        ip_ec2 = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('PrivateIpAddress')
        nombre_bucket = self.bucket
        status = 'Loaded'
        print("variables a cargar listas")
        
#        client.get('Reservations')[0].get('Instances')[0].get('KeyName')

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Conectandose a la instancia RDS con los datos RAW...")
        #Se conecta a la postgres en el RDS con las credenciales correspondientes
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])


        # Allows Python code to execute PostgreSQL command in a database session.
        cursor = connection.cursor()
        

        # Inserta los metadatos en la tabla metadata_extract
        text = "INSERT INTO raw.metadataload  VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (
        user,fecha_ejecucion, fecha_json,ip_ec2, nombre_bucket, columns_loaded)
        print(text)
        
        cursor.execute(text) #Execute a database operation (query or command).

        
        connection.commit() # This method sends a COMMIT statement to the MySQL server, committing the current transaction. 
        cursor.close()# Close the cursor now (rather than whenever del is executed). The cursor will be unusable from this point forward
        connection.close() # For a connection obtained from a connection pool, close() does not actually close it but returns it to the pool and makes it available for subsequent connection requests.
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Carga de metadatos de Extract completada! :)")

        # para los outputs que no vamos a usar
        vacio = ' '
        data_vacia = {'vacio':[vacio]}
        pandas_a_csv = pd.DataFrame(data=data_vacia)
        pandas_a_csv(output().path, index=False)
        print("archivo creado correctamente")


    # Envía el output al S3 bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.csv". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)


############################################################# CLEANED ###################################
##aqui
class loadCleaned(luigi.Task):

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name='cleaned_data_04_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================
    
    def requires(self):
        return copyToPostgres(bucket = self.bucket, date=  self.date)
    
    
    def run(self):

        # Lee nuevamente el archivo JSON que se subió al S3 bucket, para después obtener metadatos sobre la carga
        archivoquenosirve = 'load_task_03_01/metro_' + self.date + '.csv'

        creds = pd.read_csv("../../credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials.csv")
        print("credenciales leídas correctamente")

        # Conexión a la S3
        print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
        print("Conexión Exitosa! :)")

        archivoquenosirve_object = s3_resource.Object(self.bucket, archivoquenosirve)
        #lectura_de_archivo = pd.read_csv(archivoquenosirve_object) 

        connection = psycopg2.connect(user=creds.user[0],
                                          password=creds.password[0],
                                          host=creds.host[0],
                                          port=creds.port[0],
                                          database=creds.db[0])

                                          # metadata_load_04_01
    
        cursor = connection.cursor()
        query = """
            drop table if exists cleaned.metro cascade;
            create table cleaned.metro as (
                SELECT 
                "Fecha"::DATE as fecha, 
                "Ano"::int as ano, 
                "Linea"::varchar as linea, 
                "Estacion"::varchar as estacion,
                "Afluencia"::int as afluencia
                from raw.metro
                );
                """    
        cursor.execute(query) #Execute a database operation (query or command).
        connection.commit() # This method sends a COMMIT statement to the MySQL server, committing the current transaction. 
        cursor.close()# Close the cursor now (rather than whenever del is executed). The cursor will be unusable from this point forward
        connection.close()

        print("cerró conexión")


        # para los outputs que no vamos a usar
        vacio = ' '
        data_vacia = {'vacio':[vacio]}
        pandas_a_csv = pd.DataFrame(data=data_vacia)
        pandas_a_csv.to_csv(self.output().path, index=False)
        print("archivo creado correctamente")


    # Envía el output al S3 bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.csv". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)

##############################################################  METADATA CLEANED  #####################################
class metadataCleaned(luigi.Task):
    """
    Function to get metadata from the loading process of mexico city metro data set on the database on postgres.
    It stores the metadata from uploading into the specified S3 bucket on AWS. Note: user MUST have the credentials 
    to use the aws s3 bucket.
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'metadata_cleaned_05_02'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3') # default='dpaprojs3')
    #==============================================================================================================

    # Indica que para iniciar el proceso de carga de metadatos requiere que emetadataloadl task de extractToJson esté terminado
    def requires(self):
        return loadCleaned(bucket=self.bucket, date=self.date)

    # Esta sección indica lo que se va a correr:
    def run(self):
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Inicia la carga de los metadatos del extract...")
        # Lee nuevamente el archivo JSON que se subió al S3 bucket, para después obtener metadatos sobre la carga
        file_to_read = 'cleaned_data_04_01/metro_' + self.date + '.csv'

        creds = pd.read_csv("../../credentials_postgres.csv")
        creds_aws = pd.read_csv("../../credentials.csv")
        print("credenciales leídas correctamente")

        # Conexión a la S3
        print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
        print("Conexión Exitosa! :)")

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Conectando al S3 Bucket...")
        
        # Metemos el ec2 y el s3 actuales en un objeto, para poder obtener sus metadatos
        clientEC2 = boto3.client('ec2')
        # clientS3 = boto3.client('s3')
        print("Inicializados el EC2 y el S3")

        # El content object está especificando el objeto que se va a extraer del bucket S3
        # (la carga que se acaba de hacer desde la API)
        content_object = s3_resource.Object(self.bucket, file_to_read)
        print("s3 encontrada exitosamente")

        # Esta línea lee el archivo especificado en content_object
        file_content = pd.read_csv(content_object)    # content_object.get()['Body'].read().decode('utf-8') # Esto está de más
        print("contenido leído exitosamente")
        # Carga el Json content desde el archivo leído de la S3 Bucket
        #json_content = json.loads(file_content) # Esto está de más
        print("contenido cargado exitosamente")
        
        #función de EC2 para describir la instancia en la que se está trabajando
        information_metadata_ours = clientEC2.describe_instances()
        print("ec2 descrita correctamente")
        
        columnas_leidas = file_content # pd.read_csv('../../columnas_leidas.csv')
        print("csv leido correctamente")
        
        
        # Columns read indica la cantidad de columnas leidas
        columns_loaded = 196 # columnas_leidas['datos a cargar'][0]
        print("se cargaron:", columns_loaded, " columnas.")
        print(columns_loaded)
        fecha_ejecucion = pd.Timestamp.now()
        user = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('KeyName')
        fecha_json = self.date
        ip_ec2 = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('PrivateIpAddress')
        nombre_bucket = self.bucket
        status = 'Loaded'
        print("variables a cargar listas")
        
#        client.get('Reservations')[0].get('Instances')[0].get('KeyName')

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Conectandose a la instancia RDS con los datos CLEANED...")
        #Se conecta a la postgres en el RDS con las credenciales correspondientes
        connection = psycopg2.connect(user=creds.user[0],
                                      password=creds.password[0],
                                      host=creds.host[0],
                                      port=creds.port[0],
                                      database=creds.db[0])


        # Allows Python code to execute PostgreSQL command in a database session.
        cursor = connection.cursor()
        

        # Inserta los metadatos en la tabla metadata_extract
        text = "INSERT INTO cleaned.metadata  VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (
        user,fecha_ejecucion, fecha_json,ip_ec2, nombre_bucket, columns_loaded)
        print(text)
        
        cursor.execute(text) #Execute a database operation (query or command).

        
        connection.commit() # This method sends a COMMIT statement to the MySQL server, committing the current transaction. 
        cursor.close()# Close the cursor now (rather than whenever del is executed). The cursor will be unusable from this point forward
        connection.close() # For a connection obtained from a connection pool, close() does not actually close it but returns it to the pool and makes it available for subsequent connection requests.
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Carga de metadatos de Extract completada! :)")

        # para los outputs que no vamos a usar
        vacio = ' '
        data_vacia = {'vacio':[vacio]}
        pandas_a_csv = pd.DataFrame(data=data_vacia)
        pandas_a_csv(output().path, index=False)
        print("archivo creado correctamente")


    # Envía el output al S3 bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.csv". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)




##############################################################      SEMANTIC       ####################################