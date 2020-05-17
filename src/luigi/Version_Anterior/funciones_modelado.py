from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd


def rmse(y, pred):
    return(np.sqrt(np.mean((y-pred)**2)))

def categorias(x, y): #Al empezar modelado #EN EL MODELADO
    n = len(x) #EN EL MODELADO
    z = np.array(x, dtype = str) #EN EL MODELADO
    q25 = np.quantile(y, 0.25) #EN EL MODELADO
    q75 = np.quantile(y, 0.75) #EN EL MODELADO
    z[x <= q25] = 'Bajo' #EN EL MODELADO
    z[(x >= q25) & (x <= q75)] = 'Normal' #EN EL MODELADO
    z[x >= q75] = 'Alto' #EN EL MODELADO
    return(z) #EN EL MODELADO

    
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




