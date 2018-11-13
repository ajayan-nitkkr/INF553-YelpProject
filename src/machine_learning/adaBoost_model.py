import time
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from INF553_YelpProject.src.data_schema.feature_names import FeatureNames
from INF553_YelpProject.src.machine_learning.evaluation_metrics import EvaluationMetric
from INF553_YelpProject.src.data_analysis.plot_roc_auc import plot_roc

#############################
########## Ajay's code for getting train and test dataset

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
             schema_obj.COL_RESTAURANTS_PRICE_RANGE2]]
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

def run_adaBoost_model():
    
    df = construct_dataset()
    X_train, X_test, y_train, y_test = divide_dataset(df)
    
    adaboost_model = AdaBoostClassifier( DecisionTreeClassifier(max_depth=2), n_estimators = 30, learning_rate=1)
    adaboost_model.fit(X_train, np.ravel(y_train))
      
    y_pred = predict_testdata(adaboost_model, X_test)
    evaluation_metric = EvaluationMetric()
  
    result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
  
    print(result)
    plot_roc(y_test, y_pred)
    
    return

if __name__=='__main__':   
    
    start=time.time()
    
    run_adaBoost_model() 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  