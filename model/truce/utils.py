import pandas as pd

from sklearn.model_selection import train_test_split


def read_data():
    print(allFiles)

    array = []

    for file in allFiles:
        read = pd.read_csv(file, header=None)
        array.append(read)

    df = pd.concat(array)
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.15)
    return Xtrain, Xtest, Ytrain, Ytest
