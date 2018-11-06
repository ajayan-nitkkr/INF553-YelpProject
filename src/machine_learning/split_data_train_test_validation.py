from sklearn.model_selection import train_test_split
import pandas as pd

def splitData():
    dataframe = pd.read_csv("../../resources/dataset/final_lasvegas_dataset.csv")
    array = dataframe.values
    X_train, X_test= train_test_split(array, test_size=0.2, random_state=1)
    X_train, X_val, = train_test_split(X_train, test_size=0.25, random_state=1)

if __name__ == "__main__":
    splitData()