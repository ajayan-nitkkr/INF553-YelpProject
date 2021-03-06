import time
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif
# from INF553_YelpProject.src.data_schema.feature_names import FeatureNames
# from INF553_YelpProject.src.machine_learning.evaluation_metrics import EvaluationMetric
# from INF553_YelpProject.src.data_analysis.plot_roc_auc import plot_roc, plot_precision_recall
# from INF553_YelpProject.src.machine_learning.split_data_train_test_validation import splitData
from src.data_schema.feature_names import FeatureNames
from src.machine_learning.evaluation_metrics import EvaluationMetric
from src.data_analysis.plot_roc_auc import plot_roc, plot_precision_recall
from src.machine_learning.split_data_train_test_validation import splitData

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

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=62)

    positive_count = 0
    negative_count = 0
    for i in range(len(y_test.values)):
        if y_test.values[i][0] == 1:
            positive_count+=1
        else:
            negative_count+=1
    return X_train, X_test, y_train, y_test

def predict_testdata(model, X_test):
    y_pred = model.predict(X_test)
    return y_pred

def do_feature_selection(X,y,kval):
    
    data_chi2_scores = SelectKBest(f_classif , k=kval).fit(X, y)
    
    selected_feature_indices=data_chi2_scores.get_support(indices=True)
    
    chi2_dataset = SelectKBest(f_classif, k=kval).fit_transform(X, y)
    return chi2_dataset


def run_adaBoost_model():
    """
    1. Construct Dataset.
    2. Run AdaBoost Model on Train data and validate on validation set.
    3. Determin the best hyperparameters by running all possible combinations.
    4. Run on test dataset.
    
    """
    ########## CONSTRUCT DATA SET ############
#     df = pd.read_csv('../../resources/dataset/final_lasvegas_dataset_v4.csv')
    df = pd.read_csv('../../resources/dataset/final_v4_with_filled_data_all.csv')
    
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
    max_depth_ada = 0
    max_n_est = 0
    max_specificity = 0
    learning_rate = 1
    op=open('../../resources/Results/mutual_info_adaboost3.txt','w')
    
    hyperparameters = []
    for k in range(1, X.shape[1]+1):
        
        datasetX = do_feature_selection(X, y, k)
        X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle = False)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle = False)

        for n_estimator in range(20, 100, 10):

            for depth in range(2, 9):
                
#                 print("K = " + str(k) +" N = " +str(n_estimator) + " D = "+ str(depth))
                
                adaboost_model = AdaBoostClassifier(DecisionTreeClassifier(max_depth = depth), n_estimators = n_estimator, learning_rate = learning_rate)
                adaboost_model.fit(X_train, np.ravel(y_train))
        
                y_pred = predict_testdata(adaboost_model, X_test)
        
                evaluation_metric = EvaluationMetric()
        
                result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
                ans = "For top " + str(k) + " " + str(depth)+" " + str(n_estimator) + " " + str(learning_rate) + " features, the result are " + str(result['sensitivity']) + " " + str(result['f1score']) +" \n \n"
#                 op.write(ans)

                if(result['sensitivity'] >= max_recall_f1):
                        
                    max_recall_f1 = result['sensitivity']
                    max_k_val = k
                    
                    f1score = result['f1score']
                    max_depth_ada = depth
                    max_n_est = n_estimator
                    max_specificity = result['specificity']
                    op.write(ans)
                    
        print("\nk = " + str(max_k_val) + " Sensitivity = " + str(max_recall_f1), " F1 Score = " + str(f1score))
    
    
    fout = open("../../resources/Results/AdaBoost_Result.txt", "w", encoding = "utf-8") 
    
    fout.write("\nk = " + str(max_k_val) + " Sensitivity = " + str(max_recall_f1) + " F1 Score = " + str(f1score) + " Specificty = " + str(max_specificity))
    fout.write("\nBest Depth = " + str(max_depth_ada) + " Best Estimator = " + str(max_n_est))

    fout.close()
        
    print("\nk = " + str(max_k_val) + " Sensitivity = " + str(max_recall_f1) + " F1 Score = " + str(f1score) + " Specificty = " + str(max_specificity))
    print("Best Decision Tree Depth = " + str(max_depth_ada) + " Best Estimator = " + str(max_n_est))

    op.close()
    return max_k_val, max_depth_ada, max_n_est, learning_rate


def run_final(k, depth, n_est, learning_rate):
    
    df = pd.read_csv('../../resources/dataset/final_v4_with_filled_data_all.csv')
    
    X = df.drop(['inspection_grade'], axis=1)
    y = df[['inspection_grade']]
    y.replace('A', 0, inplace=True)
    y.replace('B', 1, inplace=True)
    y.replace('C', 1, inplace=True)
    y.replace('D', 1, inplace=True)
    y.replace('E', 1, inplace=True)
    min_max_scaler = preprocessing.MinMaxScaler((0, 1))
    X = min_max_scaler.fit_transform(X)
    
    datasetX = do_feature_selection(X, y, k)
    
    X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=False)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=False)
    
    X_train_final = np.concatenate((X_train,X_test),axis=0)
    y_train_final = np.concatenate((y_train,y_test),axis=0)
    
    adaboost_model = AdaBoostClassifier(DecisionTreeClassifier(max_depth = depth), n_estimators = n_est, learning_rate = learning_rate)
    adaboost_model.fit(X_train_final, np.ravel(y_train_final))
        
    y_pred = predict_testdata(adaboost_model, X_val)
        
    evaluation_metric = EvaluationMetric()
        
    result = evaluation_metric.get_evaluation_metrics(y_val.values, y_pred)
    
    print(result)
    probs = adaboost_model.predict_proba(X_val)
    probs = probs[:, 1]
    
    plot_roc(y_val, probs)
    plot_precision_recall(y_val, y_pred, probs)

    return

if __name__=='__main__':   
    
    start=time.time()
    
#     k, depth, n_est, learning_rate = run_adaBoost_model() 
    
#     k, depth, n_est, learning_rate = 4, 6, 50, 1
    k, depth, n_est, learning_rate = 32, 1, 50, 1
#     k, depth, n_est, learning_rate = 26, 2, 60, 1
    
    print("\nHyper-Parameters: " + str(k) + " " + str(depth)+" " + str(n_est) + " " + str(learning_rate))
    
    run_final(k, depth, n_est, learning_rate)
    
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  