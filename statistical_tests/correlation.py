import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def features_pearson_correlation(features):
    features = features.drop("target", axis=1)
    correlations = features.corr(method="pearson")

    plt.figure(figsize=(10, 10))

    sns.heatmap(correlations, annot=True, cmap="coolwarm", center=0)

    plt.title("Pearson Correlation Heatmap")
    plt.show(block=False)
    plt.pause(0.1)

def target_pearson_correlation(features):
    features = features.drop("target", axis=1)
    target_correlations = features.corr(method="pearson")["future_return"]
    target_correlations = target_correlations.drop("future_return")

    feature_names = list(target_correlations.index)

    pearson_correlations = pd.DataFrame({
        "Features": feature_names,
        "Pearson Correlations": target_correlations
    })

    return pearson_correlations