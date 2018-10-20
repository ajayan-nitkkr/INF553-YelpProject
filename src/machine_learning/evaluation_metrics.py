from sklearn.metrics import accuracy_score

"""
API to get True Positive, True Negative,
False Positive, False Negative data
"""
def get_confusion_matrix_result(test_actual, test_pred):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(test_pred)):
        if test_pred[i]==1 and test_actual[i]==1 :
           TP += 1
    for i in range(len(test_pred)):
        if test_pred[i]==1 and test_actual[i]==0 :
           FP += 1
    for i in range(len(test_pred)):
        if test_pred[i]==0 and test_actual[i]==0 :
           TN += 1
    for i in range(len(test_pred)):
        if test_pred[i]==0 and test_actual[i]==1:
           FN += 1

    return TP, TN, FP, FN


"""
API to get sensitivity
Called by various names such as sensitivity, recall,
hit rate, true positive rate (TPR)
"""
def get_sensitivity(test_actual, test_pred):
    TP, TN, FP, FN = get_confusion_matrix_result(test_actual, test_pred)
    sensitivity = 0
    if TP + FN != 0:
        sensitivity = (float)(TP) / (TP + FN)
    return sensitivity


"""
API to get specificity
Called by various names such as specificity, selectivity,
true negative rate (TNR)
"""
def get_specificity(test_actual, test_pred):
    TP, TN, FP, FN = get_confusion_matrix_result(test_actual, test_pred)
    specificity = 0
    if TN + FP != 0:
        specificity = (float)(TN) / (TN + FP)
    return specificity


"""
API to get precision
Called by various names such as precision, positive predictive value (PPV)
"""
def get_precision(test_actual, test_pred):
    TP, TN, FP, FN = get_confusion_matrix_result(test_actual, test_pred)
    precision = 0
    if TP + FP != 0:
        precision = (float)(TP) / (TP + FP)
    return precision


"""
API to get accuracy (ACC)
"""
def get_accuracy(test_actual, test_pred):
    accuracy = accuracy_score(test_actual, test_pred)
    return accuracy


"""
API to get all the evaluation metrics
"""
def get_evaluation_metrics(test_actual, test_pred):
    TP, TN, FP, FN = get_confusion_matrix_result(test_actual, test_pred)

    sensitivity = 0
    if TP + FN != 0:
        sensitivity = (float)(TP) / (TP + FN)

    specificity = 0
    if TN + FP != 0:
        specificity = (float)(TN) / (TN + FP)

    precision = 0
    if TP + FP != 0:
        precision = (float)(TP) / (TP + FP)

    accuracy = accuracy_score(test_actual, test_pred)

    return TP, TN, FP, FN, sensitivity, specificity, precision, accuracy