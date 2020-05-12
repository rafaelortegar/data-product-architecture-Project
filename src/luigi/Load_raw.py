import json
import luigi
import boto3
import datetime
import pandas as pd
from luigi.contrib.postgres import CopyToTable

from luigi.luigi_mas_completo import extractToJson

class copyToPostgres2(CopyToTable):
    """
    Esta funcion inserta los datos raw del s3
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'load_task_03_01'
    date = luigi.DateParameter(default=datetime.date.today())
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================



    #==============================================================================================================
    # Credenciales de acceso a la base de datos
    #==============================================================================================================
    print("Iniciando conexión a la S3 de datos...")
    creds = pd.read_csv("../../credentials_postgres.csv")
    creds_aws = pd.read_csv("../../credentials.csv")
    print("credenciales leídas correctamente")
    #==============================================================================================================
    
    
    
    #==============================================================================================================
    # Se inicializan los parámetros para la conexión a la bd
    #============================================================================================================== 
    user = creds.user[0]
    password = creds.password[0]
    database = creds.db[0]
    host = creds.host[0]
    #nombre de la tabla donde vamos a insertar
    table = 'raw.metro'
    #estructura de las columnas de la tabla
    columns=   [("fecha","TEXT"),
                ("ano","TEXT"),
                ("linea","TEXT"),
                ("estacion","TEXT"),
                ("afluencia","TEXT")]
    #==============================================================================================================


    #==============================================================================================================
    # llamamos la información del bucket
    #==============================================================================================================
    print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
    ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
    s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
    dev_s3_client = ses.client('s3')
    obj = s3_resource.Bucket(bucket) # Metemos el bucket S3 en una variable obj
    print("Conexión Exitosa! :)")
    
    file_to_read = 'extractToJson_task_01/metro_' + self.date + '.json'
    print("El archivo a leer es: ",file_to_read)
    #==============================================================================================================

    # leemos el df
    content_object = s3_resource.Object(bucket, file_to_read)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    print("Archivo cargado correctamente...")

    #metemos el df en un data frame
    f = pd.DataFrame(columns=["anio", "estacion", "fecha", "linea", "afluencia"])
    df = pd.read_json(r'json_content',encoding='utf-8', orient='values', lines=True)
    dfrec=df['records'][0]
    
    
    for x in range(len(list(dfrec))):
        json_str=json.dumps(dfrec[x])
        el_json=pd.read_json(json_str,orient='index',encoding='utf-8')
        a_ver = (el_json.loc['fields'][0])
        nuevo=pd.DataFrame(a_ver,index=[0])
        f=f.append(nuevo)
    
    #f.to_csv()
    def rows(self):
        for line in f:
            yield line
    

    #json_object = json.loads(json_file) for element in json_object: for value in json_object['Name_OF_YOUR_KEY/ELEMENT']: print(json_object['Name_OF_YOUR_KEY/ELEMENT']['INDEX_OF_VALUE']['VALUE'])

#    def rows(self):
#        r = [("test 1",z), ("test 2","45")]
#        for element in r:
#            yield element
#
#        z = str(self.x + self.x)
#        print("########### ", z)
#        r = [("test 1", z), ("test 2","45")]
#        for element in r:
#            yield element
    #==Codigo
    def rows(self):
        #Leemos el d
        with self.input()["infile2"].open('r') as infile:
            for line in infile:
                yield line.strip("\n").split("\t")

#    def rows(self):
#        r = [("test 1",z), ("test 2","45")]
#        for element in r:
#            yield element
#
#        z = str(self.x + self.x)
#        print("########### ", z)
#        r = [("test 1", z), ("test 2","45")]
#        for element in r:
#            yield element



    def requires(self):
        return  extractToJson(bucket = self.bucket, date = self.date)
            



    file_to_read = 'extractToJson_task_01/metro_' + self.date + '.json'
    # Conexión a la S3
    print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
    ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
    s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
    dev_s3_client = ses.client('s3')
    obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
    print("Conexión Exitosa! :)")
        
    f = pd.DataFrame(columns=["anio", "estacion", "fecha", "linea", "afluencia"])
#
#        for i in range(len(json_content['records'])):
#            a_row = pd.Series(
#                [json_content['records'][i]["fields"]["fecha"], json_content['records'][i]["fields"]["anio"],
#                 json_content['records'][i]["fields"]["linea"], json_content['records'][i]["fields"]["estacion"],
#                 int(json_content['records'][i]["fields"]["afluencia"])])
#            row_df = pd.DataFrame([a_row])
#            row_df.columns = ["fecha", "anio", "linea", "estacion", "afluencia"]
#            df = pd.concat([df, row_df], ignore_index=True)
