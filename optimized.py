from constants import *
import helpers
import pandas


def format_and_sort_data(data: pandas.DataFrame):
    data = data[data[COLUMN_NAMES[PRICE]] > 0.1]
    data = data[data[COLUMN_NAMES[PROFIT_PERCENT]] > 0]
    data[COLUMN_NAMES[NET_PROFIT]] = round(data[COLUMN_NAMES[PRICE]] * data[COLUMN_NAMES[PROFIT_PERCENT]] / 100, 2)
    data = data.sort_values(COLUMN_NAMES[PROFIT_PERCENT], ascending=False)
    return data


def select_actions_optimized(data: pandas.DataFrame):
    money_spent = 0
    results = []
    for _, action in data.iterrows():
        if money_spent + action[COLUMN_NAMES[PRICE]] <= BUDGET:
            results.append(action)
            money_spent += action[COLUMN_NAMES[PRICE]]
    return results


for file in DATASETS:
    dataset_base = pandas.read_csv(DATASETS_DIR + file)
    dataset = format_and_sort_data(dataset_base)
    dataset_results = select_actions_optimized(dataset)
    helpers.write_results_to_csv(file, OPTIMIZED_PREFIX, dataset_results)
    helpers.show_results(file, dataset_results)
