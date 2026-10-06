from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

def logistic_regression_model(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["target"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["target"]

    scaler = StandardScaler()
    
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]

    return model, scaler, X_test, y_test, y_pred, y_prob

def linear_regression_model(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["future_return"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["future_return"]

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    return model, scaler, X_test, y_test, y_pred