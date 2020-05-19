import luigi
import logging
import psycopg2
import pandas as pd
import pandas.io.sql as psql
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
    table = 'cleaned.metro'
    port = creds.port[0]
    query = """
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
    
    #=============================================================================================================
    def requires(self):
        return copyToPostgres(bucket=self.bucket, date=self.date)
    
    def run(self):
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()
        sql = self.query
        
        logger.info('Executing query from task: {name}'.format(name=self.task_name))
        cursor.execute(sql)

        #sección añadida despues de que corría
#        creds2 = pd.read_csv("../../../credentials_postgres.csv")
#        connection2 = psycopg2.connect(user=creds2.user[0],
#                                  password=creds2.password[0],
#                                  host=creds2.host[0],
#                                  port=creds2.port[0],
#                                  database=creds2.db[0])
#        df = psql.read_sql('SELECT * FROM cleaned.metro;', connection2)
#        total_final = len(df)
#        csv_leido = pd.read_csv('../../../columnas_leidas.csv')
#        csv_leido['total_final'][0] = total_final
#        csv_leido.to_csv('../../../columnas_leidas.csv')
#        connection2.close()       
        #fin de sección        
        
        # Update marker table
        self.output().touch(connection)

        # commit and close connection
        connection.commit()
        connection.close()
        
        
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

if __name__ == '__main__':
    luigi.loadCleaned()
