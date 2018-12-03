
import logging
import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif

import math
from src.machine_learning.model_save_and_load import *
from src.machine_learning.split_data_train_test_validation import *
from src.machine_learning.evaluation_metrics import *
from src.data_analysis.plot_roc_auc import *
import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_schema.feature_names import FeatureNames
from src.machine_learning.evaluation_metrics import EvaluationMetric
from sklearn import preprocessing

logging.disable(logging.WARNING)
logging.disable(logging.CRITICAL)

def construct_dataset():
    file = '../../resources/dataset/final_lasvegas_dataset.csv'
    df = pd.read_csv(file)
    schema_obj = FeatureNames()
    # df = df[:100]
    df = df[[schema_obj.COL_RATING,
             schema_obj.COL_RESTAURANTS_PRICE_RANGE2,
             schema_obj.COL_INSPECTION_GRADE,
             schema_obj.COL_REVIEW_COUNT,
             schema_obj.COL_VIOLATIONS,
             schema_obj.COL_CURRENT_DEMERITS,
        schema_obj.COL_INSPECTION_DEMERITS]]
    df[schema_obj.COL_RESTAURANTS_PRICE_RANGE2] = df.apply(categorize_price_as_integer, axis=1)
    df[schema_obj.COL_INSPECTION_GRADE] = df.apply(categorize_grade_with_integer, axis=1)

    print("Dataset Shape:: ", df.shape)
    return df

def categorize_grade_with_integer(row):
    schema_obj = FeatureNames()
    attribute_name = schema_obj.COL_INSPECTION_GRADE

    modified_score = None
    if row[attribute_name] == 'A':
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


def divide_dataset(df):
    schema_obj = FeatureNames()
    X = df[[schema_obj.COL_RATING,
             schema_obj.COL_RESTAURANTS_PRICE_RANGE2,
             schema_obj.COL_REVIEW_COUNT,
             schema_obj.COL_VIOLATIONS,
             schema_obj.COL_CURRENT_DEMERITS,
             schema_obj.COL_INSPECTION_DEMERITS]]
    Y = df[[schema_obj.COL_INSPECTION_GRADE]]

    # print "Dividing data set into training and test set..."
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=62)

    positive_count = 0
    negative_count = 0
    for i in range(len(y_test.values)):
        if y_test.values[i][0] == 1:
            positive_count+=1
        else:
            negative_count+=1

#     print("Test data Shape:: ", X_test.shape, 'with ', \
#         'Positives =', positive_count, ', Negatives =', negative_count)

    return X_train, X_test, y_train, y_test



def get_training_val_test_set(filename):
    X_train,X_val,X_test,y_train,y_val,y_test=splitData(filename)
    return X_train,X_val,X_test,y_train,y_val,y_test

def train_LinearSVC(X_train,Y_train,max_iter,C):
    '''
    Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.
    This class supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.
    '''
    clf = LinearSVC(random_state=None, tol=1e-5, penalty="l2",class_weight="balanced",max_iter=max_iter,C=C)
    clf = CalibratedClassifierCV(clf)
    #hinge loss, L2 penalty, do dual=False when n_samples>n_features
    model = clf.fit(X_train, Y_train) 
    print('Model:', clf)
    print("Training completed...")
    return clf


def predict_testdata(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred


def predict_probabilities(svm_clf, X_test):
    probs = svm_clf.predict_proba(X_test)
    return probs

def do_feature_selection(X,y,kval):
    data_chi2_scores = SelectKBest(mutual_info_classif, k=kval).fit(X, y)
    selected_feature_indices=data_chi2_scores.get_support(indices=True)
    chi2_dataset = SelectKBest(mutual_info_classif, k=kval).fit_transform(X, y)
    return chi2_dataset

if __name__ == '__main__':

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

    C_list = [0.001, 0.01, 0.1, 1, 10]
    gamma_list = [0.001, 0.01, 0.1, 1]
    max_iter_list = [1, 10, 20, 50, 100, 200, 500, 1000]

    op=open('../../resources/Results/mutual_classif_linearsvc.txt','w')
    max_sensitivity = 0
    max_f1score = 0

    for k in range(1,X.shape[1]+1):
        datasetX = do_feature_selection(X, y, k)


        ############# DATA SLICING ################

        X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=False)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=False)

        #X_train, X_val, X_test, y_train, y_val, y_test = splitData(filename='../../resources/dataset/final_lasvegas_dataset.csv')

        ###########################################
        for C in C_list:
            for max_iter in max_iter_list:

                #print(len(X_train),len(X_val),len(X_test))
                clf=train_LinearSVC(X_train,y_train,max_iter,C)

                ################ PREDICTION ###############
                y_pred = predict_testdata(clf, X_test)
                ###########################################
                """
                ################ PREDICTION ###############
                probs = predict_probabilities(clf, X_test)
                ###########################################
                new_probs=[]
                for prob in probs:
                    new_probs.append(max(prob[0],prob[1]))
                ################ ROC GRAPHS ###############
                plot_roc(y_test,new_probs)
                plot_precision_recall(y_test,y_pred,new_probs)
                ###########################################
                """
                ################ ACCURACY #################
                evaluation_metric = EvaluationMetric()
                # confusion_matrix = confusion_matrix(y_test.values, y_pred)
                result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
                ans = "For top " + str(k) + " features," + " C:" + str(C)  + ", max_iter:" + str(max_iter) + \
                      ", sensitivity:" + str(result["sensitivity"]) + ", F1 score:" + str(
                    result["f1score"]) + "\n \n"
                op.write(ans)
                if result["sensitivity"] > max_sensitivity:
                    max_sensitivity = result["sensitivity"]
                    max_f1score = result["f1score"]

    print("max_sensitivity:", max_sensitivity)
    print("max_f1score:", max_f1score)
