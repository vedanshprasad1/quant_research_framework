from data_analysis.statistics import percentage_returns, log_returns, rolling_volatility, simple_moving_average, pmar, percentage_momentum, daily_volume_change, exponential_moving_average, moving_average_difference, rsi, relative_daily_price_range, bollinger_position
import pandas as pd

def build_features(df, features, configs):
    features_data = pd.DataFrame(index=df.index)

    features_data["percentage_return"] = percentage_returns(df)

    features_data["log_return"] = log_returns(df)
    
    features_data["sma"] = simple_moving_average(df, configs["moving_average_window"])

    features_data["pmar"] = pmar(df, configs["moving_average_window"])
    
    features_data["rv"] = rolling_volatility(df, configs["rolling_volatility_window"])
    
    features_data["momentum"] = percentage_momentum(df, configs["momentum_window"])

    features_data["volume"] = daily_volume_change(df)

    features_data["ema"] = exponential_moving_average(df, configs["moving_average_window"])

    features_data["ma_diff"] = moving_average_difference(df, configs["ma_diff_short"], configs["ma_diff_long"])

    features_data["rsi"] = rsi(df, configs["rsi_window"])

    features_data["daily_price_range"] = relative_daily_price_range(df)
    
    features_data["bollinger"] = bollinger_position(df, configs["bollinger_window"])

    features_data["future_return"] = features_data["percentage_return"].shift(-1)
    features_data["target"] = features_data["future_return"] > 0

    return features_data