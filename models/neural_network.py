from tf_keras.models import Sequential
from tf_keras.layers import Dense
from sklearn.preprocessing import StandardScaler

def ffnn_classifier(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["target"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["target"]

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = Sequential([
    Dense(64, activation="relu"),
    Dense(32, activation="relu"),
    Dense(1, activation="sigmoid")
    ])

    model.compile(optimizer="adam",
                  loss="binary_crossentropy",
                  metrics=["accuracy"])

    model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

    y_prob = model.predict(X_test).flatten()
    y_pred = (y_prob >= 0.5).astype(int)

    return model, scaler, X_test, y_test, y_pred, y_prob

def ffnn_regressor(training_data, test_data):
    X_train = training_data.drop(["target", "future_return"], axis=1)
    y_train = training_data["future_return"]

    X_test = test_data.drop(["target", "future_return"], axis=1)
    y_test = test_data["future_return"]

    scaler = StandardScaler()
    
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = Sequential([
    Dense(64, activation="relu"),
    Dense(32, activation="relu"),
    Dense(1)
    ])

    model.compile(optimizer="adam",
                  loss="mse")

    model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

    y_pred = model.predict(X_test).flatten()

    return model, scaler, X_test, y_test, y_pred