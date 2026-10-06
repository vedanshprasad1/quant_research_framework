def ttest_report(feature_name, test_statistic, p_value, low_mean, high_mean):
    significance = p_value < 0.05

    print("--------------------")
    print("T TEST RESULT")
    print("--------------------\n")

    print(f"Feature: {feature_name}\n")

    print(f"Low mean return: {low_mean}\n")

    print(f"High mean return: {high_mean}\n")

    print(f"Test statistic: {test_statistic}\n")

    print(f"p-value: {p_value}\n")

    print(f"Significant: {significance}")

    return significance

