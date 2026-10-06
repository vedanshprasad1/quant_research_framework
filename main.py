import matplotlib.pyplot as plt
import numpy as np
from data.downloader import download_data
from data_analysis.loader import load_data
from visualisation.stock_price import show_stock_price_graph
from visualisation.moving_average import show_moving_average
from visualisation.returns_distribution import show_returns_distribution
from visualisation.rolling_volatility import show_rolling_volatility
from visualisation.feature_distribution import get_feature_choice, feature_distribution
from features.feature_builder import build_features
from experiments.experiment_runner import run_experiment
from experiments.experiment_creator import create_experiment
from experiments.experiment_manager import save_experiment
from post_experiment_analysis import post_run_analysis
from experiments.experiment_manager import choose_experiment, remove_experiment

np.set_printoptions(legacy="1.25")

program_running = True

def experiment_menu(experiment):
    df = load_data(experiment["stock"])

    features = build_features(df, experiment["features"], experiment["configs"])
    features = features.dropna()

    print("Choices:")
    print("1. Show Stock Price History")
    print("2. Show Returns Distribution")
    print("3. Show Simple Moving Average Graph")
    print("4. Show Exponential Moving Average Graph")
    print("5. Show Rolling Volatility Distribution")
    print("6. Show Distribution of a Feature")
    print("7. Run Experiment")
    print("10. Main Menu")

    choice = input("Enter choice number: ")
    while choice != "10":
        if choice == "1":
            show_stock_price_graph(df)
        elif choice == "2":
            show_returns_distribution(features["percentage_return"])
        elif choice == "3":
            show_moving_average(features["sma"])
        elif choice == "4":
            show_moving_average(features["ema"])
        elif choice == "5":
            show_rolling_volatility(features["rv"])
        elif choice == "6":
            feature_choice = get_feature_choice()
            feature_distribution(features[feature_choice])
        elif choice == "7":
            print("EXPERIMENT", experiment["name"].upper())
            classification_analysis, regression_analysis, trained_models = run_experiment(df, experiment, features, ticker)

            print()
            print("Ran Experiment")

            post_run_analysis(features, classification_analysis, regression_analysis, trained_models, experiment)

            print()
            print("Returning to main menu")
            print()

        elif choice == "10":
            break
        else:
            print("Invalid choice")

        plt.show(block=False)
        plt.pause(0.1)
        print()
        print("Choices:")
        print("1. Show Stock Price History")
        print("2. Show Returns Distribution")
        print("3. Show Simple Moving Average Graph")
        print("4. Show Exponential Moving Average Graph")
        print("5. Show Rolling Volatility Distribution")
        print("6. Show Distribution of a Feature")
        print("7. Run Experiment")
        print("10. Main Menu")
        choice = input("Enter choice number: ")

while program_running:
    print()
    print("QUANTITATIVE TRADING RESEARCH PLATFORM")
    print("---------------------------------------")
    print("1. Create New Experiment")
    print("2. Load Existing Experiment")
    print("3. Delete Experiment")
    print("10. Exit")

    choice = input("Enter choice number: ")

    if choice == "1":
        # Get ticker and download data
        while True:
            ticker = input("Enter ticker symbol: ").upper()
    
            start_date = input("Enter start date in format YYYY-MM-DD: ")
            end_date = input("Enter end date in format YYYY-MM-DD: ")
            split_date = input("Enter the date to split the data between training and testing in format YYYY-MM-DD: ")
            print()
    
            if download_data(ticker, start_date, end_date):
                break
    
        experiment = create_experiment(ticker, start_date, end_date, split_date)
        if not experiment:
            continue
        save_experiment(experiment)
    
        print("\nExperiment created\n")

        experiment_menu(experiment)

    elif choice == "2":
        experiment = choose_experiment()

        if experiment is None:
            continue

        ticker = experiment["stock"]

        start_date = experiment["start_date"]
        end_date = experiment["end_date"]

        if not download_data(ticker, start_date, end_date):
            print("Could not download experiment data.")
            continue

        experiment_menu(experiment)

    elif choice == "3":
        remove_experiment()

    elif choice == "10":
        program_running = False

    else:
        print("Invalid choice")