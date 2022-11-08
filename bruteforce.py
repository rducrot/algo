from constants import *
import helpers
import itertools
import pandas


def select_actions(data: pandas.DataFrame):
    """
    Return a list of actions with the best profit regarding a budget.
    :param data: DataFrame
    :return: best_results: list
    """
    best_results = []
    best_profit = 0
    for i in range(data.size):
        for prices_list in itertools.combinations(data[COLUMN_NAMES[PRICE]], i + 1):
            total_price = sum(prices_list)
            if total_price <= BUDGET:
                results = data.loc[data[COLUMN_NAMES[PRICE]].isin(prices_list)]
                profit = sum(results[COLUMN_NAMES[NET_PROFIT]])
                if profit > best_profit:
                    best_profit = profit
                    print(best_profit)
                    best_results.clear()
                    for _, action in results.iterrows():
                        best_results.append(action)
    return best_results


dataset_base = pandas.read_csv(DATASETS_DIR + DATASETS[BRUTEFORCE_INDEX])
dataset = helpers.format_data(dataset_base)
dataset_results = select_actions(dataset)
helpers.write_results_to_csv(DATASETS[BRUTEFORCE_INDEX], BRUTEFORCE_PREFIX, dataset_results)
helpers.show_results(DATASETS[BRUTEFORCE_INDEX], dataset_results)
