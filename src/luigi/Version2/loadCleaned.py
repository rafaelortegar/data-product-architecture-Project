import luigi
import logging
import psycopg2
import pandas as pd
from luigi.contrib.postgres import PostgresQuery, PostgresTarget


from copyToPostgres import copyToPostgres

logger = logging.getLogger('luigi-interface')

class loadCleaned(PostgresQuery):

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name='cleaned_data_04_01'
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
    port = creds.port[0]
    #=============================================================================================================
    def requires(self):
        return copyToPostgres(bucket=self.bucket, date=self.date)
    
    def run(self):
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()
        sql = """
        drop table if exists cleaned.metro cascade;
        create table cleaned.metro as (
            SELECT 
            fecha::DATE as fecha, 
            anio::int as ano, 
            linea::varchar as linea, 
            estacion::varchar as estacion,
            afluencia::int as afluencia
            from raw.metro
            );  
            """ 
        
        
        logger.info('Executing query from task: {name}'.format(name=self.task_name))
        cursor.execute(sql)

        # Update marker table
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
    luigi.loadCleaned()




































    def requires(self):
        return copyToPostgres(bucket = self.bucket, date=  self.date), metadataLoad(bucket = self.bucket, date=  self.date)
    
    
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

if __name__ == '__main__':
    luigi.loadCleaned()
    
    
#
#class PostgresQuery(rdbms.Query):
#    """
#    Template task for querying a Postgres compatible database
#
#    Usage:
#    Subclass and override the required `host`, `database`, `user`, `password`, `table`, and `query` attributes.
#    Optionally one can override the `autocommit` attribute to put the connection for the query in autocommit mode.
#
#    Override the `run` method if your use case requires some action with the query result.
#
#    Task instances require a dynamic `update_id`, e.g. via parameter(s), otherwise the query will only execute once
#
#    To customize the query signature as recorded in the database marker table, override the `update_id` property.
#    """
#    def run(self):
#        connection = self.output().connect()
#        connection.autocommit = self.autocommit
#        cursor = connection.cursor()
#        sql = self.query
#
#        logger.info('Executing query from task: {name}'.format(name=self.__class__))
#        cursor.execute(sql)
#
#        # Update marker table
#        self.output().touch(connection)
#
#        # commit and close connection
#        connection.commit()
#        connection.close()
#
#
#    def output(self):
#        """
#        Returns a PostgresTarget representing the executed query.
#
#        Normally you don't override this.
#        """
#        return PostgresTarget(
#            host=self.host,
#            database=self.database,
#            user=self.user,
#            password=self.password,
#            table=self.table,
#            update_id=self.update_id,
#            port=self.port
#        )
#        
#as
#asfaf
#