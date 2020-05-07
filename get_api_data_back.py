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
import luigi.contrib.postgres
import os

class extractToJson(luigi.Task):
  """ Extrae los datos de la Base de datos y los guarda en un archivo con formato JSON"""
  task_name = "EL74"
  date = luigi.Parameter()
  bucket = luigi.Parameter()
  
  def requires(self):
    return None
  
  def insert_metadata(self, conn, inspections):
    params_string = "year={} month={} day={}".format(str(self.year), str(self.month), str(self.day))
    if len(inspections) > 0:
        inserted_vars = ",".join(inspections[0].keys())
    else:
        inserted_vars =  ""

    metadata = "'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}'".format(
        str(datetime.now(tz=None)),
        params_string,
        str(len(inspections)),
        get_os_user(),
        get_current_ip(),
        get_database_name(),
        "raw",
        get_database_table(),
        get_database_user(),
        inserted_vars,
        "etl"
    )
    with conn.cursor() as cur:
        cur.execute(
            'INSERT INTO raw.etl_metadata(executed_at, task_params, record_count, execution_user, source_ip, database_name, database_schema, database_table, database_user, vars, script_tag) VALUES (%s)'%metadata
        )
  
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
      json.dump(data_raw.json(), json_file)
    
    
  def output(self):
    output_path = "s3://{}/{}/metro_{}.json".\
        format(self.bucket, self.task_name, self.date)
    return luigi.contrib.s3.S3Target(path=output_path)
    

