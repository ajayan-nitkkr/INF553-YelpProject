
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.svm import LinearSVC

import math
from src.machine_learning.model_save_and_load import *
from src.machine_learning.split_data_train_test_validation import *
from src.machine_learning.evaluation_metrics import *

import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_schema.feature_names import FeatureNames
from src.machine_learning.evaluation_metrics import EvaluationMetric



def construct_dataset():
    file = '../../resources/dataset/final_lasvegas_dataset.csv'
    df = pd.read_csv(file)
    schema_obj = FeatureNames()
    # df = df[:100]
    df = df[[schema_obj.COL_RATING,
             schema_obj.COL_RESTAURANTS_PRICE_RANGE2,
             schema_obj.COL_INSPECTION_GRADE]]
    df[schema_obj.COL_RESTAURANTS_PRICE_RANGE2] = df.apply(categorize_price_as_integer, axis=1)
    df[schema_obj.COL_INSPECTION_GRADE] = df.apply(categorize_grade_with_integer, axis=1)

    print("Dataset Shape:: ", df.shape)
    return df


def divide_dataset(df):
    schema_obj = FeatureNames()
    X = df[[schema_obj.COL_RATING,
             schema_obj.COL_RESTAURANTS_PRICE_RANGE2]]
    Y = df[[schema_obj.COL_INSPECTION_GRADE]]

    # print "Dividing data set into training and test set..."
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

    positive_count = 0
    negative_count = 0
    for i in range(len(y_test.values)):
        if y_test.values[i][0] == 1:
            positive_count+=1
        else:
            negative_count+=1

    print("Test data Shape:: ", X_test.shape, 'with ', \
        'Positives =', positive_count, ', Negatives =', negative_count)

    return X_train, X_test, y_train, y_test


# def categorize_score_attribute_with_boolean(row):
#     # attribute_name = 'SCORE'
#     schema_obj = FeatureNames()
#     attribute_name = schema_obj.COL_INSPECTION_SCORE
#
#     modified_score = None
#     if row[attribute_name] > 90 and row[attribute_name] <= 100: modified_score = 0
#     elif row[attribute_name] > 0 and row[attribute_name] <= 90: modified_score = 1
#     return modified_score


def categorize_grade_with_integer(row):
    schema_obj = FeatureNames()
    attribute_name = schema_obj.COL_INSPECTION_GRADE

    modified_score = None
    if row[attribute_name] == 'A' :
        modified_score = 0
    else:
        modified_score = 1
    return modified_score


def categorize_price_as_integer(row):
    schema_obj = FeatureNames()
    attribute_name = schema_obj.COL_RESTAURANTS_PRICE_RANGE2
    modified_price = None

    if row[attribute_name] == "Null": modified_price = -1
    else: modified_price = int(row[attribute_name])
    return modified_price



def get_training_val_test_set(filename):
    X_train,X_val,X_test,y_train,y_val,y_test=splitData(filename)
    return X_train,X_val,X_test,y_train,y_val,y_test

def train_LinearSVC(X_train,Y_train):
    '''
    Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.
    This class supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.
    '''
    clf = LinearSVC(random_state=0, tol=1e-5)
    #hinge loss, L2 penalty, do dual=False when n_samples>n_features
    model = clf.fit(X_train, Y_train) 
    print('Model:', clf)
    print("Training completed...")
    return clf


def predict_testdata(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred


if __name__ == '__main__':

    ########### CONSTRUCT DATA SET ############
    df = construct_dataset()
    ###########################################

    ############# DATA SLICING ################
    X_train, X_test, y_train, y_test = divide_dataset(df)
    # print(X_train,X_test,y_train,y_test)
    ###########################################

    ################ TRAINING #################
    clf = train_LinearSVC(X_train, y_train)
    ###########################################

    ################ PREDICTION ###############
    y_pred = predict_testdata(clf, X_test)
    ###########################################

    ################ ACCURACY #################
    evaluation_metric = EvaluationMetric()
    # confusion_matrix = confusion_matrix(y_test.values, y_pred)
    result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
    print(result)
    ###########################################