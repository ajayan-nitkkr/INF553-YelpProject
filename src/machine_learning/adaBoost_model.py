import time
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from INF553_YelpProject.src.data_schema.feature_names import FeatureNames
from INF553_YelpProject.src.machine_learning.evaluation_metrics import EvaluationMetric
from INF553_YelpProject.src.data_analysis.plot_roc_auc import plot_roc, plot_precision_recall
from INF553_YelpProject.src.machine_learning.split_data_train_test_validation import splitData
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif

import logging
logging.disable(logging.WARNING)
logging.disable(logging.CRITICAL)

def construct_dataset():
    file = '../../resources/dataset/final_lasvegas_dataset_v4.csv'
    
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

def predict_testdata(model, X_test):
    y_pred = model.predict(X_test)
    return y_pred

def do_feature_selection(X,y,kval):
    
#     data_chi2_scores = SelectKBest(chi2, k=kval).fit(X, y)
    data_chi2_scores = SelectKBest(f_classif, k=kval).fit(X, y)
    selected_feature_indices=data_chi2_scores.get_support(indices=True)
    chi2_dataset = SelectKBest(f_classif, k=kval).fit_transform(X, y)
    return chi2_dataset


def run_adaBoost_model():
    """
    df = construct_dataset()
#     X_train, X_test, y_train, y_test = divide_dataset(df)
    
    X_train,X_val,X_test,y_train,y_val,y_test = splitData(filename = '../../resources/dataset/final_lasvegas_dataset_v4.csv')
    
#     X_train,X_val,X_test,y_train,y_val,y_test = splitData(filename = '../../resources/dataset/dataset_alpha_0.1.csv')
    
    min_max_scaler = preprocessing.MinMaxScaler((0,1))
    X_train = min_max_scaler.fit_transform(X_train)
    X_test = min_max_scaler.transform(X_test)

    adaboost_model = AdaBoostClassifier( DecisionTreeClassifier(max_depth=5), n_estimators = 30, learning_rate=0.1)
    adaboost_model.fit(X_train, np.ravel(y_train))
    
    y_pred = predict_testdata(adaboost_model, X_test)
    
    evaluation_metric = EvaluationMetric()
  
    result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
  
    print(result)
    probs = adaboost_model.predict_proba(X_test)
    probs = probs[:, 1]
    plot_roc(y_test, probs)
    plot_precision_recall(y_test, y_pred, probs)
    
#     plot_roc(y_test, y_pred)
    
    return
    """
    ########## CONSTRUCT DATA SET ############
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
    
    max_recall_f1 = -float('inf') 
   
    op=open('../../resources/Results/f_classif_adaboost1.txt','w')
    for k in range(1, X.shape[1]+1):
        datasetX = do_feature_selection(X, y, k)


        ############# DATA SLICING ################

        X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=True)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=True)

        #X_train, X_val, X_test, y_train, y_val, y_test = splitData(filename='../../resources/dataset/final_lasvegas_dataset.csv')

        ###########################################
        adaboost_model = AdaBoostClassifier(DecisionTreeClassifier(max_depth = 7), n_estimators=30, learning_rate=0.1)
        adaboost_model.fit(X_train, np.ravel(y_train))

        y_pred = predict_testdata(adaboost_model, X_test)

        evaluation_metric = EvaluationMetric()

        result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
        ans = "For top " + str(k) + " features, the result are " + str(result) + " \n \n"
        op.write(ans)
        
#         if(result['sensitivity']+ result['f1score'] > max_recall_f1):
        if(result['sensitivity'] > max_recall_f1):
            
            max_recall_f1 = result['sensitivity']
            max_k_val = k
#         if (k == 7):
#             print(result)
#             probs = adaboost_model.predict_proba(X_test)
#             probs = probs[:, 1]
#             plot_roc(y_test, probs)
#             plot_precision_recall(y_test, y_pred, probs)
    
    print(max_k_val)

if __name__=='__main__':   
    
    start=time.time()
    
    run_adaBoost_model() 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  