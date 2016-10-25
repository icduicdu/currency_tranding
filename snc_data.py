import csv
from random import randint, random

currency_codes = ['USD', 'CNY', 'RUB']
currencies = ['EURO', 'USD', 'CNY', 'RUB']
our_money_amount = 1.0

separator = ' -> '
currency_rate = None


def read_rates():
    global currency_rate
    currency_rate = {}
    f = open('data.csv', 'rb')
    reader = csv.reader(f)
    idx = 0
    for row in reader:
        row_list = row[0].split()
        for i in range(len(currencies)):
            currency_rate[currencies[idx] + '/' + currencies[i]] = float(row_list[i])
        idx += 1
    f.close()


def get_rate(c_from, c_to):
    global currency_rate
    if currency_rate is None:
        read_rates()
    return currency_rate[c_from + '/' + c_to]
