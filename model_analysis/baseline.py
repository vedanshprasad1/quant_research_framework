def random_guessing(accuracy):
    if accuracy >= 0.5:
        # Better than random guessing
        return True
    else:
        # Worst than random guessing
        return False

def majority_voting(accuracy, value_counts):
    false_count = value_counts.iloc[0]
    true_count = value_counts.iloc[1]

    baseline_value = max(false_count, true_count) / (false_count + true_count)

    if accuracy >= baseline_value:
        # Better than majority guessing
        return True
    else:
        # Worse than majority guessing
        return False