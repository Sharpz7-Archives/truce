import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from truce.utils import read_data
from truce.tree_count import calculate_best_tree_count

df, X_train, X_test, y_train, y_test = read_data()

print(df.shape)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

s = StandardScaler()
X_train_s = s.fit_transform(X_train)
X_test_s = s.transform(X_test)

best_tree_count = calculate_best_tree_count(X_train_s, y_train)
print(best_tree_count)

optimised_classifier = RandomForestClassifier(
    n_estimators=200, oob_score=True, random_state=42, n_jobs=-1
)

optimised_classifier.fit(X_train_s, y_train)

y_pred_rf = optimised_classifier.predict(X_test_s)

print(classification_report(y_test, y_pred_rf))

f, ax = plt.subplots(figsize=(15, 15))
confusion_mtx = confusion_matrix(y_test, y_pred_rf)
sns.set(font_scale=1.4)
sns.heatmap(
    confusion_mtx, annot=True, linewidths=0.01, cmap="Greens", linecolor="gray", ax=ax
)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix Validation set")
plt.savefig("matrix.png", format="png")
