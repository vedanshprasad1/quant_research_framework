from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor

def gradient_boosting_model(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["target"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["target"]

    model = GradientBoostingClassifier(n_estimators=300, learning_rate=0.05, random_state=100, max_features=5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]

    return model, None, X_test, y_test, y_pred, y_prob

def gradient_boosting_regressor(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["future_return"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["future_return"]

    model = GradientBoostingRegressor(n_estimators=300, learning_rate=0.05, random_state=100, max_features=5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    return model, None, X_test, y_test, y_pred