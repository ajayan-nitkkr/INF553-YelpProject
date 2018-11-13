import time
from collections import defaultdict
from INF553_YelpProject.src.utils.inputOutput_utils import csvReader, csvWriter_from_text
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from INF553_YelpProject.src.data_schema.feature_names import FeatureNames
from INF553_YelpProject.src.machine_learning.evaluation_metrics import EvaluationMetric


def run_adaBoost_model(path):
    x_test, x_train, x_validate =  csvReader(path + "X_test.csv"), csvReader(path + "X_train.csv"), csvReader(path + "X_validate.csv")
    y_test, y_train, y_validate =  csvReader(path + "y_test.csv"), csvReader(path + "y_train.csv"), csvReader(path + "y_validate.csv")
    
    
    model_real = AdaBoostClassifier( DecisionTreeClassifier(max_depth=2),n_estimators=600,learning_rate=1)

    model_discrete = AdaBoostClassifier( DecisionTreeClassifier(max_depth=2), n_estimators=600, learning_rate=1.5, algorithm="SAMME")
    
    


if __name__=='__main__':   
    
    start=time.time()
    path = "../../resources/split_data/"
    
    run_adaBoost_model(path) 
    print ("\nRun time: "+ str(time.time()-start)+" seconds" )  