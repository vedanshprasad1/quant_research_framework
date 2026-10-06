from experiments.experiment_manager import load_experiments

def create_experiment(ticker, start_date, end_date, split_date):
    choices = []

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
    print("20. End Choice Selection")

    choice = input("Enter the number of the feature you want to include: ")
    while choice != "20" or not choices:
        if not choices and choice == "20":
            print("Select at least one feature")
        else:
            if choice.isnumeric():
                choice = int(choice)
                if choice <= 12 and choice > 0:
                    if choice not in choices:
                        choices.append(choice)
                        print("Feature added")
                    else:
                        print("Feature already included")
                else:
                    print("Invalid choice")
            else:
                print("Invalid choice")

        choice = input("\nEnter the number of the feature you want to include: ")

    features = []

    for choice in choices:
        match choice:
            case 1:
                features.append("percentage_return")
            case 2:
                features.append("log_return")
            case 3:
                features.append("sma")
            case 4:
                features.append("pmar")
            case 5:
                features.append("rv")
            case 6:
                features.append("momentum")
            case 7:
                features.append("volume")
            case 8:
                features.append("ema")
            case 9:
                features.append("ma_diff")
            case 10:
                features.append("rsi")
            case 11:
                features.append("daily_price_range")
            case 12:
                features.append("bollinger")

    configs = {
        "moving_average_window": 20,
        "rolling_volatility_window": 30,
        "momentum_window": 10,
        "ma_diff_short": 5,
        "ma_diff_long": 20,
        "rsi_window": 14,
        "bollinger_window": 20
        }

    if 3 in choices or 8 in choices:
        valid_value = False
        while not valid_value:
            configs["moving_average_window"] = input("Enter the time window for moving averages: ")
            if configs["moving_average_window"].isnumeric():
                configs["moving_average_window"] = int(configs["moving_average_window"])
                valid_value = True
            else:
                print("Invalid value, enter a number")

    if 5 in choices:
        valid_value = False
        while not valid_value:
            configs["rolling_volatility_window"] = input("Enter the time window for rolling volatility: ")
            if configs["rolling_volatility_window"].isnumeric():
                configs["rolling_volatility_window"] = int(configs["rolling_volatility_window"])
                valid_value = True
            else:
                print("Invalid value, enter a number")

    if 6 in choices:
        valid_value = False
        while not valid_value:
            configs["momentum_window"] = input("Enter the time window for momentum: ")
            if configs["momentum_window"].isnumeric():
                configs["momentum_window"] = int(configs["momentum_window"])
                valid_value = True
            else:
                print("Invalid value, enter a number")

    if 9 in choices:
        valid_value = False
        while not valid_value:
            configs["ma_diff_short"] = input("Enter the time window for the short-term average for moving average difference: ")
            if configs["ma_diff_short"].isnumeric():
                configs["ma_diff_short"] = int(configs["ma_diff_short"])
                valid_value = True
            else:
                print("Invalid value, enter a number")

        valid_value = False
        while not valid_value:
            configs["ma_diff_long"] = input("Enter the time window for the long-term average for moving average difference: ")
            if configs["ma_diff_long"].isnumeric():
                configs["ma_diff_long"] = int(configs["ma_diff_long"])
                valid_value = True
            else:
                print("Invalid value, enter a number")

    if 10 in choices:
        valid_value = False
        while not valid_value:
            configs["rsi_window"] = input("Enter the time window for RSI: ")
            if configs["rsi_window"].isnumeric():
                configs["rsi_window"] = int(configs["rsi_window"])
                valid_value = True
            else:
                print("Invalid value, enter a number")

    if 12 in choices:
        valid_value = False
        while not valid_value:
            configs["bollinger_window"] = input("Enter the time window for bollinger bands: ")
            if configs["bollinger_window"].isnumeric():
                configs["bollinger_window"] = int(configs["bollinger_window"])
                valid_value = True
            else:
                print("Invalid value, enter a number")

    model_choices = []

    print()
    print("Choices of models:")
    print("1. Logistic Regression")
    print("2. Linear Regression")
    print("3. Random Forest Classifier")
    print("4. Random Forest Regressor")
    print("5. Gradient Boosting Classifier")
    print("6. Gradient Boosting Regressor")
    print("7. Sequential Classifier")
    print("8. Sequential Regressor")
    print("20. End Choice Selection")

    choice = input("Enter the number of the model you want to include: ")
    while choice != "20" or not model_choices:
        if not model_choices and choice == "20":
            print("Select at least one model")
        else:
            if choice.isnumeric():
                choice = int(choice)
                if choice <= 8 and choice > 0:
                    if choice not in model_choices:
                        model_choices.append(choice)
                        print("Model added")
                    else:
                        print("Model already included")
                else:
                    print("Invalid choice")
            else:
                print("Invalid choice")

        choice = input("\nEnter the number of the model you want to include: ")

    models = []

    for choice in model_choices:
        match choice:
            case 1:
                models.append("logistic_regression")
            case 2:
                models.append("linear_regression")
            case 3:
                models.append("random_forest")
            case 4:
                models.append("random_forest_regressor")
            case 5:
                models.append("gradient_boosting")
            case 6:
                models.append("gradient_boosting_regressor")
            case 7:
                models.append("ffnn_classifier")
            case 8:
                models.append("ffnn_regressor")

    valid_value = False
    while not valid_value:
        capital = input("Enter initial capital amount: ")
        if capital.isnumeric():
            capital = int(capital)
            valid_value = True
        else:
            print("Invalid value entered")

    confidence_threshold = 0
    regression_threshold = 0

    for choice in model_choices:
        if choice in [1, 3, 5, 7]:
            valid_value = False
            while not valid_value:
                confidence_threshold = input("Enter value for confidence threshold for testing: ")
                try:
                    if float(confidence_threshold) <= 1 and float(confidence_threshold) >= 0:
                        valid_value = True
                        confidence_threshold = float(confidence_threshold)
                        break
                except:
                    print("Invalid value entered")

            break

    for choice in model_choices:
        if choice in [2, 4, 6, 8]:
            valid_value = False
            while not valid_value:
                regression_threshold = input("Enter value for regression threshold for testing: ")
                try:
                    if float(regression_threshold) >= 0:
                        valid_value = True
                        regression_threshold = float(regression_threshold)
                        break
                except:
                    print("Invalid value entered")

            break

    experiments = load_experiments()

    while True:
        experiment_name = input("Enter a name for the experiment: ")

        matching_experiments = [
            experiment
            for experiment in experiments
            if experiment["name"] == experiment_name
        ]

        if not matching_experiments:
            break

        print()
        print(f"An experiment named '{experiment_name}' already exists.")
        print("1. Replace existing experiment")
        print("2. Choose a different name")
        print("3. Cancel")

        choice = input("Enter your choice: ")

        if choice == "1":
            break

        elif choice == "2":
            continue

        elif choice == "3":
            print("Experiment creation cancelled.")
            return None

        else:
            print("Invalid choice.")

    experiment = {
        "name": experiment_name,
        "stock": ticker,
        "features": features,
        "configs": configs,
        "models": models,
        "split_date": split_date,
        "start_date": start_date,
        "end_date": end_date,
        "capital": capital,
        "confidence_threshold": confidence_threshold,
        "regression_threshold": regression_threshold
    }

    return experiment