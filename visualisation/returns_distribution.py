import matplotlib.pyplot as plt

def show_returns_distribution(returns):
    plt.figure(figsize=(7,7))

    plt.hist(
        returns.dropna(),
        bins=50
    )

    plt.title("Returns Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Number of days")