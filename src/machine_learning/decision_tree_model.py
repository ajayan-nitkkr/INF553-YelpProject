import numpy as np
from sklearn.svm import SVC
import pandas as pd
import math
from model_save_and_load import *
from split_data_train_test_validation import *
from evaluation_metrics import *
from sklearn.tree import DecisionTreeClassifier

global dtree
def read_dataset(filename):
    df=pd.DataFrame.from_csv(filename)
    return df

def get_training_test_set(filename):
    X_train,X_val,X_test,Y_train,Y_val,Y_test=splitData(filename)
    return X_train,X_val,X_test,Y_train,Y_val,Y_test

def train_DecisionTree(X_train,Y_train):
    '''
    Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.
    This class supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.
    '''
    dtree=DecisionTreeClassifier()
    dtree.fit(X_train,Y_train)
    return dtree
    #save_model(model,'svc_model.sav')
    
def predict_health_score(X_test):
    Y_pred=dtree.predict([X_test])
    return Y_pred

def get_eval_metrics(Y_test,Y_pred):
    #Use Ajay's API
    eval_obj=EvaluationMetric()
    eval_dict=eval_obj.get_evaluation_metrics(Y_test, Y_pred)
    return eval_dict

X_train,X_val,X_test,Y_train,Y_val,Y_test=get_training_test_set("../../resources/dataset/final_lasvegas_dataset.csv")
dtree = train_DecisionTree(X_train,Y_train)
Y_pred= predict_health_score(X_test)
eval_dict=get_eval_metrics(Y_test,Y_pred)
