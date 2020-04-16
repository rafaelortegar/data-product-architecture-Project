# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parametro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=mge luigi --module ex3_luigi S3Task --local-scheduler ...
import requests
import pandas
import json
import luigi
import boto3
import pandas as pd
import luigi.contrib.s3
import os
import pyspark
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages "org.apache.hadoop:hadoop-aws:2.7.3" pyspark-shell'
from pyspark.sql.types import *
from pyspark.context import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.session import SparkSession
from pyspark.sql import Row
import s3fs

sc = SparkContext('local')
spark = SparkSession(sc)


class extractToJson(luigi.Task):
  task_name = "raw"
  date = luigi.Parameter()
  bucket = luigi.Parameter()
  
  def requires(self):
    return None
  
  def run(self):
    ses = boto3.session.Session(profile_name='gabster', region_name='us-west-2')
    s3_resource = ses.resource('s3')
    obj = s3_resource.Bucket(self.bucket)
    
    data_raw = requests.get(f"https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=afluencia-diaria-del-metro-cdmx&rows=10000&sort=-fecha&refine.fecha={self.date}")
    
    # data_raw.status_code
    # data_raw.headers['content-type']
    # data_raw.headers['Date']
    # data_raw.json()
    
    with self.output().open('w') as json_file:
      json.dump(data_raw.json()['records'], json_file)
    
    
  def output(self):
    output_path = "s3://{}/{}/metro_{}.json".\
        format(self.bucket, self.task_name, self.date)
    return luigi.contrib.s3.S3Target(path=output_path)
    

class processToParquet(luigi.Task):
  task_name = "parquet"
  date = luigi.Parameter()
  bucket = luigi.Parameter()
  
  def requires(self):
    return extractToJson(bucket = self.bucket, date=self.date)
  
  def output(self):
    output_path = "s3://{}/{}/metro.parquet".\
        format(self.bucket, self.task_name, self.date)
    return luigi.contrib.s3.S3Target(path=output_path)

  def run(self):
    ses = boto3.session.Session(profile_name='gabster', region_name='us-west-2')
    s3_resource = ses.resource('s3')
    sc = SparkContext.getOrCreate()
    sc._jsc.hadoopConfiguration().set("fs.s3.impl", "org.apache.hadoop.fs.s3.S3FileSystem")
    sc._jsc.hadoopConfiguration().set('fs.s3.awsAccessKeyId', 'AKIA2VS63DHC2HH3O2X5')
    sc._jsc.hadoopConfiguration().set('fs.s3.awsSecretAccessKey', '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')
    spark = SQLContext(sc)

    data_raw = spark.read.json(self.input().path)
    data_raw.write.parquet(self.output().path)
  

