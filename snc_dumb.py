
from snc_data import get_rates, get_sequences, our_money_amount, our_currency, print_non_risk_seq

currency_rate = get_rates()
sequences = get_sequences()

for seq in sequences:
    current_money_amount = our_money_amount
    current_currency = our_currency
    current_list = list(seq)
    for i in current_list:
        current_money_amount = currency_rate[current_currency + '/' + i] * current_money_amount
        current_currency = i
    amount_in_our_currency = currency_rate[current_currency + '/' + our_currency] * current_money_amount
    if amount_in_our_currency > 1.0:
        print_non_risk_seq(current_list, amount_in_our_currency)
