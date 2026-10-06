import yfinance as yf

# Get data for the stock ticker and store to csv
def download_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=True
    )

    if data.empty:
        print("Invalid value(s) entered")
        return False

    data.columns = data.columns.droplevel(1)

    data.to_csv(f"data/downloads/{ticker}.csv")
    return True