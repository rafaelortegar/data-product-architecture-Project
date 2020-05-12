import numpy as np
import pandas as pd
import feature_builder as fb
import modelado
import prediction

#Leer los archivos

X = pd.read_csv('afluencia-diaria-del-metro-cdmx.csv')
X.columns = ['fecha', 'anio', 'linea', 'estacion', 'afluencia']
X_nuevas = X.iloc[[-3, -2, -1], :]
X_nuevas.columns = ['fecha', 'anio', 'linea', 'estacion', 'afluencia']

#Feature Engineering

x_mat = fb.FeatureBuilder()
x_mat = x_mat.featurize(X)  #X sería la matriz que extraen de postgres
model_matrix = fb.create_model_matrix(X)  #Esta función se guarda en un pickle

#Modelado

modelos = modelado.ModelBuilder()
modelos = modelos.build_model(x_mat)  #Esta variable se guarda en un pickle

#Prediction

#Se cargan model_matrix y modelos

pred_f = prediction.Predict()
pred_f = pred_f.predict(X_nuevas, modelos, model_matrix)
pred_f

