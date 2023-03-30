import pandas as pd

from sklearn.model_selection import train_test_split

ALL_FILES = ["data/0.csv", "data/1.csv", "data/2.csv", "data/3.csv"]


def read_data():
    print(ALL_FILES)

    array = []

    for file in ALL_FILES:
        read = pd.read_csv(file, header=None)
        array.append(read)

    df = pd.concat(array)
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.15)
    return Xtrain, Xtest, Ytrain, Ytest
