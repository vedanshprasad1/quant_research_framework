from model_analysis.baseline import random_guessing, majority_voting

def classification_model_report(model, ticker, value_counts, accuracy, precision, recall, f1, matrix):
    print("--------------------")
    print("MODEL EVALUATION")
    print("--------------------\n")

    print("Model:", type(model).__name__)
    print("Stock:", ticker)

    print(f"\nAccuracy: {round(accuracy, 2)}\n")
    print(f"Precision: {round(precision, 2)}\n")
    print(f"Recall: {round(recall, 2)}\n")
    print(f"f1: {round(f1, 2)}\n")

    print("Confusion matrix:")
    print(matrix)

    print(f"\nBetter than random guessing: {random_guessing(accuracy)}")
    print(f"\nBetter than majority guessing: {majority_voting(accuracy, value_counts)}\n")

def regression_model_report(model, ticker, mae, rmse, r2, directional_accuracy):
    print("--------------------")
    print("MODEL EVALUATION")
    print("--------------------\n")

    print("Model:", type(model).__name__)
    print("Stock:", ticker)

    print(f"\nMean Absolute Error: {round(mae, 2)}\n")
    print(f"Root Mean Square Error: {round(rmse, 2)}\n")
    print(f"R2 score: {round(r2, 2)}\n")
    print(f"Directional Accuracy: {round(directional_accuracy, 2)}\n")