import pandas as pd

from sklearn.model_selection import train_test_split

ALL_FILES = ["data/0.csv", "data/1.csv", "data/2.csv", "data/3.csv"]


def read_data():
    """
    Read the data from the csv files and return the dataframes
    and the train and test sets.

    The Ratio of the train and test sets is 50:50.
    """
    array = []

    for file in ALL_FILES:
        read = pd.read_csv(file, header=None)
        array.append(read)

    df = pd.concat(array)
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values
    # Random State is set to 42 for reproducibility
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(
        X, Y, test_size=0.50, random_state=42
    )
    return df, Xtrain, Xtest, Ytrain, Ytest
