from itertools import permutations

currency_codes = ['USD', 'CNY', 'RUB']

our_currency = 'EURO'
our_money_amount = 1.0

separator = ' -> '


def get_rates():
    currency_rate = {}
    currency_rate['USD/USD'] = 1.0
    currency_rate['USD/EURO'] = 0.9
    currency_rate['USD/CNY'] = 6.0
    currency_rate['USD/RUB'] = 65.0
    currency_rate['EURO/USD'] = 1.1
    currency_rate['EURO/EURO'] = 1.0
    currency_rate['EURO/CNY'] = 6.5
    currency_rate['EURO/RUB'] = 70.0
    currency_rate['CNY/USD'] = 0.17
    currency_rate['CNY/EURO'] = 0.16
    currency_rate['CNY/CNY'] = 1.0
    currency_rate['CNY/RUB'] = 10.75
    currency_rate['RUB/USD'] = 0.02
    currency_rate['RUB/EURO'] = 0.01
    currency_rate['RUB/CNY'] = 0.08
    currency_rate['RUB/RUB'] = 1.0
    return currency_rate


def get_rate(c_from, c_to):
    rates = get_rates()
    return rates[c_from + '/' + c_to]


def get_sequences():
    _list = []
    i = len(currency_codes) + 1
    while i > 1:
        i -= 1
        res = list(permutations(currency_codes, i))
        _list += res
    return _list


def print_non_risk_seq(li, k):
    res = str(k) + ' ' + our_currency + separator
    for s in li:
        res += s + ' -> '
    res += our_currency
    print res


def convert_seq(_list):
    res = 1
    for i in range(1, len(_list)):
        res *= get_rate(_list[i-1], _list[i])
    print res
