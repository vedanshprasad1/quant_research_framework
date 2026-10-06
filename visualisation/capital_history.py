import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def show_capital_history(backtest_results, model, problem_type):
    plt.figure(figsize=(7,7))

    for strategy_name, result in backtest_results.items():
        if strategy_name == "Buy and Hold":
            plt.plot(result["capital_history"].index, result["capital_history"], label=strategy_name, linewidth=3)
        else:
            plt.plot(result["capital_history"].index, result["capital_history"], label=strategy_name)

    plt.legend()

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.xticks(rotation=45)

    plt.title(f"Backtesting strategies for {type(model).__name__} ({problem_type})")
    plt.xlabel("Date")
    plt.ylabel("Capital value")