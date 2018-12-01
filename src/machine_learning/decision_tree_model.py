import numpy as np
from sklearn.svm import SVC
import pandas as pd
import math
from model_save_and_load import *
from split_data_train_test_validation import *
from evaluation_metrics import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif
from sklearn import preprocessing


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

def do_feature_selection(X,y,kval):
    data_chi2_scores = SelectKBest(chi2, k=kval).fit(X, y)
    selected_feature_indices=data_chi2_scores.get_support(indices=True)
    chi2_dataset = SelectKBest(mutual_info_classif, k=kval).fit_transform(X, y)
    return chi2_dataset


X_train,X_val,X_test,Y_train,Y_val,Y_test=get_training_test_set("../../resources/dataset/final_lasvegas_dataset.csv")
dtree = train_DecisionTree(X_train,Y_train)
Y_pred= predict_health_score(X_test)
eval_dict=get_eval_metrics(Y_test,Y_pred)


"""
########### CONSTRUCT DATA SET ############
    df = pd.read_csv('../../resources/dataset/final_lasvegas_dataset_v4.csv')
    X = df.drop(['inspection_grade'], axis=1)
    y = df[['inspection_grade']]
    y.replace('A', 0, inplace=True)
    y.replace('B', 1, inplace=True)
    y.replace('C', 1, inplace=True)
    y.replace('D', 1, inplace=True)
    y.replace('E', 1, inplace=True)
    min_max_scaler = preprocessing.MinMaxScaler((0, 1))
    X = min_max_scaler.fit_transform(X)

    op=open('../../resources/Results/mutual_info_decisionTrees.txt','w')
    for k in range(1,X.shape[1]+1):
        datasetX = do_feature_selection(X, y, k)


        ############# DATA SLICING ################

        X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=True)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=True)

        #X_train, X_val, X_test, y_train, y_val, y_test = splitData(filename='../../resources/dataset/final_lasvegas_dataset.csv')

        ###########################################



"""