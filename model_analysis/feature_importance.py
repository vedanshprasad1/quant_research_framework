import pandas as pd

def get_feature_contributions(model, feature_names):
    if hasattr(model, "coef_"):
        if type(model).__name__ == "LogisticRegression":
            values = [round(value, 3) for value in model.coef_[0]]
            column = "Logistic Coefficients"

        else:
            values = [round(value, 3) for value in model.coef_]
            column = "Linear Regression Coefficients"

    elif hasattr(model, "feature_importances_"):
        values = [round(value, 3) for value in model.feature_importances_]
        column = "Feature Importances"

    else:
        return None
    
    features_names_list = list(feature_names)

    feature_importances = pd.DataFrame({
        "Features": features_names_list,
        column: values
    })

    return feature_importances