import numpy as np

def sharpe_ratio(capital_history):
    returns = capital_history.pct_change().dropna()

    std = returns.std()

    if std == 0:
        return 0

    return (returns.mean() / std) * np.sqrt(252) # Will need to config this number

def maximum_drawdown(capital_history):
    running_maximum = capital_history.cummax()
    drawdowns = (capital_history - running_maximum) / running_maximum

    return drawdowns.min()