import json
import os

def load_experiments():
    filename = "experiments/experiment_configs.json"

    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_experiment(experiment):
    filename = "experiments/experiment_configs.json"

    if not os.path.exists(filename):
        return

    experiments = load_experiments()

    experiments.append(experiment)

    with open(filename, "w") as file:
        json.dump(experiments, file, indent=4)

def delete_experiment(experiment_name):
    filename = "experiments/experiment_configs.json"

    if not os.path.exists(filename):
        return

    experiments = load_experiments()

    remaining_experiments = [
        experiment
        for experiment in experiments
        if experiment["name"] != experiment_name
    ]

    with open(filename, "w") as file:
        json.dump(remaining_experiments, file, indent=4)

def delete_experiment_results(experiment_name):
    filename = "results/results.json"

    if not os.path.exists(filename):
        return

    with open(filename, "r") as file:
        try:
            results = json.load(file)
        except json.JSONDecodeError:
            results = []

    remaining_results = [
        result
        for result in results
        if result["experiment"] != experiment_name
    ]

    with open(filename, "w") as file:
        json.dump(remaining_results, file, indent=4)

def choose_experiment():
    experiments = load_experiments()

    if not experiments:
        print()
        print("No saved experiments")
        return None

    print()
    print("SAVED EXPERIMENTS")
    print("-----------------")

    for i, experiment in enumerate(experiments, start=1):
        print(
            f"{i}. {experiment["name"]} "
            f"({experiment["stock"]})"
        )

    print()

    try:
        choice = int(input("Enter experiment number: "))
    except ValueError:
        print("Invalid choice.")
        return None

    if choice < 1 or choice > len(experiments):
        print("Invalid experiment number.")
        return None

    return experiments[choice - 1]

def remove_experiment():
    choice = choose_experiment()

    if choice is None:
        return

    print()
    print(f"Experiment: {choice['name']}")

    confirmation = input(
        "Are you sure you want to delete this experiment? (Y/N) "
    ).upper()

    if confirmation == "Y":
        delete_experiment(choice["name"])
        delete_experiment_results(choice["name"])
        print("Experiment deleted.")
    else:
        print("Experiment was not deleted.")