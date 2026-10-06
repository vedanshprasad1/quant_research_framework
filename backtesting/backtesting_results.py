from backtesting.backtester import simple_buying, buy_and_hold, random_buying, confidence_buying, threshold_buying
from backtesting.metrics import sharpe_ratio, maximum_drawdown

def show_classification_backtest_results(experiment_settings, backtest_data, predicted_values, probabilities):
    backtest_results = {}
    
    backtest_results["Simple Buying"] = simple_buying(experiment_settings["capital"], backtest_data["future_return"], predicted_values)
    backtest_results["Simple Buying"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Simple Buying"]["capital_history"])
    backtest_results["Simple Buying"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Simple Buying"]["capital_history"])

    backtest_results["Buy and Hold"] = buy_and_hold(experiment_settings["capital"], backtest_data["future_return"])
    backtest_results["Buy and Hold"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Buy and Hold"]["capital_history"])
    backtest_results["Buy and Hold"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Buy and Hold"]["capital_history"])

    backtest_results["Random Buying"] = random_buying(experiment_settings["capital"], backtest_data["future_return"])
    backtest_results["Random Buying"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Random Buying"]["capital_history"])
    backtest_results["Random Buying"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Random Buying"]["capital_history"])

    backtest_results["Confidence Buying"] = confidence_buying(experiment_settings["capital"], backtest_data["future_return"], probabilities, experiment_settings["confidence_threshold"])
    backtest_results["Confidence Buying"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Confidence Buying"]["capital_history"])
    backtest_results["Confidence Buying"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Confidence Buying"]["capital_history"])
    
    print()
    print("BACKTESTING RESULT\n")
    print("Simple Buying")
    print("Profit:", backtest_results["Simple Buying"]["profit"])
    print("Final capital value:", backtest_results["Simple Buying"]["final_capital"])
    print("Number of trades:", backtest_results["Simple Buying"]["number_of_trades"])
    print("Sharpe ratio:", backtest_results["Simple Buying"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Simple Buying"]["maximum_drawdown"])
    print("\nBuy and Hold")
    print("Profit:", backtest_results["Buy and Hold"]["profit"])
    print("Final capital value:", backtest_results["Buy and Hold"]["final_capital"])
    print("Sharpe ratio:", backtest_results["Buy and Hold"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Buy and Hold"]["maximum_drawdown"])
    print("\nRandom Buying")
    print("Profit:", backtest_results["Random Buying"]["profit"])
    print("Final capital value:", backtest_results["Random Buying"]["final_capital"])
    print("Number of trades:", backtest_results["Random Buying"]["number_of_trades"])
    print("Sharpe ratio:", backtest_results["Random Buying"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Random Buying"]["maximum_drawdown"])
    print("\nConfidence Buying")
    print("Profit:", backtest_results["Confidence Buying"]["profit"])
    print("Final capital value:", backtest_results["Confidence Buying"]["final_capital"])
    print("Number of trades:", backtest_results["Confidence Buying"]["number_of_trades"])
    print("Sharpe ratio:", backtest_results["Confidence Buying"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Confidence Buying"]["maximum_drawdown"])
    print()

    return backtest_results

def show_regression_backtest_results(experiment_settings, backtest_data, predicted_values):
    backtest_results = {}

    backtest_results["Simple Buying"] = simple_buying(experiment_settings["capital"], backtest_data["future_return"], predicted_values)
    backtest_results["Simple Buying"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Simple Buying"]["capital_history"])
    backtest_results["Simple Buying"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Simple Buying"]["capital_history"])

    backtest_results["Buy and Hold"] = buy_and_hold(experiment_settings["capital"], backtest_data["future_return"])
    backtest_results["Buy and Hold"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Buy and Hold"]["capital_history"])
    backtest_results["Buy and Hold"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Buy and Hold"]["capital_history"])

    backtest_results["Random Buying"] = random_buying(experiment_settings["capital"], backtest_data["future_return"])
    backtest_results["Random Buying"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Random Buying"]["capital_history"])
    backtest_results["Random Buying"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Random Buying"]["capital_history"])

    backtest_results["Threshold Buying"] = threshold_buying(experiment_settings["capital"], backtest_data["future_return"], predicted_values, experiment_settings["regression_threshold"])
    backtest_results["Threshold Buying"]["sharpe_ratio"] = sharpe_ratio(backtest_results["Threshold Buying"]["capital_history"])
    backtest_results["Threshold Buying"]["maximum_drawdown"] = maximum_drawdown(backtest_results["Threshold Buying"]["capital_history"])

    print()
    print("BACKTESTING RESULT\n")
    print("Simple Buying")
    print("Profit:", backtest_results["Simple Buying"]["profit"])
    print("Final capital value:", backtest_results["Simple Buying"]["final_capital"])
    print("Number of trades:", backtest_results["Simple Buying"]["number_of_trades"])
    print("Sharpe ratio:", backtest_results["Simple Buying"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Simple Buying"]["maximum_drawdown"])
    print("\nBuy and Hold")
    print("Profit:", backtest_results["Buy and Hold"]["profit"])
    print("Final capital value:", backtest_results["Buy and Hold"]["final_capital"])
    print("Sharpe ratio:", backtest_results["Buy and Hold"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Buy and Hold"]["maximum_drawdown"])
    print("\nRandom Buying")
    print("Profit:", backtest_results["Random Buying"]["profit"])
    print("Final capital value:", backtest_results["Random Buying"]["final_capital"])
    print("Number of trades:", backtest_results["Random Buying"]["number_of_trades"])
    print("Sharpe ratio:", backtest_results["Random Buying"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Random Buying"]["maximum_drawdown"])
    print("\nThreshold Buying")
    print("Profit:", backtest_results["Threshold Buying"]["profit"])
    print("Final capital value:", backtest_results["Threshold Buying"]["final_capital"])
    print("Number of trades:", backtest_results["Threshold Buying"]["number_of_trades"])
    print("Sharpe ratio:", backtest_results["Threshold Buying"]["sharpe_ratio"])
    print("Maximum drawdown:", backtest_results["Threshold Buying"]["maximum_drawdown"])
    print()

    return backtest_results