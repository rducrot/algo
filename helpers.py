from constants import *
import csv
import pandas


def format_data(data: pandas.DataFrame, sort_data=False):
    """
    Remove errors from the dataset.
    :param data: DataFrame
    :param sort_data: bool
    Sort data by best profit.
    :return: data: DataFrame
    """
    data = data[data[COLUMN_NAMES[PRICE]] > 0.1]
    data = data[data[COLUMN_NAMES[PROFIT_PERCENT]] > 0]
    data[COLUMN_NAMES[NET_PROFIT]] = round(data[COLUMN_NAMES[PRICE]] * data[COLUMN_NAMES[PROFIT_PERCENT]] / 100, 2)

    if sort_data:
        data = data.sort_values(COLUMN_NAMES[PROFIT_PERCENT], ascending=False)

    return data


def write_results_to_csv(file: str, prefix: str, dataset_results: list):
    """
    Write results to a CSV file.
    :param file: str
    :param prefix: str
    :param dataset_results: list
    """
    with open(RESULTS_DIR + prefix + file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(COLUMN_NAMES)
        writer.writerows(dataset_results)


def show_results(file: str, results: list):
    """
    Print results in the terminal.
    :param file: str
    :param results: list
    """
    actions = 0
    total_sum = 0
    profit = 0

    for result in results:
        actions += 1
        total_sum += result[PRICE]
        profit += result[NET_PROFIT]

    print(file)
    print(f'Actions achetées : {actions}')
    print(f'Somme dépensée : {round(total_sum, 2)}')
    print(f'Profit réalisé : {round(profit, 2)}')
