from itertools import permutations
from snc_data import our_money_amount, currencies, separator, currency_codes, get_rate


def print_non_risk_seq(li, k):
    res = str(k) + ' ' + currencies[0] + separator
    for s in li:
        res += s + ' -> '
    res += currencies[0]
    print res


def run_dumb():
    sequences = []
    i = len(currency_codes) + 1
    while i > 1:
        i -= 1
        res = list(permutations(currency_codes, i))
        sequences += res

    for seq in sequences:
        current_money_amount = our_money_amount
        current_currency = currencies[0]
        current_list = list(seq)
        for i in current_list:
            current_money_amount = get_rate(current_currency, i) * current_money_amount
            current_currency = i
        amount_in_our_currency = get_rate(current_currency, currencies[0]) * current_money_amount
        if amount_in_our_currency > 1.0:
            print_non_risk_seq(current_list, amount_in_our_currency)

run_dumb()
