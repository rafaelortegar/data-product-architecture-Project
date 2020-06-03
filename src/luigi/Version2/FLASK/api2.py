from flask import Flask
import pandas as pd
from io import StringIO
import json
import boto3

app = Flask(__name__)

@app.route('/')
def root():
    return "API DE Predicciones de Afluencia del metro CDMX"

@app.route('/user/<string:username>')
def show_user_profile(username):
    return "Hello user {}".format(username)


@app.route('/date/<string:date>')
def show_user2_profile(date):
    year = date[:4]
    month = date[4:6]
    day = date[6:]


    ses = boto3.session.Session(profile_name='rafael-dpa-proj', region_name='us-west-2')
    s3_resource = ses.resource('s3')

    obj = s3_resource.Object("dpaprojs3", "predictionMetro_task_07_01/metro_{}-{}-{}.csv".format(str(year), str(month).zfill(2), str(day).zfill(2)))
    file_content = obj.get()['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(file_content))
    dfJson = df.to_json(orient='table')

    
    return dfJson
@app.route('/datecsv/<string:date>')
def show_user2_profile(date):
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    ses = boto3.session.Session(profile_name='rafael-dpa-proj', region_name='us-west-2')
    s3_resource = ses.resource('s3')

    obj = s3_resource.Object("dpaprojs3", "predictionMetro_task_07_01/metro_{}-{}-{}.csv".format(str(year), str(month).zfill(2), str(day).zfill(2)))
    file_content = obj.get()['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(file_content))
    return df

if __name__ == "__main__":
    app.run()
