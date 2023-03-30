import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def hyper_tune(X_train_s, y_train):
    """
    Tune the hyperparameters of the Random Forest Classifier
    using Out of Bag Error.

    Here we specifically tune the number of trees and the
    max_features parameter.
    """

    rf_oob_dfs = []
    for max_features in ["sqrt", "log2", None]:
        # Max Depth was set to 3 to reduce the number of trees
        # required to achieve a good OOB score.
        # Random State is set to 42 for reproducibility
        rf_test = RandomForestClassifier(
            oob_score=True,
            random_state=42,
            max_features=max_features,
            max_depth=3,
            n_jobs=-1,
        )
        oob_list = []
        for n_trees in range(10, 20, 1):
            rf_test.set_params(n_estimators=n_trees)
            rf_test.fit(X_train_s, y_train)
            oob_error = 1 - rf_test.oob_score_
            oob_list.append(pd.Series({"n_trees": n_trees, "oob": oob_error}))

        rf_oob_df = pd.concat(oob_list, axis=1).T.set_index("n_trees")
        rf_oob_dfs.append((max_features, rf_oob_df))

    return rf_oob_dfs
