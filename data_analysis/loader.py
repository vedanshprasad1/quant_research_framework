import pandas as pd

def load_data(ticker):
    df = pd.read_csv(f"data/downloads/{ticker}.csv", parse_dates=["Date"], index_col="Date")

    return df