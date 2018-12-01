
from sklearn.feature_selection import VarianceThreshold

from src.machine_learning.split_data_train_test_validation import *
from sklearn import preprocessing

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, mutual_info_classif
import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_schema.feature_names import FeatureNames


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


def get_training_val_test_set(filename):
    X_train,X_val,X_test,y_train,y_val,y_test=splitData(filename)
    return X_train,X_val,X_test,y_train,y_val,y_test

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


if __name__ == '__main__':
    X_train, X_val, X_test, y_train, y_val, y_test = splitData(
        filename='../../resources/dataset/final_lasvegas_dataset_v4.csv')

    min_max_scaler = preprocessing.MinMaxScaler((0, 1))
    X_train = min_max_scaler.fit_transform(X_train)
    X_test = min_max_scaler.transform(X_test)

    X_new_chi2 = SelectKBest(chi2, k=10).fit(X_train, y_train)
    print(X_new_chi2.get_support(indices=True))
    X_new_chi2_data = SelectKBest(chi2, k=10).fit_transform(X_train, y_train)

    '''
    print(len(X_new_chi2))

    X_new_f_classif = SelectKBest(f_classif, k=10).fit(X_train, y_train)
    print(X_new_f_classif.get_support(indices=True))
    print(type(X_new_f_classif))

    X_new_mutual_info = SelectKBest(mutual_info_classif, k=10).fit(X_train, y_train)
    print(X_new_mutual_info.get_support(indices=True))
    print(type(X_new_mutual_info))
    '''