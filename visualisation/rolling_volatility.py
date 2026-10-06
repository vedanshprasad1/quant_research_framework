import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def show_rolling_volatility(rolling_volatility):
    plt.figure(figsize=(7, 7))

    plt.plot(rolling_volatility.index, rolling_volatility, label="Rolling Volatility")
    plt.legend()

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.xticks(rotation=45)

    plt.title("Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")