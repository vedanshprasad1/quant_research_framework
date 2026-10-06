import json
import os
import pandas as pd

def create_results_table(experiment_name=None):
    filename = "results/results.json"

    if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    results = json.load(file)
                except json.JSONDecodeError:
                    results = []
    else:
        return None

    if experiment_name:
        results = [
            result
            for result in results
            if result["experiment"] == experiment_name
        ]

    rows = []

    for result in results:
        row = {
             "model": result["model"],
             "problem type": result["problem type"],
             "experiment": result["experiment"],
             "stock": result["stock"],
             "accuracy": result.get("accuracy"),
             "precision": result.get("precision"),
             "recall": result.get("recall"),
             "f1": result.get("f1"),
             "mean absolute error": result.get("mean absolute error"),
             "root mean square error": result.get("root mean square error"),
             "r2": result.get("r2"),
             "directional accuracy": result.get("directional accuracy")
        }

        rows.append(row)

    model_table = pd.DataFrame(rows)

    rows = []

    for result in results:
        for strategy, backtest in result["backtest_results"].items():
             row = {
                "model": result["model"],
                "problem type": result["problem type"],
                "experiment": result["experiment"],
                "stock": result["stock"],
                "strategy": strategy,
                "profit": backtest.get("profit"),
                "final capital": backtest.get("final_capital"),
                "trades": backtest.get("number_of_trades"),
                "sharpe ratio": backtest.get("sharpe_ratio"),
                "maximum drawdown": backtest.get("maximum_drawdown")
             }

             rows.append(row)

    backtest_table = pd.DataFrame(rows)
    
    return model_table, backtest_table

def show_results_table(model_table, backtest_table):
    print()
    print("MODEL TABLE")
    print()

    print(model_table)

    print()
    print("BACKTEST TABLE")
    print()

    print(backtest_table)

def csv_results(model_table, backtest_table):
    confirmation = input("Save results as CSV? (Y/N) ")

    if confirmation.upper() == "Y":
        model_table.to_csv("results/models.csv", index=False)

        backtest_table.to_csv("results/backtesting.csv", index=False)