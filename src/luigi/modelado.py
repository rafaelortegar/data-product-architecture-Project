import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

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

def pred_final(pred_bajo, prob_bajo, 
               pred_normal, prob_normal, 
               pred_alto, prob_alto):

    n = len(pred_normal)
    pred_final = np.array(pred_normal, dtype = str)
    pred = pd.DataFrame({'Bajo':pred_bajo, 
                         'Normal':pred_normal, 
                         'Alto':pred_alto})
    prob = pd.DataFrame({'Bajo':prob_bajo, 
                         'Normal':prob_normal, 
                         'Alto':prob_alto})
    
    for i in np.arange(1, n+1):
        if pred.iloc[i-1, :].sum() == 1:
            pred_final[i-1] = pred.iloc[i-1, :].idxmax()
        else:
            pred_final[i-1] = prob.iloc[i-1, :].idxmax()
    
    return(pred_final)

class ModelBuilder():
    def __init__(self):
        pass
    def build_model(self, x_mat):
        indice_ent = x_mat['fecha'] <= '2019-11-30'
        
        variables_a_eliminar = ['fecha', 'anio', 'afluencia']

        x_ent = x_mat[indice_ent].drop(variables_a_eliminar, axis = 1)
        x_pr = x_mat[~indice_ent].drop(variables_a_eliminar, axis = 1)
        y_ent = categorias(x_mat['afluencia'][indice_ent], 
                   x_mat['afluencia'][indice_ent])
        y_pr = categorias(x_mat['afluencia'][~indice_ent], 
                  x_mat['afluencia'][indice_ent])
        
        cat = 'Bajo'
        sc = 0.56
        modelo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)

        pred_bajo = modelo['pred']
        prob_bajo = modelo['prob']

        cat = 'Normal'
        sc = 0.50
        modelo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)

        pred_normal = modelo['pred']
        prob_normal = modelo['prob']

        cat = 'Alto'
        sc = 0.50
        modelo = modelo_cat(cat, x_ent, y_ent, x_pr, y_pr, sc)

        pred_alto = modelo['pred']
        prob_alto = modelo['prob']

        pred_f = pred_final(pred_bajo, prob_bajo, 
               pred_normal, prob_normal, 
               pred_alto, prob_alto)
        return(pred_f)

