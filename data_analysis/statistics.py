import pandas as pd
import numpy as np

# Return a series of percentage returns
def percentage_returns(df):
    closing_values = pd.to_numeric(df["Close"])

    returns = closing_values.pct_change()
    returns = returns.rename("Percentage Returns")

    return returns

# Return a series of log returns
def log_returns(df):
    closing_values = pd.to_numeric(df["Close"])

    returns = np.log(closing_values / closing_values.shift(1))
    returns = returns.rename("Log Returns")

    return returns

def rolling_volatility(df, window):
    returns = percentage_returns(df)
    returns = returns.rename("Rolling volatility")

    return returns.rolling(window).std()

def simple_moving_average(df, window):
    closing_values = pd.to_numeric(df["Close"])

    moving_average = closing_values.rolling(window).mean()
    moving_average = moving_average.rename("Simple moving average")

    return moving_average

# Zero-centered
def pmar(df, window):
    sma = simple_moving_average(df, window)

    ratio_values = (df["Close"] - sma) / sma
    ratio_values = ratio_values.rename("Price Movement Average Ratio")

    return ratio_values

def percentage_momentum(df, window):
    closing_values = pd.to_numeric(df["Close"])

    momentum = (closing_values / closing_values.shift(window)) - 1
    momentum = momentum.rename("Momentum")

    return momentum

def daily_volume_change(df):
    volume_values = pd.to_numeric(df["Volume"])

    volume_change = volume_values.pct_change()
    volume_change = volume_change.rename("Volume change")

    return volume_change

def exponential_moving_average(df, window):
    closing_values = pd.to_numeric(df["Close"])

    moving_average = closing_values.ewm(span=window, adjust=False).mean()
    moving_average = moving_average.rename("Exponential moving average")

    return moving_average

def moving_average_difference(df, short_window, long_window):
    short_ma = simple_moving_average(df, short_window)
    long_ma = simple_moving_average(df, long_window)

    difference = short_ma - long_ma
    difference = difference.rename("MA difference")

    return difference

def rsi(df, window):
    closing_values = pd.to_numeric(df["Close"])

    differences = closing_values.diff()

    gains = differences.where(differences > 0, 0)
    losses = -differences.where(differences < 0, 0)

    avg_gains = gains.rolling(window).mean()
    avg_losses = losses.rolling(window).mean()
    relative_strength = avg_gains / avg_losses

    rsi_values = 100 - (100 / (1 + relative_strength))
    return rsi_values

def relative_daily_price_range(df):
    high_prices = pd.to_numeric(df["High"])
    low_prices = pd.to_numeric(df["Low"])
    closing_values = pd.to_numeric(df["Close"])

    price_range = (high_prices - low_prices) / closing_values
    price_range = price_range.rename("Daily price range")

    return price_range

def bollinger_position(df, window):
    closing_values = pd.to_numeric(df["Close"])

    middle_values = closing_values.rolling(window).mean()
    volatility = rolling_volatility(df, window)

    upper_band = middle_values + 2 * volatility
    lower_band = middle_values - 2 * volatility

    position = (closing_values - lower_band) / (upper_band - lower_band)
    position = position.rename("Bollinger position")

    return position