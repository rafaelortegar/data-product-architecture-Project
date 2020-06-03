import numpy as np
import pandas as pd
from math import floor
from sklearn.linear_model import LogisticRegression
import feature_builder as fb

def rmse(y, pred):
    return(np.sqrt(np.mean((y-pred)**2)))
    
def categorias(x, y):
    n = len(x)
    z = np.array(x, dtype = str)
    q25 = np.quantile(y, 0.25)
    q75 = np.quantile(y, 0.75)
    z[x <= q25] = 'Bajo'
    z[(x >= q25) & (x <= q75)] = 'Normal'
    z[x >= q75] = 'Alto'
    return(z)

def modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc):

    y_ent1 = np.where(y_ent == cat, 1, 0)
    y_pr1 = np.where(y_pr == cat, 1, 0)

    modelo = LogisticRegression()
    modelo.fit(x_ent, y_ent1)

    pred = modelo.predict_proba(x_pr)[:,1]
    prob = pred.copy()
    pred = np.where(pred >= sc, 1, 0)
    TP = np.sum((pred == 1) & (y_pr1 == 1))
    TN = np.sum((pred == 0) & (y_pr1 == 0))
    FP = np.sum((pred == 1) & (y_pr1 == 0))
    FN = np.sum((pred == 0) & (y_pr1 == 1))

    accuracy = (TP+TN)/(TP+TN+FP+FN)

    precision = TP/(TP+FP)

    recall = TP/(TP+FN)

    a = {'modelo':modelo, 'pred':pred, 'prob':prob, 
         'accuracy':accuracy, 'precision':precision, 'recall':recall}
    return(a)

class ModelBuilder():
    def __init__(self):
        pass
    def build_model(self, x_mat):
        print("Entrando a ModelBuilder...")
        #indice_ent = x_mat['fecha'] <= '2019-11-30'
        x_mat.shape[0]*.80
        indice_ent = x_mat['fecha'] <= '2019-11-30'
        print("indice_ent...",indice_ent)
        
        variables_a_eliminar = ['fecha', 'ano', 'afluencia']
        print("variables_a_eliminar...",variables_a_eliminar)
        x_ent = x_mat[indice_ent].drop(variables_a_eliminar, axis = 1)
        print("x_ent...",x_ent)
        x_pr = x_mat[~indice_ent].drop(variables_a_eliminar, axis = 1)
        print("x_pr...",x_pr)
        y_ent = categorias(x_mat['afluencia'][indice_ent], 
                   x_mat['afluencia'][indice_ent])
        print("y_ent...",y_ent)
        y_pr = categorias(x_mat['afluencia'][~indice_ent], 
                  x_mat['afluencia'][indice_ent])
        print("y_pr...",y_pr)
        
        cat = 'Bajo'
        sc = 0.56
        modelo_bajo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['modelo']
        print("modelo_bajo...",modelo_bajo)
        
        cat = 'Normal'
        sc = 0.50
        modelo_normal = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['modelo']
        print("modelo_normal...",modelo_normal)

        cat = 'Alto'
        sc = 0.50
        modelo_alto = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['modelo']
        print("modelo_alto...",modelo_alto)
        
        modelos = [modelo_bajo, modelo_normal, modelo_alto]
        print("modelos...",modelos)
        
        return(modelos)
    
    
class ModelBuilderModelado():
    def __init__(self):
        pass
    def build_model(self, x_mat):
        print("Entrando a ModelBuilder...")
        #indice_ent = x_mat['fecha'] <= '2019-11-30'
        x_mat.shape[0]*.80
        indice_ent = x_mat['fecha'] <= '2019-11-30'
        print("indice_ent...",indice_ent)
        
        variables_a_eliminar = ['fecha', 'ano', 'afluencia']
        print("variables_a_eliminar...",variables_a_eliminar)
        x_ent = x_mat[indice_ent].drop(variables_a_eliminar, axis = 1)
        print("x_ent...",x_ent)
        x_pr = x_mat[~indice_ent].drop(variables_a_eliminar, axis = 1)
        print("x_pr...",x_pr)
        y_ent = categorias(x_mat['afluencia'][indice_ent], 
                   x_mat['afluencia'][indice_ent])
        print("y_ent...",y_ent)
        y_pr = categorias(x_mat['afluencia'][~indice_ent], 
                  x_mat['afluencia'][indice_ent])
        print("y_pr...",y_pr)
        
        
        cat = 'Bajo'
        sc = 0.56
        modelo1 = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)
        print('modelo1',modelo1)
        
        cat = 'Normal'
        sc = 0.50
        modelo2 = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)
        print('modelo1',modelo2)
        
        cat = 'Alto'
        sc = 0.50
        modelo2 = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)
        print('modelo1',modelo2)
        
        
        cat = 'Bajo'
        sc = 0.56
        modelo_bajo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['modelo']
        print("modelo_bajo...",modelo_bajo)
        
        cat = 'Normal'
        sc = 0.50
        modelo_normal = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['modelo']
        print("modelo_normal...",modelo_normal)

        cat = 'Alto'
        sc = 0.50
        modelo_alto = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['modelo']
        print("modelo_alto...",modelo_alto)
        
        modelos = [modelo_bajo, modelo_normal, modelo_alto]
        print("modelos...",modelos)
        
        cat = 'Bajo'
        sc = 0.56
        prob_modelo_bajo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc=.56)['prob']
        accuracy_modelo_bajo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc=.56)['accuracy']
        precision_modelo_bajo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc=.56)['precision']
        recall_modelo_bajo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc=.56)['recall']
        
        cat = 'Normal'
        sc = 0.50
        prob_modelo_normal = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['prob']
        accuracy_modelo_normal = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['accuracy']
        precision_modelo_normal = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['precision']
        recall_modelo_normal = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['recall']
        
        cat = 'Alto'
        sc = 0.50
        prob_modelo_alto = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['prob']
        accuracy_modelo_alto = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['accuracy']
        precision_modelo_alto = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['precision']
        recall_modelo_alto = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)['recall']
        
        probs = [prob_modelo_bajo, prob_modelo_normal, prob_modelo_alto]
        print("probs...",probs)
        
        accs = [accuracy_modelo_bajo, accuracy_modelo_normal, accuracy_modelo_alto]
        print("accuracy's...",accs)
        
        precs = [precision_modelo_bajo, precision_modelo_normal, precision_modelo_alto]
        print("precisions...",precs)
        
        recs = [recall_modelo_bajo, recall_modelo_normal, recall_modelo_alto]
        print("recalls...",recs)
        
        return(modelos,probs,accs,precs,recs)

