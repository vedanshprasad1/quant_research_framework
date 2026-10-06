from models.model_runner import run_classification_model, run_regression_model
from models.logistic_regression import logistic_regression_model, linear_regression_model
from models.random_forest import random_forest_model, random_forest_regressor
from models.gradient_boosting import gradient_boosting_model, gradient_boosting_regressor
from models.neural_network import ffnn_classifier, ffnn_regressor
from model_analysis.feature_analysis_compiler import compile_feature_analysis_classification, compile_feature_analysis_regression
from model_analysis.store_results import delete_experiment_results
import matplotlib.pyplot as plt

def run_experiment(df, experiment_settings, features, ticker):
    delete_experiment_results(experiment_settings["name"])

    feature_names = experiment_settings["features"]

    backtest_data = features.loc[experiment_settings["split_date"]:]

    training_data = features.loc[:experiment_settings["split_date"]]
    test_data = features.loc[experiment_settings["split_date"]:]

    training_data = training_data[feature_names + ["target", "future_return"]]
    test_data = test_data[feature_names + ["target", "future_return"]]

    classification_analysis = None
    regression_analysis = None

    logistic_model = None
    logistic_scaler = None
    rf_model = None
    gb_model = None
    ffnn_model = None
    ffnn_scaler = None
    linear_model = None
    linear_scaler = None
    rf_regressor = None
    gb_regressor = None
    ffnn_regression = None
    ffnn_regressor_scaler = None

    classification_testing_data = None
    classification_predicted_values = None
    probabilities = None
    regression_testing_data = None
    regression_predicted_values = None

    for model in experiment_settings["models"]:
        if model == "logistic_regression":
            logistic_model, logistic_scaler, classification_testing_data, classification_predicted_values, probabilities = run_classification_model(logistic_regression_model, training_data, test_data, ticker, experiment_settings, backtest_data)

        elif model == "random_forest":
            rf_model, _, classification_testing_data, classification_predicted_values, probabilities = run_classification_model(random_forest_model, training_data, test_data, ticker, experiment_settings, backtest_data)

        elif model == "gradient_boosting":
            gb_model, _, classification_testing_data, classification_predicted_values, probabilities = run_classification_model(gradient_boosting_model, training_data, test_data, ticker, experiment_settings, backtest_data)

        elif model == "ffnn_classifier":
            ffnn_model, ffnn_scaler, classification_testing_data, classification_predicted_values, probabilities = run_classification_model(ffnn_classifier, training_data, test_data, ticker, experiment_settings, backtest_data)

        elif model == "linear_regression":
            linear_model, linear_scaler, regression_testing_data, regression_predicted_values = run_regression_model(linear_regression_model, training_data, test_data, ticker, experiment_settings, backtest_data)

        elif model == "random_forest_regressor":
            rf_regressor, _, regression_testing_data, regression_predicted_values = run_regression_model(random_forest_regressor, training_data, test_data, ticker, experiment_settings, backtest_data)

        elif model == "gradient_boosting_regressor":
            gb_regressor, _, regression_testing_data, regression_predicted_values = run_regression_model(gradient_boosting_regressor, training_data, test_data, ticker, experiment_settings, backtest_data)

        elif model == "ffnn_regressor":
            ffnn_regression, ffnn_regressor_scaler, regression_testing_data, regression_predicted_values = run_regression_model(ffnn_regressor, training_data, test_data, ticker, experiment_settings, backtest_data)

    plt.show(block=False)
    plt.pause(0.1)

    trained_models = {
        "logistic_regression": {
            "model": logistic_model,
            "scaler": logistic_scaler
        },
        "random_forest": {
            "model": rf_model,
            "scaler": None
        },
        "gradient_boosting": {
            "model": gb_model,
            "scaler": None
        },
        "ffnn_classifier": {
            "model": ffnn_model,
            "scaler": ffnn_scaler
        },
        "linear_regression": {
            "model": linear_model,
            "scaler": linear_scaler
        },
        "random_forest_regressor": {
            "model": rf_regressor,
            "scaler": None
        },
        "gradient_boosting_regressor": {
            "model": gb_regressor,
            "scaler": None
        },
        "ffnn_regressor": {
            "model": ffnn_regression,
            "scaler": ffnn_regressor_scaler
        }
    }

    if logistic_model or rf_model or gb_model or ffnn_model:
        classification_analysis = compile_feature_analysis_classification(features, classification_testing_data, classification_predicted_values, logistic_model, rf_model, gb_model, ffnn_model, feature_names)

    if linear_model or rf_regressor or gb_regressor or ffnn_regression:
        regression_analysis = compile_feature_analysis_regression(features, regression_testing_data, regression_predicted_values, linear_model, rf_regressor, gb_regressor, ffnn_regression, feature_names)

    return classification_analysis, regression_analysis, trained_models