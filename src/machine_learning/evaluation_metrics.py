from sklearn.metrics import accuracy_score

"""
Author: Ajay Anand
"""
class EvaluationMetric:
    DEFAULT_VALUE = -1
    LABEL_TP = "TP"
    LABEL_FP = "FP"
    LABEL_TN = "TN"
    LABEL_FN = "FN"
    LABEL_SENSITIVITY = "sensitivity"
    LABEL_SPECIFICITY = "specificity"
    LABEL_PRECISION = "precision"
    LABEL_F1SCORE = "f1score"
    LABEL_ACCURACY = "accuracy"

    def __init__(self):
        self.TP = self.DEFAULT_VALUE
        self.FP = self.DEFAULT_VALUE
        self.TN = self.DEFAULT_VALUE
        self.FN = self.DEFAULT_VALUE
        self.sensitivity = self.DEFAULT_VALUE
        self.specificity = self.DEFAULT_VALUE
        self.precision = self.DEFAULT_VALUE
        self.f1_score = self.DEFAULT_VALUE
        self.accuracy = self.DEFAULT_VALUE

    """
    API to get True Positive, True Negative,
    False Positive, False Negative data
    """
    def get_confusion_matrix_result(self, test_actual, test_pred):
        if self.TP != self.DEFAULT_VALUE and self.TN != self.DEFAULT_VALUE and \
                        self.FP != self.DEFAULT_VALUE and self.FN != self.DEFAULT_VALUE:
            # value already exist
            return self.TP, self.TN, self.FP, self.FN

        self.TP, self.FP, self.TN, self.FN = 0, 0, 0, 0
        for i in range(len(test_pred)):
            if test_pred[i]==1 and test_actual[i]==1 :
                self.TP += 1
            elif test_pred[i]==1 and test_actual[i]==0 :
                self.FP += 1
            elif test_pred[i]==0 and test_actual[i]==0 :
                self.TN += 1
            elif test_pred[i]==0 and test_actual[i]==1:
                self.FN += 1

        return self.TP, self.TN, self.FP, self.FN

    """
    API to get sensitivity
    Called by various names such as sensitivity, recall,
    hit rate, true positive rate (TPR)
    """
    def get_sensitivity(self, test_actual, test_pred):
        if self.sensitivity != self.DEFAULT_VALUE:
            # value already exist
            return self.sensitivity

        self.TP, self.TN, self.FP, self.FN = self.get_confusion_matrix_result(test_actual, test_pred)

        if self.TP + self.FN != 0:
            self.sensitivity = (float)(self.TP) / (self.TP + self.FN)
        else:
            self.sensitivity = 0
        return self.sensitivity

    """
    API to get specificity
    Called by various names such as specificity, selectivity,
    true negative rate (TNR)
    """
    def get_specificity(self, test_actual, test_pred):
        if self.specificity != self.DEFAULT_VALUE:
            # value already exist
            return self.specificity

        self.TP, self.TN, self.FP, self.FN = self.get_confusion_matrix_result(test_actual, test_pred)

        if self.TN + self.FP != 0:
            self.specificity = (float)(self.TN) / (self.TN + self.FP)
        else:
            self.specificity = 0
        return self.specificity

    """
    API to get precision
    Called by various names such as precision, positive predictive value (PPV)
    """
    def get_precision(self, test_actual, test_pred):
        if self.precision != self.DEFAULT_VALUE:
            # value already exist
            return self.precision

        self.TP, self.TN, self.FP, self.FN = self.get_confusion_matrix_result(test_actual, test_pred)

        if self.TP + self.FP != 0:
            self.precision = (float)(self.TP) / (self.TP + self.FP)
        else:
            self.precision = 0
        return self.precision

    """
    API to get F1 score
    """
    def get_F1score(self, test_actual, test_pred):
        if self.f1_score != self.DEFAULT_VALUE:
            # value already exist
            return self.f1_score

        self.TP, self.TN, self.FP, self.FN = self.get_confusion_matrix_result(test_actual, test_pred)

        self.precision = self.get_precision(test_actual, test_pred)
        self.sensitivity = self.get_sensitivity(test_actual, test_pred)

        if self.sensitivity + self.precision != 0:
            self.f1_score = (float)(2*self.precision*self.sensitivity)/(self.precision+self.sensitivity)
        else:
            self.f1_score = 0

        return self.f1_score

    """
    API to get accuracy (ACC)
    """
    def get_accuracy(self, test_actual, test_pred):
        if self.accuracy != self.DEFAULT_VALUE:
            # value already exist
            return self.accuracy

        self.accuracy = accuracy_score(test_actual, test_pred)
        return self.accuracy

    """
    API to get all the evaluation metrics
    """
    def get_evaluation_metrics(self, test_actual, test_pred):
        self.TP, self.TN, self.FP, self.FN = self.get_confusion_matrix_result(test_actual, test_pred)
        self.sensitivity = self.get_sensitivity(test_actual, test_pred)
        self.specificity = self.get_specificity(test_actual, test_pred)
        self.precision = self.get_precision(test_actual, test_pred)
        self.f1_score = self.get_F1score(test_actual, test_pred)
        self.accuracy = self.get_accuracy(test_actual, test_pred)

        eval_dict = {}
        eval_dict[self.LABEL_TP] = self.TP
        eval_dict[self.LABEL_TN] = self.TN
        eval_dict[self.LABEL_FP] = self.FP
        eval_dict[self.LABEL_FN] = self.FN
        eval_dict[self.LABEL_SENSITIVITY] = self.sensitivity
        eval_dict[self.LABEL_SPECIFICITY] = self.specificity
        eval_dict[self.LABEL_PRECISION] = self.precision
        eval_dict[self.LABEL_F1SCORE] = self.f1_score
        eval_dict[self.LABEL_ACCURACY] = self.accuracy
        return eval_dict