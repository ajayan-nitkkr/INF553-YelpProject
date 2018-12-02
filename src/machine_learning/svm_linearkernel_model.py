"""
Author: Ajay Anand
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from src.data_schema.feature_names import FeatureNames
from src.machine_learning.evaluation_metrics import EvaluationMetric
from src.machine_learning.split_data_train_test_validation import splitData
from src.data_analysis.plot_roc_auc import plot_roc,plot_precision_recall
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif


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


def training_svm(X_train, y_train):
    print("Training the data")
    y_train_new = np.array([item for sublist in np.array(y_train).tolist() for item in sublist])
    svm_clf = svm.SVC(kernel='linear')
    # svm_clf = DecisionTreeClassifier(criterion='entropy', max_depth=5)
    # svm_clf.fit(X_train, y_train_new)
    svm_clf.fit(X_train, y_train)
    print('Model:', svm_clf)
    print("Training completed...")
    return svm_clf


def predict_testdata(svm_clf, X_test):
    y_pred = svm_clf.predict(X_test)
    return y_pred

def do_feature_selection(X,y,kval):
    data_chi2_scores = SelectKBest(f_classif, k=kval).fit(X, y)
    selected_feature_indices=data_chi2_scores.get_support(indices=True)
    chi2_dataset = SelectKBest(f_classif, k=kval).fit_transform(X, y)
    return chi2_dataset


if __name__ == '__main__':

    # ########### CONSTRUCT DATA SET ############
    # df = construct_dataset()
    # ###########################################
    #
    # ############# DATA SLICING ################
    # X_train, X_test, y_train, y_test = divide_dataset(df)
    # # print(X_train,X_test,y_train,y_test)
    # ###########################################
    #
    # ################ TRAINING #################
    # svm_clf = training_svm(X_train, y_train)
    # ###########################################
    #
    # ################ PREDICTION ###############
    # y_pred = predict_testdata(svm_clf, X_test)
    # ###########################################
    #
    # ################ ACCURACY #################
    # evaluation_metric = EvaluationMetric()
    # # confusion_matrix = confusion_matrix(y_test.values, y_pred)
    # result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
    # print(result)
    # ###########################################

    """
    alpha_list = [0.01, 0.03, 0.05, 0.07, 0.1, 0.15]
    file_path = '../../resources/dataset/dataset_alpha_'
    for alpha in alpha_list:
        print("alpha:", alpha)
        X_train, X_val, X_test, y_train, y_val, y_test = splitData(
            filename= file_path + str(alpha) + '.csv')
        min_max_scaler = preprocessing.MinMaxScaler((0,1))
        X_train = min_max_scaler.fit_transform(X_train)
        X_test = min_max_scaler.transform(X_test)
        # print(len(X_train),len(X_val),len(X_test))

        svm_clf=svm.SVC(kernel='linear', probability=True)
        svm_clf.fit(X_train, y_train)
        y_pred = svm_clf.predict(X_test)

        evaluation_metric = EvaluationMetric()
        result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
        print(result)

        # probs = svm_clf.predict_proba(X_test)
        # probs = probs[:, 1]
        # plot_roc(y_test, probs)
        # plot_precision_recall(y_test, y_pred, probs)
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

    op=open('../../resources/Results/f_classif_svm.txt','w')
    for k in range(1,X.shape[1]+1):
        datasetX = do_feature_selection(X, y, k)


        ############# DATA SLICING ################

        X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=False)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=False)

        #X_train, X_val, X_test, y_train, y_val, y_test = splitData(filename='../../resources/dataset/final_lasvegas_dataset.csv')
        svm_clf = svm.SVC(kernel='linear', probability=True)
        svm_clf.fit(X_train, y_train)
        y_pred = svm_clf.predict(X_test)
        evaluation_metric = EvaluationMetric()
        result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
        ans="For top "+str(k)+" features, the result are "+ str(result)+" \n \n"
        op.write(ans)
        ###########################################


