from constants import *
import helpers
import pandas


def select_actions_optimized(data: pandas.DataFrame):
    """
    Return a list of actions with the best profit regarding a budget.
    :param data: DataFrame
    :return: results
    """
    money_spent = 0
    results = []
    for _, action in data.iterrows():
        if money_spent + action[COLUMN_NAMES[PRICE]] <= BUDGET:
            results.append(action)
            money_spent += action[COLUMN_NAMES[PRICE]]
    return results


for file in DATASETS:
    dataset_base = pandas.read_csv(DATASETS_DIR + file)
    dataset = helpers.format_data(dataset_base, sort_data=True)
    dataset_results = select_actions_optimized(dataset)
    helpers.write_results_to_csv(file, OPTIMIZED_PREFIX, dataset_results)
    helpers.show_results(file, dataset_results)
