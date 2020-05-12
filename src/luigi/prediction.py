import numpy as np
import pandas as pd

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

class Predict():
    def __init__(self):
        pass
    def predict(self, X_nuevas, modelos, model_matrix):
        x_nuevas = model_matrix(X_nuevas)
        
        pred = modelos[1-1].predict_proba(x_nuevas)[:,1]
        prob = pred.copy()
        pred = np.where(pred >= 0.56, 1, 0)
        pred_bajo = pred.copy()
        prob_bajo = prob.copy()
        
        pred = modelos[2-1].predict_proba(x_nuevas)[:,1]
        prob = pred.copy()
        pred = np.where(pred >= 0.50, 1, 0)
        pred_normal = pred.copy()
        prob_normal = prob.copy()
        
        pred = modelos[3-1].predict_proba(x_nuevas)[:,1]
        prob = pred.copy()
        pred = np.where(pred >= 0.50, 1, 0)
        pred_alto = pred.copy()
        prob_alto = prob.copy()
        
        pred_f = pred_final(pred_bajo, prob_bajo, 
                            pred_normal, prob_normal, 
                            pred_alto, prob_alto)

        return(pred_f)

