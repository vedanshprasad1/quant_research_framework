from scipy.stats import ttest_ind

def feature_t_test(features, feature_name):
    median = features[feature_name].median()

    low_values = features[features[feature_name] < median]
    low_mean = low_values["future_return"].mean()
    high_values = features[features[feature_name] >= median]
    high_mean = high_values["future_return"].mean()

    ttest_result = ttest_ind(low_values["future_return"], high_values["future_return"], equal_var=False)

    return ttest_result.statistic, ttest_result.pvalue, low_mean, high_mean