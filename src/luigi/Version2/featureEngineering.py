import luigi
import logging
import psycopg2
import sqlalchemy

import pandas.io.sql as psql
import pandas as pd

from sqlalchemy import create_engine
from luigi.contrib.postgres import PostgresQuery, PostgresTarget

import feature_builder as fb
from loadCleaned import loadCleaned

logger = logging.getLogger('luigi-interface')
##############################################################      SEMANTIC       ####################################

############################################################## FEATURE ENGINEERING ####################################
#X['Fecha'] = pd.to_datetime(X['Fecha'])     #IFE


#X['Dia'] = pd.DatetimeIndex(X['Fecha']).day.astype('object')
#X['Mes'] = pd.DatetimeIndex(X['Fecha']).month.astype('object')
#X['Dia_Semana'] = (pd.DatetimeIndex(X['Fecha']).weekday + 1).astype('object') #FFE
#

#variables_categoricas = X.dtypes.pipe(lambda x: x[x == 'object']).index     #Sí va en FE
#
#num_cols = X.dtypes.pipe(lambda x: x[x != 'object']).index
#for x in num_cols:
#    imp = SimpleImputer(missing_values = np.nan, strategy = 'median')
#    imp.fit(np.array(X[x]).reshape(-1, 1))
#    X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))
#
#nominal_cols = X.dtypes.pipe(lambda x: x[x == 'object']).index
#for x in nominal_cols:
#    imp = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
#    imp.fit(np.array(X[x]).reshape(-1, 1))
#    X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))
#
#x_mat = pd.get_dummies(X, columns = variables_categoricas, drop_first = True)   #FFE


class featureEngineering(PostgresQuery):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket. Requires extractToJson
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'feature_engineering_05_01'
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
    table = 'semantic.metro'
    port = creds.port[0]
    query = """SELECT * FROM semantic.metro"""
    #=============================================================================================================
    # Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    def requires(self):
        return loadCleaned(bucket=self.bucket, date=self.date) # , metadataCleaned(bucket = self.bucket, date=  self.date)


    def run(self):
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()
        
        df = psql.read_sql('SELECT * FROM cleaned.metro;', connection)
        df2 = fb.FeatureBuilder()
        df2 = df2.featurize(df)
        print(df2.shape)
        
        engine = create_engine('postgresql+psycopg2://postgres:12345678@database-1.cqtrfcufxibu.us-west-2.rds.amazonaws.com:5432/dpa')
        #user,password,host,port,db
        #postgres,12345678,database-1.cqtrfcufxibu.us-west-2.rds.amazonaws.com,5432,dpa
        table_name= self.table
        scheme='semantic'
        df2.to_sql("semantic.metro", con=engine, schema='semantic',if_exists='replace')
        print(psql.read_sql('SELECT * FROM semantic.metro LIMIT 10;', connection))
        
        logger.info('Executing query from task: {name}'.format(name=self.task_name))
#        
#        for row in df2:
#            tupla = [tuple(x) for x in df2.values]
#            print(tupla)
#            query = """INSERT INTO {} VALUES {};""".format(self.table,tupla)
#            sql = query
#            cursor.execute(sql)
#        
        #logger.info('Executing query from task: {name}'.format(name=self.task_name))
        #cursor.execute(sql)
        #print(type(bd))
        #print(bd)
        
        #df = pd.DataFrame(data=bd)
        
#        df = psql.read_sql(self.query, connection)
#        df2 = fb()
#        df2 = df2.featurize(df)
#        print(df2.shape)
#        #engine = create_engine('postgresql+psycopg2://postgres:12345678@database-1.cqtrfcufxibu.us-west-2.rds.amazonaws.com:5432/dpa')
        #df2 es el output
        
        # Update marker table
#        with self.output().open('w') as output_file:
#            output_file.write('algo')
        

        #df2.to_sql(self.output,connection)
        self.output().touch(connection)

        # commit and close connection
        connection.commit()
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
    luigi.featureEngineering()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #def run(self):
#
    #    # Lee nuevamente el archivo JSON que se subió al S3 bucket, para después obtener metadatos sobre la carga
    #    archivoquenosirve = 'cleaned_data_04_01/metro_' + self.date + '.csv'
#
    #    creds = pd.read_csv("../../credentials_postgres.csv")
    #    creds_aws = pd.read_csv("../../credentials.csv")
    #    print("credenciales leídas correctamente")
#
    #    # Conexión a la S3
    #    print("Iniciando la conexión con el recurso S3 que contiene los datos extraídos...")
    #    ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
    #    s3_resource = ses.resource('s3') # Inicialzamos e recursoS3
    #    obj = s3_resource.Bucket(self.bucket) # Metemos el bucket S3 en una variable obj
    #    print("Conexión Exitosa! :)")
#
    #    content_object = s3_resource.Object(self.bucket, archivoquenosirve)
    #    #file_content = pd.read_csv(content_object) 
    #    print("s3 encontrada exitosamente")
#
    #    connection = psycopg2.connect(user=creds.user[0],
    #                                      password=creds.password[0],
    #                                      host=creds.host[0],
    #                                      port=creds.port[0],
    #                                      database=creds.db[0])
    #    cursor = connection.cursor()
    #    df = psql.read_sql('SELECT * FROM cleaned.metro', connection)
    #    #dummies=pd.get_dummies(df["ano"],prefix='y')
    #    #df=pd.concat([df,dummies],axis=1)
    #    #dummies=pd.get_dummies(df["linea"],prefix='l')
    #    #df=pd.concat([df,dummies],axis=1)
    #    #print(df.columns)
    #    df2 = FeatureBuilder()
    #    df2 = df2.featurize(df)
    #    print(df2.shape)
    #    #sqlalchemy engine to psycopg2
    #    #dialect+driver://username:password@host:port/database
    #    engine = create_engine('postgresql+psycopg2://postgres:12345678@database-1.cqtrfcufxibu.us-west-2.rds.amazonaws.com:5432/dpa')
    #    #user,password,host,port,db
    #    #postgres,12345678,database-1.cqtrfcufxibu.us-west-2.rds.amazonaws.com,5432,dpa
#
    #    table_name='semantic.metro'
    #    scheme='semantic'
    #    df2.to_sql("semantic.metro", con=engine, schema='semantic',if_exists='replace')
    #    print(psql.read_sql('SELECT * FROM semantic.metro LIMIT 10;', connection))
    #    
    #    # para los outputs que no vamos a usar
    #    vacio = ' '
    #    data_vacia = {'vacio':[vacio]}
    #    pandas_a_csv = pd.DataFrame(data=data_vacia)
    #    pandas_a_csv.to_csv(self.output().path, index=False)
    #    print("archivo creado correctamente")    
#
#===#====
#   #     df2.to_sql("metro", engine, schema='semantic',if_exists='replace')
    #    
#
    #
    ## Envía el output al S3 bucket especificado con el nombre de output_path
    #def output(self):
    #    output_path = "s3://{}/{}/metro_{}.csv". \
    #        format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
    #    return luigi.contrib.s3.S3Target(path=output_path)
#
    ## Esta sección indica lo que se va a correr:
    ## Indica que para iniciar el proceso de carga de metadatos requiere que el task de extractToJson esté terminado
    ##def requires(self):
    ##    return create_semantic_schema(bucket=self.bucket, date=self.date)
#
#if __name__ == '__main__':
#    luigi.runAll()