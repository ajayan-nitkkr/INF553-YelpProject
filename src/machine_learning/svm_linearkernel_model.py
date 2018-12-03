"""
Author: Ajay Anand
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import preprocessing
from src.data_schema.feature_names import FeatureNames
from src.machine_learning.evaluation_metrics import EvaluationMetric
from src.machine_learning.split_data_train_test_validation import splitData
from src.data_analysis.plot_roc_auc import plot_roc,plot_precision_recall
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif


def do_feature_selection(X,y,kval):
    data_chi2_scores = SelectKBest(mutual_info_classif, k=kval).fit(X, y)
    selected_feature_indices=data_chi2_scores.get_support(indices=True)
    chi2_dataset = SelectKBest(mutual_info_classif, k=kval).fit_transform(X, y)
    return chi2_dataset


if __name__ == '__main__':

    ########### CONSTRUCT DATA SET ############
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

    # C_list = [0.001, 0.01, 0.1, 1, 10]
    # gamma_list = [0.001, 0.01, 0.1, 1]
    # max_iter_list = [1, 10, 20, 50, 100, 200, 500, 1000]
    #
    # op=open('../../resources/Results/mutual_info_classif_svm.txt','w')
    # op2 = open('../../resources/Results/mutual_info_classif_svm2.txt', 'w')
    # max_sensitivity = 0
    # max_f1score = 0
    # best_k = 0
    # count = 0
    # for k in range(1,X.shape[1]+1):
    #     datasetX = do_feature_selection(X, y, k)
    #
    #     ############# DATA SLICING ################
    #     X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=False)
    #     X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=False)
    #
    #     ############# TRAIN AND RUN THE MODEL ################
    #     for C in C_list:
    #         for gamma in gamma_list:
    #             for max_iter in max_iter_list:
    #                 count += 1
    #                 print(count)
    #                 svm_clf = svm.SVC(kernel='linear', probability=True, C=C, gamma=gamma, max_iter=max_iter)
    #                 svm_clf.fit(X_train, y_train)
    #                 y_pred = svm_clf.predict(X_test)
    #                 evaluation_metric = EvaluationMetric()
    #                 result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
    #                 # ans="For top "+str(k)+" features, the result are "+ str(result)+" \n \n"
    #                 # op.write(ans)
    #                 ans = "For top "+str(k)+" features," + " C:" + str(C) + ", gamma:" + str(gamma) + ", max_iter:" + str(max_iter) + \
    #                       ", sensitivity:" + str(result["sensitivity"]) + ", F1 score:" + str(result["f1score"]) + "\n \n"
    #                 op.write(ans)
    #                 if result["sensitivity"] >= max_sensitivity:
    #                     max_sensitivity = result["sensitivity"]
    #                     max_f1score = result["f1score"]
    #                     best_k = k
    #                     op2.write(ans)
    #
    #     ###########################################
    #
    # print("max_sensitivity:", max_sensitivity)
    # print("max_f1score:", max_f1score)
    # print("best k:", k)

    # FINAL TESTING
    k_best_features = 15
    max_iter = 20
    C = 0.01
    gamma = 0.01
    datasetX = do_feature_selection(X, y, k_best_features)

    X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=False)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=False)

    X_train_final = np.concatenate((X_train, X_test), axis=0)
    y_train_final = np.concatenate((y_train, y_test), axis=0)

    svm_clf = svm.SVC(kernel='linear', probability=True, C=C, gamma=gamma, max_iter=max_iter)
    svm_clf.fit(X_train_final, y_train_final)
    y_pred = svm_clf.predict(X_val)
    evaluation_metric = EvaluationMetric()
    result = evaluation_metric.get_evaluation_metrics(y_val.values, y_pred)
    print(result)

    probs = svm_clf.predict_proba(X_val)
    probs = probs[:, 1]
    plot_roc(y_val, probs)
    plot_precision_recall(y_val, y_pred, probs)