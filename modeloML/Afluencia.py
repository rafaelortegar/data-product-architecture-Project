import os
directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala'
os.chdir(directorio)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

X = pd.read_csv('afluencia-diaria-del-metro-cdmx.csv')

X.head()

def factor(x):
    return(x.astype('category'))

def rmse(y, pred):
    return(np.sqrt(np.mean((y-pred)**2)))

X['Fecha'] = pd.to_datetime(X['Fecha'])
#X['Linea'] = factor(X['Linea'])
#X['Estacion'] = factor(X['Estacion'])
X['Dia'] = pd.DatetimeIndex(X['Fecha']).day
X['Mes'] = pd.DatetimeIndex(X['Fecha']).month
X['Dia_Semana'] = pd.DatetimeIndex(X['Fecha']).weekday + 1

indice_ent = X['Fecha'] <= '2019-11-30'

variables_a_eliminar = ['Fecha', 'Año', 'Afluencia']

variables_categoricas = X.dtypes.pipe(lambda x: x[x == 'object']).index

x_mat = pd.get_dummies(X, columns = variables_categoricas, drop_first = True)

x_ent = x_mat[indice_ent].drop(variables_a_eliminar, axis = 1)
x_pr = x_mat[~indice_ent].drop(variables_a_eliminar, axis = 1)
y_ent = x_mat['Afluencia'][indice_ent]
y_pr = x_mat['Afluencia'][~indice_ent]

modelo = LinearRegression()
modelo.fit(x_ent, y_ent)

pred = modelo.predict(x_pr)
rmse(y_pr, pred)

