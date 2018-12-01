from sklearn.model_selection import train_test_split
import pandas as pd

def splitData(filename):
    dataframe = pd.read_csv(filename)
    X = dataframe.drop(['inspection_grade'],axis=1)
    y = dataframe[['inspection_grade']]
    y.replace('A',0,inplace=True)
    y.replace('B',1,inplace=True)
    y.replace('C',1,inplace=True)
    y.replace('D',1,inplace=True)
    y.replace('E',1,inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1, shuffle=True)
    X_train, X_val,y_train, y_val = train_test_split(X_train,y_train, test_size=0.25, random_state=1, shuffle=True)

    return X_train,X_val,X_test,y_train,y_val,y_test


if __name__ == "__main__":
    splitData("/Users/apple/Desktop/final_lasvegas_dataset.csv")
