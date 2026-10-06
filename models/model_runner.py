from model_analysis.model_evaluation import evaluate_classification_model, evaluate_regression_model
from model_analysis.model_report import classification_model_report, regression_model_report
from model_analysis.store_results import save_classification_results, save_regression_results
from backtesting.backtesting_results import show_classification_backtest_results, show_regression_backtest_results
from visualisation.capital_history import show_capital_history
import pandas as pd

def run_classification_model(model_function, training_data, test_data, ticker, experiment_settings, backtest_data):
    model, scaler, testing_data, tested_values, predicted_values, probabilities = model_function(training_data, test_data)

    value_counts, accuracy, precision, recall, f1, matrix = evaluate_classification_model(tested_values, predicted_values)

    classification_model_report(model, ticker, value_counts, accuracy, precision, recall, f1, matrix)

    predicted_values = pd.Series(predicted_values, index=test_data.index, name="Predictions")
    probabilities = pd.Series(probabilities, index=test_data.index, name="Confidence")
    
    backtest_results = show_classification_backtest_results(experiment_settings, backtest_data, predicted_values, probabilities)
    
    show_capital_history(backtest_results, model, "classifier")

    save_classification_results(model, ticker, accuracy, precision, recall, f1, backtest_results, experiment_settings["name"])
    
    return model, scaler, testing_data, predicted_values, probabilities

def run_regression_model(model_function, training_data, test_data, ticker, experiment_settings, backtest_data):
    model, scaler, testing_data, tested_values, predicted_values = model_function(training_data, test_data)

    mae, rmse, r2, directional_accuracy = evaluate_regression_model(tested_values, predicted_values)

    regression_model_report(model, ticker, mae, rmse, r2, directional_accuracy)

    predicted_values = pd.Series(predicted_values, index=test_data.index, name="Predictions")

    backtest_results = show_regression_backtest_results(experiment_settings, backtest_data, predicted_values)

    show_capital_history(backtest_results, model, "regressor")

    save_regression_results(model, ticker, mae, rmse, r2, directional_accuracy, backtest_results, experiment_settings["name"])

    return model, scaler, testing_data, predicted_values