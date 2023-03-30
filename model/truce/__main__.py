import warnings

from micromlgen import port
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from truce.hyperparams import hyper_tune
from truce.plots import plot_oob_results, plot_classifier_results
from truce.utils import read_data

# Remove Warnings Related to bad oob scores
warnings.filterwarnings("ignore", category=UserWarning)

df, X_train, X_test, y_train, y_test = read_data()

rf_oob_dfs = hyper_tune(X_train, y_train)

# Plot the results
plot_oob_results(rf_oob_dfs)

# Find the best max_features and best tree count
# by looking at the minimum OOB error
min_oob = min([rf_oob_df["oob"].min() for max_features, rf_oob_df in rf_oob_dfs])
for max_features, rf_oob_df in rf_oob_dfs:
    if rf_oob_df["oob"].min() == min_oob:
        BEST_MAX_FEATURES = max_features
        BEST_TREE_COUNT = rf_oob_df["oob"].idxmin()
        break

print(f"Best max features: {BEST_MAX_FEATURES}")
print(f"Best tree count: {BEST_TREE_COUNT}")

# Random State is set to 42 for reproducibility
optimised_classifier = RandomForestClassifier(
    n_estimators=int(BEST_TREE_COUNT),
    random_state=42,
    n_jobs=-1,
    max_features=BEST_MAX_FEATURES,
)

optimised_classifier.fit(X_train, y_train)

y_pred_rf = optimised_classifier.predict(X_test)

print(classification_report(y_test, y_pred_rf))

plot_classifier_results(y_test, y_pred_rf)

# Send ported model to file
with open("../truce-c/src/RandomForest.h", "w", encoding="utf-8") as f:
    f.write(port(optimised_classifier))
