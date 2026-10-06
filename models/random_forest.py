from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

def random_forest_model(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["target"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["target"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]

    return model, None, X_test, y_test, y_pred, y_prob

def random_forest_regressor(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["future_return"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["future_return"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    return model, None, X_test, y_test, y_pred