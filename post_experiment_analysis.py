from model_analysis.results_table import show_results_table, create_results_table, csv_results
from statistical_tests.hypothesis_testing import feature_t_test
from statistical_tests.ttest_all_features import ttest_all_features
from statistical_tests.ttest_report import ttest_report
from statistical_tests.correlation import features_pearson_correlation, target_pearson_correlation
from data.prediction_data import download_prediction_data
from features.feature_builder import build_features

def post_run_analysis(features, classification_analysis, regression_analysis, trained_models, experiment):
    model_table, backtest_table = create_results_table(experiment["name"])

    print()
    print("Choices:")
    print("1. View Experiment Results")
    print("2. Save Results")
    print("3. T-Test Analysis")
    print("4. Pearson Correlation")
    print("5. Feature Importance")
    print("6. Compare Experiments")
    print("7. Predict Future Trading Day")
    print("10. End Post Experiment Analysis")

    choice = input("Enter number of choice: ")

    while choice != "10":
        if choice == "1":
            show_results_table(model_table, backtest_table)
            
        elif choice == "2":
            csv_results(model_table, backtest_table)

        elif choice == "3":
            ttest_analysis(features)

        elif choice == "4":
            pearson_correlation(features)

        elif choice == "5":
            feature_importance(classification_analysis, regression_analysis)

        elif choice == "6":
            all_model_table, all_backtest_table = create_results_table()
            compare_experiments(all_model_table, all_backtest_table)

        elif choice == "7":
            print()
            print("FUTURE TRADING DAY PREDICTION")
            print("-----------------------------")

            prediction_date = input(
                "Enter prediction date (YYYY-MM-DD): "
            )

            predict_future_day(
                experiment,
                trained_models,
                prediction_date
            )

        else:
            print("Invalid choice")

        print()
        print("Choices:")
        print("1. View Experiment Results")
        print("2. Save Results")
        print("3. T-Test Analysis")
        print("4. Pearson Correlation")
        print("5. Feature Importance")
        print("6. Compare Experiments")
        print("7. Predict Future Trading Day")
        print("10. End Post Experiment Analysis")

        choice = input("Enter number of choice: ")

def ttest_analysis(features):
    print()
    print("T-TEST ANALYSIS")
    print("----------------")
    print("1. Test a specific feature")
    print("2. Test all features")
    print("10. Return")

    choice = input("Enter number of choice: ")

    while choice != "10":

        if choice == "1":
            print()
            print("Available features:")

            available_features = features.drop(["future_return", "target"], axis=1).columns

            print()
            print("Available features:")
            for i, feature in enumerate(available_features, start=1):
                print(f"{i}. {feature}")

            choice = input("Enter the feature number: ")

            try:
                choice = int(choice)

                if choice < 1 or choice > len(available_features):
                    print("Invalid feature number.")
                    return

                feature_name = available_features[choice - 1]

                test_statistic, p_value, low_mean, high_mean = feature_t_test(
                    features,
                    feature_name
                )

                ttest_report(
                    feature_name,
                    test_statistic,
                    p_value,
                    low_mean,
                    high_mean
                )

            except:
                print("Invalid choice.")
                return            

        elif choice == "2":
            results = ttest_all_features(features)

            print()
            print(results)

        else:
            print("Invalid choice.")

        print()
        print("T-TEST ANALYSIS")
        print("----------------")
        print("1. Test a specific feature")
        print("2. Test all features")
        print("10. Return")

        choice = input("Enter number of choice: ")

def pearson_correlation(features):
    print()
    print("PEARSON CORRELATION")
    print("-------------------")
    print("1. Feature correlation heatmap")
    print("2. Feature correlation with future return")
    print("10. Return")

    choice = input("Enter number of choice: ")

    while choice != "10":

        if choice == "1":
            features_pearson_correlation(features)

        elif choice == "2":
            print(target_pearson_correlation(features))

        else:
            print("Invalid choice")

        print()
        print("PEARSON CORRELATION")
        print("-------------------")
        print("1. Feature correlation heatmap")
        print("2. Feature correlation with future return")
        print("10. Return")

        choice = input("Enter number of choice: ")

