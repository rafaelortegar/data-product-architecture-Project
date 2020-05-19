import luigi
import pandas as pd
from luigi import extractToJson
from luigi.Version2.metadataExtract import metadataExtract
from luigi import extract


class pruebaCopy(luigi.Task):
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
    creds = pd.read_csv("../../credentials_postgres.csv")
    creds_aws = pd.read_csv("../../credentials.csv")
    print('Credenciales leídas correctamente')
    host = creds.host[0]
    database = creds.db[0]
    user = creds.user[0]
    password = creds.password[0]
    port = creds.port[0]
    table = 'raw.pruebaCopy'
    columns = [("fecha", "TEXT"),("anio", "TEXT"), ("linea", "TEXT"), ("estacion", "TEXT"), ("afluencia", "TEXT")]
    
    def run(self):
        with self.input().open('r') as json_file:
            json_product = json.load(json_file)

    #=============================================================================================================

    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date) #, metadataExtract(bucket=self.bucket, date=self.date), testExtract(bucket=self.bucket, date=self.date), metadataTestExtract(bucket=self.bucket, date=self.date)




#    class ArtistToplistToDatabase(luigi.contrib.postgres.CopyToTable):
#    date_interval = luigi.DateIntervalParameter()
#    use_hadoop = luigi.BoolParameter()
#
#    host = "localhost"
#    database = "toplists"
#    user = "luigi"
#    password = "abc123"  # ;)
#    table = "top10"
#
#    columns = [("date_from", "DATE"),
#               ("date_to", "DATE"),
#               ("artist", "TEXT"),
#               ("streams", "INT")]
#
#    def requires(self):
#        return Top10Artists(self.date_interval, self.use_hadoop)