import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


def plot_oob_results(rf_oob_dfs):
    fig, ax = plt.subplots(figsize=(10, 6))

    for max_features, rf_oob_df in rf_oob_dfs:
        rf_oob_df.plot(y="oob", ax=ax, label=max_features)

    ax.set_ylabel("OOB error")
    ax.set_xlabel("Number of trees")
    ax.set_title("OOB error by number of trees")
    ax.legend(loc="upper right")
    fig.savefig("figures/oob.png", format="png")


def plot_classifier_results(y_test, y_pred_rf):
    f, ax = plt.subplots(figsize=(15, 15))
    confusion_mtx = confusion_matrix(y_test, y_pred_rf)
    sns.set(font_scale=1.4)
    sns.heatmap(
        confusion_mtx,
        annot=True,
        linewidths=0.01,
        cmap="Greens",
        linecolor="gray",
        ax=ax,
    )
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix Validation set")
    plt.savefig("figures/matrix.png", format="png")
