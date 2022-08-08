from constants import *
import csv


def write_results_to_csv(file, dataset_results):
    with open(RESULTS_DIR + RESULT_PREFIX + file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(COLUMN_NAMES)
        writer.writerows(dataset_results)


def show_results(file, results):
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
