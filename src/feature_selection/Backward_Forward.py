import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
from src.machine_learning.evaluation_metrics import EvaluationMetric
from src.data_analysis.plot_roc_auc import *

def forward_tuning(X_train,y_train,X_test,y_test):

   n,m=X_train.shape
   for i in range(1,m+1):
       input_set=X_train[:,:i]
       result=run_model(input_set,y_train,X_test,y_test)
       print("For the first {} features, result is {}".format(i,result))

def predict_testdata(clf, X_test):
    y_pred = clf.predict(X_test)
    return y_pred


def predict_probabilities(svm_clf, X_test):
    probs = svm_clf.predict_proba(X_test)
    return probs


def backward_tuning(X_train,y_train,X_test,y_test):
    n, m = X_train.shape
    for i in range(m+1, 0, -1):
        input_set = X_train[:, :i]
        result = run_model(input_set, y_train, X_test, y_test)
        print("Taking till 0 to {} features, result is {}".format(i, result))


def run_model(X_train,y_train,X_test,y_test):
    svm = LinearSVC()
    clf = CalibratedClassifierCV(svm)
    clf = clf.fit(X_train, y_train)

    y_pred = predict_testdata(clf, X_test)

    evaluation_metric = EvaluationMetric()
    result = evaluation_metric.get_evaluation_metrics(y_test.values, y_pred)
    return result


train_X=[[1,2,3],[4,5,6],[7,8,9]]
X_train=np.array(train_X)
y_train=[1,2,3]
#forward_tuning(X_train,y_train,X_test,y_test)
#backward_tuning(X_train,y_train,X_test,y_test)