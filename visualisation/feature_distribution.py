import matplotlib.pyplot as plt

def get_feature_choice():
    print()
    print("Choices of features:")
    print("1. Percentage Return")
    print("2. Log Return")
    print("3. Simple Moving Average")
    print("4. Price Movement Average Ratio")
    print("5. Rolling Volatility")
    print("6. Momentum")
    print("7. Volume Traded")
    print("8. Exponential Moving Average")
    print("9. Moving Average Difference")
    print("10. Relative Strength Index")
    print("11. Daily Price Range")
    print("12. Bollinger Bands")

    while True:
        choice = input("Enter the number of the feature you want to see the distribution of: ")
        match choice:
            case "1":
                return "percentage_return"
            case "2":
                return "log_return"
            case "3":
                return "sma"
            case "4":
                return "pmar"
            case "5":
                return "rv"
            case "6":
                return "momentum"
            case "7":
                return "volume"
            case "8":
                return "ema"
            case "9":
                return "ma_diff"
            case "10":
                return "rsi"
            case "11":
                return "daily_price_range"
            case "12":
                return "bollinger"
            case _:
                print("Invalid choice")

def feature_distribution(feature):
    plt.figure(figsize=(7,7))
    feature_name = feature.name.capitalize()
    print(feature_name)

    plt.hist(feature, bins=50)

    plt.title(f"{feature_name} Distribution")
    plt.xlabel(feature_name.capitalize())
    plt.ylabel("Frequency")