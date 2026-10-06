import pandas as pd
from random import randint

def simple_buying(capital, returns, predicted_values):
    trade_mask = predicted_values > 0

    initial_capital = capital

    capital_history = []
    
    for date, value in returns.items():
        if trade_mask.loc[date]:
            capital *= (1 + value)
        capital_history.append(capital)
    
    capital_history = pd.Series(capital_history, index=returns.index)
    capital_history = capital_history.rename("Simple Buying Capital History")

    profit = capital - initial_capital
    return {"profit": profit,
            "final_capital": capital, 
            "number_of_trades": int(trade_mask.sum()),
            "capital_history": capital_history
            }

def confidence_buying(capital, returns, probabilities, threshold):
    trade_mask = probabilities > threshold

    initial_capital = capital

    capital_history = []

    for date, value in returns.items():
        if trade_mask.loc[date]:
            capital *= (1 + value)
        capital_history.append(capital)

    capital_history = pd.Series(capital_history, index=returns.index)
    capital_history = capital_history.rename("Confidence Buying Capital History")

    profit = capital - initial_capital
    return {"profit": profit,
            "final_capital": capital,
            "number_of_trades": int(trade_mask.sum()),
            "capital_history": capital_history}

def buy_and_hold(capital, returns):
    initial_capital = capital

    capital_history = []

    for value in returns:
        capital *= (1 + value)
        capital_history.append(capital)

    capital_history = pd.Series(capital_history, index=returns.index)
    capital_history = capital_history.rename("Buy & Hold Capital History")

    profit = capital - initial_capital

    return {"profit": profit,
            "final_capital": capital,
            "capital_history": capital_history}

def random_buying(capital, returns):
    initial_capital = capital

    capital_history = []

    mask = pd.Series([randint(0, 1) for _ in range(len(returns))], index=returns.index).astype(bool)

    chosen_returns = returns[mask]

    for value in chosen_returns:
        capital *= (1 + value)
        capital_history.append(capital)

    capital_history = pd.Series(capital_history, index=chosen_returns.index)

    profit = capital - initial_capital

    return {"profit": profit,
            "final_capital": capital,
            "number_of_trades": int(mask.sum()),
            "capital_history": capital_history}

def threshold_buying(capital, returns, predicted_values, threshold):
    trade_mask = predicted_values > threshold

    initial_capital = capital
    
    capital_history = []

    for date, value in returns.items():
        if trade_mask.loc[date]:
            capital *= (1 + value)
        capital_history.append(capital)

    capital_history = pd.Series(capital_history, index=returns.index)
    capital_history = capital_history.rename("Threshold Buying Capital History")

    profit = capital - initial_capital
    return {"profit": profit,
            "final_capital": capital,
            "number_of_trades": int(trade_mask.sum()),
            "capital_history": capital_history}