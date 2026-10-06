import yfinance as yf

def download_prediction_data(ticker, start_date, prediction_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=prediction_date,
        progress=False,
        auto_adjust=True
    )

    if data.empty:
        print("Could not download prediction data.")
        return None

    data.columns = data.columns.droplevel(1)

    return data