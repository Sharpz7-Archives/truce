import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier


def calculate_best_tree_count(X_train_s, y_train):
    RF = RandomForestClassifier(
        oob_score=True, random_state=42, warm_start=True, n_jobs=-1
    )
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

    # Find which tree count is best
    best_tree_count = rf_oob_df.idxmin()[0]
    print(f"Best tree count: {best_tree_count}")
    return best_tree_count
