import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from catboost import CatBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


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

model = CatBoostClassifier(iterations=300, learning_rate=0.7, random_seed=42, depth=5)

s = StandardScaler()
X_train_s = s.fit_transform(X_train)
X_test_s = s.transform(X_test)

model.fit(
    X_train_s, y_train, cat_features=None, eval_set=(X_test_s, y_test), verbose=False
)

prediction = model.predict(X_test_s)

print(classification_report(y_test, prediction))

f, ax = plt.subplots(figsize=(15, 15))
confusion_mtx = confusion_matrix(y_test, prediction)
sns.set(font_scale=1.4)
sns.heatmap(
    confusion_mtx, annot=True, linewidths=0.01, cmap="Greens", linecolor="gray", ax=ax
)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix Validation set")
plt.savefig("matrix.png", format="png")
