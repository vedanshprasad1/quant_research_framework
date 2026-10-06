import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def show_moving_average(moving_averages):
    plt.figure(figsize=(7, 7))

    plt.plot(moving_averages.index, moving_averages, label="Moving Average")
    plt.legend()

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.xticks(rotation=45)

    plt.xlabel("Date")
    plt.ylabel("Moving Average")