def feature_importance(classification_analysis, regression_analysis):
    print()
    print("FEATURE IMPORTANCE")
    print("------------------")
    print("1. View Classification Feature Analysis")
    print("2. View Regression Feature Analysis")
    print("10. Return")

    choice = input("Enter number of choice: ")

    while choice != "10":

        if choice == "1":
            if classification_analysis is not None:
                print()
                print(classification_analysis)
            else:
                print("No classification analysis available.")

        elif choice == "2":
            if regression_analysis is not None:
                print()
                print(regression_analysis)
            else:
                print("No regression analysis available.")

        else:
            print("Invalid choice.")

        print()
        print("FEATURE IMPORTANCE")
        print("------------------")
        print("1. View Classification Feature Analysis")
        print("2. View Regression Feature Analysis")
        print("10. Return")

        choice = input("Enter number of choice: ")

def compare_experiments(model_table, backtest_table):
    print()
    print("AVAILABLE EXPERIMENTS")
    print("---------------------")

    experiments = model_table["experiment"].unique()

    for i, experiment in enumerate(experiments, start=1):
        print(f"{i}. {experiment}")

    print()
    choice = input("Enter experiment numbers separated by commas and no spaces: ")

    try:
        selected_numbers = [
            int(number.strip())
            for number in choice.split(",")
        ]
    except:
        print("Invalid input")
        return

    if len(selected_numbers) < 2:
        print("Select at least two experiments.")
        return

    if any(
        number < 1 or number > len(experiments)
        for number in selected_numbers
    ):
        print("Invalid experiment number.")
        return

    selected_experiments = [
        experiments[number - 1]
        for number in selected_numbers
    ]

    selected_model_table = model_table[
        model_table["experiment"].isin(selected_experiments)
    ]

    selected_backtest_table = backtest_table[
        backtest_table["experiment"].isin(selected_experiments)
    ]

    print()
    print("MODEL COMPARISON")
    print("----------------")

    print(selected_model_table.to_string(index=False))

    print()
    print("BACKTEST COMPARISON")
    print("-------------------")

    print(selected_backtest_table.to_string(index=False))

def predict_future_day(experiment_settings, trained_models, prediction_date):
    ticker = experiment_settings["stock"]
    start_date = experiment_settings["start_date"]
    feature_names = experiment_settings["features"]
    configs = experiment_settings["configs"]

    data = download_prediction_data(ticker,start_date,prediction_date)

    if data is None:
        return

    features = build_features(data,feature_names,configs)

    latest_features = features.iloc[[-1]][feature_names]

    if latest_features.isna().any().any():
        print("Unable to generate prediction because required features contain missing values.")
        return

    print()
    print(f"PREDICTIONS FOR {prediction_date}")
    print("-----------------------------")

    classification_models = [
        "logistic_regression",
        "random_forest",
        "gradient_boosting",
        "ffnn_classifier"
    ]

    for model_name in classification_models:
        model_info = trained_models[model_name]

        model = model_info["model"]
        scaler = model_info["scaler"]

        if model is None:
            continue

        model_features = latest_features.copy()

        if scaler is not None:
            model_features = scaler.transform(model_features)

        if model_name == "ffnn_classifier":
            probability = model.predict(model_features, verbose=0).flatten()[0]
            prediction = int(probability >= 0.5)
        else:
            prediction = model.predict(model_features)[0]
            probability = model.predict_proba(model_features)[0][1]

        if prediction == 1:
            direction = "UP"
        else:
            direction = "DOWN"

        print()
        print(model_name)
        print(f"Predicted direction: {direction}")
        print(f"Confidence: {probability:.2%}")

        regression_models = [
        "linear_regression",
        "random_forest_regressor",
        "gradient_boosting_regressor",
        "ffnn_regressor"
    ]

    for model_name in regression_models:
        model_info = trained_models[model_name]

        model = model_info["model"]
        scaler = model_info["scaler"]

        if model is None:
            continue

        model_features = latest_features.copy()

        if scaler is not None:
            model_features = scaler.transform(model_features)

        prediction = model.predict(model_features)

        if hasattr(prediction, "flatten"):
            prediction = prediction.flatten()[0]
        else:
            prediction = prediction[0]

        if prediction > 0:
            direction = "UP"
        else:
            direction = "DOWN"

        print()
        print(model_name)
        print(f"Predicted return: {prediction:.2%}")
        print(f"Predicted direction: {direction}")