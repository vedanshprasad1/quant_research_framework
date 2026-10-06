import json
import os

def save_classification_results(model, ticker, accuracy, precision, recall, f1, backtest_results, experiment_name):
    result = {
        "model": type(model).__name__,
        "problem type": "classification",
        "experiment": experiment_name,
        "stock": ticker,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

    filename = "results/results.json"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                results = json.load(file)
            except json.JSONDecodeError:
                results = []
    else:
        results = []

    result["backtest_results"] = cleaned_backtest_results(backtest_results)
    results.append(result)

    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

    return result

def save_regression_results(model, ticker, mae, rmse, r2, directional_accuracy, backtest_results, experiment_name):
    result = {
        "model": type(model).__name__,
        "problem type": "regression",
        "experiment": experiment_name,
        "stock": ticker,
        "mean absolute error": mae,
        "root mean square error": rmse,
        "r2": r2, 
        "directional accuracy": directional_accuracy,
    }

    filename = "results/results.json"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                results = json.load(file)
            except json.JSONDecodeError:
                results = []
    else:
        results = []

    result["backtest_results"] = cleaned_backtest_results(backtest_results)
    results.append(result)

    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

    return result

def cleaned_backtest_results(backtest_results):
    cleaned_results = {}

    for strategy, results in backtest_results.items():
        cleaned_results[strategy] = {
            key: value
            for key, value in results.items()
            if key != "capital_history"
        }

    return cleaned_results

def delete_experiment_results(experiment_name):
    filename = "results/results.json"

    if not os.path.exists(filename):
        return

    with open(filename, "r") as file:
        try:
            results = json.load(file)
        except json.JSONDecodeError:
            results = []

    remaining_results = [
        result
        for result in results
        if result["experiment"] != experiment_name
    ]

    with open(filename, "w") as file:
        json.dump(remaining_results, file, indent=4)