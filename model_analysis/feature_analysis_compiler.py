from statistical_tests.correlation import target_pearson_correlation
from statistical_tests.ttest_all_features import ttest_all_features
from model_analysis.feature_importance import get_feature_contributions
from sklearn.metrics import accuracy_score, root_mean_squared_error
import pandas as pd
import numpy as np

def compile_feature_analysis_classification(features, X_test, y_test, logistic_model, forest_model, gradient_boosting, ffnn_model, feature_names):
    pearson_correlations = target_pearson_correlation(features)

    p_values = ttest_all_features(features)

    compilation = pearson_correlations.merge(p_values, on="Features")

    if logistic_model:
        logistic_importances = get_feature_contributions(logistic_model, feature_names)
        compilation = compilation.merge(logistic_importances, on="Features")

    if forest_model:
        forest_importances = get_feature_contributions(forest_model, feature_names)
        compilation = compilation.merge(forest_importances, on="Features")

    if gradient_boosting:
        gradient_boosting_importances = get_feature_contributions(gradient_boosting, feature_names)
        compilation = compilation.merge(gradient_boosting_importances, on="Features")

    if ffnn_model:
        permuation_importances = get_ffnn_classification_importance(ffnn_model, X_test, y_test, feature_names)
        compilation = compilation.merge(permuation_importances, on="Features")

    return compilation

def get_ffnn_classification_importance(model, X_test, y_test, feature_names):
    y_prob = model.predict(X_test, verbose=0).flatten()
    y_pred = (y_prob >= 0.5).astype(int)

    baseline_accuracy = accuracy_score(y_test, y_pred)

    importances = []

    for i in range(X_test.shape[1]):

        X_permuted = X_test.copy()

        np.random.shuffle(X_permuted[:, i])

        y_prob = model.predict(X_permuted, verbose=0).flatten()
        y_pred = (y_prob >= 0.5).astype(int)

        accuracy = accuracy_score(y_test, y_pred)

        importance = baseline_accuracy - accuracy

        importances.append(round(importance, 3))

    return pd.DataFrame({
        "Features": feature_names,
        "FFNN Importance": importances
    })

def compile_feature_analysis_regression(features, X_test, y_test, linear_regression_model, rf_regressor, gb_regressor, ffnn_regressor, feature_names):
    pearson_correlations = target_pearson_correlation(features)
    
    p_values = ttest_all_features(features)

    compilation = pearson_correlations.merge(p_values, on="Features")

    if linear_regression_model:
        linear_importances = get_feature_contributions(linear_regression_model, feature_names)
        compilation = compilation.merge(linear_importances, on="Features")

    if rf_regressor:
        forest_importances = get_feature_contributions(rf_regressor, feature_names)
        compilation = compilation.merge(forest_importances, on="Features")

    if gb_regressor:
        gradient_boosting_importances = get_feature_contributions(gb_regressor, feature_names)
        compilation = compilation.merge(gradient_boosting_importances, on="Features")

    if ffnn_regressor:
        permuation_importances = get_ffnn_regression_importance(ffnn_regressor, X_test, y_test, feature_names)
        compilation = compilation.merge(permuation_importances, on="Features")

    return compilation

def get_ffnn_regression_importance(model, X_test, y_test, feature_names):
    y_pred = model.predict(X_test, verbose=0).flatten()

    baseline_rmse = root_mean_squared_error(
        y_test,
        y_pred
    )

    importances = []

    for i in range(X_test.shape[1]):
        X_permuted = X_test.copy()

        np.random.shuffle(X_permuted[:, i])

        y_pred = model.predict(X_permuted, verbose=0).flatten()

        rmse = root_mean_squared_error(
            y_test,
            y_pred
        )

        importance = rmse - baseline_rmse

        importances.append(round(importance, 3))

    return pd.DataFrame({
        "Features": feature_names,
        "FFNN Regression Importance": importances
    })