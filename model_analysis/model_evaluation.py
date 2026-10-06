from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

def evaluate_classification_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)

    # How many predicted positives are correct
    precision = precision_score(y_test, y_pred)

    # How many actual positives the model identified
    recall = recall_score(y_test, y_pred)

    # Balance of recall and precision
    f1 = f1_score(y_test, y_pred)

    matrix = confusion_matrix(y_test, y_pred)

    value_counts = y_test.value_counts()

    return value_counts, accuracy, precision, recall, f1, matrix

def evaluate_regression_model(y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)

    rmse = root_mean_squared_error(y_test, y_pred)

    r2 = r2_score(y_test, y_pred)

    correct_directions = (y_test > 0) == (y_pred > 0)
    directional_accuracy = correct_directions.mean()

    return mae, rmse, r2, directional_accuracy