import pandas as pd
from statistical_tests.hypothesis_testing import feature_t_test

def ttest_all_features(features):
    results = []

    for feature in features.drop(["future_return", "target"], axis=1):
        test_statistic, p_value, low_mean, high_mean = feature_t_test(features, feature)

        results.append({
            "Features": feature,
            "Low mean returns": low_mean,
            "High mean returns": high_mean,
            "Test statistics": test_statistic,
            "p_values": p_value,
            "Significant": p_value < 0.05
        })
    
    return pd.DataFrame(results)