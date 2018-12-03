import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from feature_names import FeatureNames
from evaluation_metrics import EvaluationMetric
from plot import plot_roc
from plot import plot_precision_recall
from sklearn import preprocessing
import numpy as np
from sklearn.svm import SVC
import pandas as pd
import math
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif
from sklearn import preprocessing




# def categorize_score_attribute_with_boolean(row):
#     # attribute_name = 'SCORE'
#     schema_obj = FeatureNames()
#     attribute_name = schema_obj.COL_INSPECTION_SCORE
#
#     modified_score = None
#     if row[attribute_name] > 90 and row[attribute_name] <= 100: modified_score = 0
#     elif row[attribute_name] > 0 and row[attribute_name] <= 90: modified_score = 1
#     return modified_score



def train_DecisionTree(X_train,Y_train):
    '''
    Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.
    This class supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.
    '''
    dtree=DecisionTreeClassifier(random_state = 100)
    dtree.fit(X_train,Y_train)
    return dtree


def predict_testdata(svm_clf, X_test):
    y_pred = svm_clf.predict(X_test)
    return y_pred

def do_feature_selection(X,y,kval):
    data_chi2_scores = SelectKBest(f_classif, k=kval).fit(X, y)
    selected_feature_indices=data_chi2_scores.get_support(indices=True)
    #print(selected_feature_indices)
    chi2_dataset = SelectKBest(f_classif, k=kval).fit_transform(X, y)
    return chi2_dataset


if __name__ == '__main__':

    ########### CONSTRUCT DATA SET ############
    #df = construct_dataset()
    ###########################################

    ############# DATA SLICING ################
    #X_train,X_val,X_test,y_train,y_val,y_test = splitData(filename = '/Users/apple/Downloads/v4.csv')#divide_dataset(df)
    # print(X_train,X_test,y_train,y_test)
    ###########################################

    ################ TRAINING #################
    df = pd.read_csv('/Users/apple/IdeaProjects/INF553-YelpProject/resources/dataset/final_v4_with_filled_data_all.csv')
    X = df.drop(['inspection_grade'], axis=1)
    y = df[['inspection_grade']]
    y.replace('A', 0, inplace=True)
    y.replace('B', 1, inplace=True)
    y.replace('C', 1, inplace=True)
    y.replace('D', 1, inplace=True)
    y.replace('E', 1, inplace=True)
    min_max_scaler = preprocessing.MinMaxScaler((0, 1))
    X = min_max_scaler.fit_transform(X)

    max_sensitivity = 0
    max_f1score = 0
    max_specificity = 0
    
    #criterion_list = ['gini','entropy']

    op=open('/Users/apple/IdeaProjects/INF553-YelpProject/resources/Results/chi2_decisionTree.txt','w')
    for k in range(1,X.shape[1]+1):
        datasetX = do_feature_selection(X, y, k)


        ############# DATA SLICING ################

        X_train, X_test, y_train, y_test = train_test_split(datasetX, y, test_size=0.2, random_state=1, shuffle=False)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1, shuffle=False)

        #for criterionAtt in criterion_list:
        svm_clf = train_DecisionTree(X_train, y_train)
        y_pred = predict_testdata(svm_clf, X_test)
        evaluation_metric = EvaluationMetric()
        # confusion_matrix = confusion_matrix(y_test.values, y_pred)
        result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
        ans = "For top " + str(k)  + \
                      ", sensitivity:" + str(result["sensitivity"]) + ", F1 score:" + str(
                    result["f1score"]) + ", Specificity:" + str(
                    result["specificity"]) + "\n \n"
        op.write(ans)
        if result["sensitivity"] > max_sensitivity:
             max_sensitivity = result["sensitivity"]
             max_f1score = result["f1score"]
             max_specificity = result["specificity"]
    print("max_sensitivity:", max_sensitivity)
    print("max_f1score:", max_f1score)
    print("max_specificity:", max_specificity)
        #probs = svm_clf.predict_proba(X_test)
        #probs = probs[:, 1]
        ################ ACCURACY #################
        ##evaluation_metric = EvaluationMetric()
        # confusion_matrix = confusion_matrix(y_test.values, y_pred)
        ##result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
        ###ans="For top "+str(k)+" features, the result are "+ str(result)+" \n \n"
        ###op.write(ans)
        #plot_roc(y_test.values, probs)
        #plot_precision_recall(y_test.values, y_pred, probs)
