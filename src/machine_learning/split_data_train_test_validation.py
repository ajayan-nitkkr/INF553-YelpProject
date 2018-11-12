# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split
import pandas as pd

def splitData():
    dataframe = pd.read_csv("/Users/apple/Desktop/final_lasvegas_dataset.csv")
    X = dataframe.drop(['current_grade','current_score','inspection_grade','inspection_score'],axis=1)
    y = dataframe[['inspection_grade']]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1, shuffle=False)
    X_train, X_validate,y_train, y_validate = train_test_split(X_train,y_train, test_size=0.25, random_state=1, shuffle=False)
    
    X_train.to_csv("/Users/apple/Desktop/X_train.csv", encoding='utf-8', index=False)
    y_train.to_csv("/Users/apple/Desktop/y_train.csv", encoding='utf-8', index=False)
    X_test.to_csv("/Users/apple/Desktop/X_test.csv", encoding='utf-8', index=False)
    y_test.to_csv("/Users/apple/Desktop/y_test.csv", encoding='utf-8', index=False)
    X_validate.to_csv("/Users/apple/Desktop/X_validate.csv", encoding='utf-8', index=False)
    y_validate.to_csv("/Users/apple/Desktop/y_validate.csv", encoding='utf-8', index=False)
    #print(len(X_test))
    #print (len(y_test))
    #print (len(X_train))
    #print (len(y_train))
    #print (len(X_validate))
    #print (len(y_validate))


if __name__ == "__main__":
    splitData()
