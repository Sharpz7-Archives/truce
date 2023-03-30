import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


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


allFiles = ["data/0.csv", "data/1.csv", "data/2.csv", "data/3.csv"]

data = []
for file in allFiles:
    read = pd.read_csv(file, header=None)
    data.append(read)

df = pd.concat(data)

print(df.shape)

count_plot = sns.countplot(x=64, data=df)
fig = count_plot.get_figure()
fig.savefig("out.png")

X_train, X_test, y_train, y_test = read_data()

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

s = StandardScaler()
X_train_s = s.fit_transform(X_train)
X_test_s = s.transform(X_test)

RF = RandomForestClassifier(oob_score=True, random_state=42, warm_start=True, n_jobs=-1)
oob_list = []
for n_trees in [15, 20, 30, 40, 50, 100, 150, 200, 300, 400]:
    RF.set_params(n_estimators=n_trees)
    RF.fit(X_train_s, y_train)
    oob_error = 1 - RF.oob_score_
    oob_list.append(pd.Series({"n_trees": n_trees, "oob": oob_error}))

rf_oob_df = pd.concat(oob_list, axis=1).T.set_index("n_trees")

sns.set_context("talk")
sns.set_style("white")

ax = rf_oob_df.plot(legend=False, marker="o", figsize=(14, 7), linewidth=5)
ax.set(ylabel="out-of-bag error")

# Save ax to file
fig = ax.get_figure()
fig.savefig("bag-error.png", format="png")
