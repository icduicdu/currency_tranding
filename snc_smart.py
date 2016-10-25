from exchange_sequence import ExchangeSequence
from snc_data import get_rate, separator

currencies = ['EURO', 'USD', 'CNY', 'RUB']

# all risk free exchange sequences
sequences = set()
shortest_seq = None
max_profit_seq = None


# exchange rate for convert i-currency-item to j-currency-item
def rate(c_from, c_to):
    return get_rate(currencies[c_from], currencies[c_to])


def add_conversion_step(currency_from, currency_to, exchange_seq_object):
    new_amount = exchange_seq_object.amount * rate(currency_from, currency_to)
    new_sequence = exchange_seq_object.sequence + separator + currencies[currency_to]
    new_op_amount = exchange_seq_object.operations_amount + 1
    exc_seq = ExchangeSequence(new_amount, new_sequence, new_op_amount)
    return exc_seq


def append_exchange_seq_if_no_risk(exchange_seq_object, currency_index):
    if (exchange_seq_object.amount * rate(currency_index, 0)) > 1.00:
        global shortest_seq
        global max_profit_seq
        new_amount = exchange_seq_object.amount * rate(currency_index, 0)
        new_seq = exchange_seq_object.sequence + separator + currencies[0]
        op_amount = exchange_seq_object.operations_amount + 1
        new_seq = ExchangeSequence(new_amount, new_seq, op_amount)
        # sequences.add(ExchangeSequence(new_amount, new_seq, op_amount))

        if shortest_seq is None:
            shortest_seq = new_seq

        if new_seq.operations_amount < shortest_seq.operations_amount:
            shortest_seq = new_seq

        if max_profit_seq is None:
            max_profit_seq = new_seq

        if new_seq.amount > max_profit_seq.amount:
            max_profit_seq = new_seq


# best[1][i]-maximum counts of currency i on step 1
best = []
for i in range(len(currencies)):
    best.append([])
    for j in range(len(currencies)):
        best[i].append(ExchangeSequence(0, currencies[0], 1))


# first step: convert one euro to all currencies
for i in range(len(currencies)):
    if i == 0:
        best[0][i] = ExchangeSequence(rate(0, i), currencies[0], 1)
    else:
        best[0][i] = ExchangeSequence(rate(0, i), currencies[0] + separator + currencies[i], 2)


for k in range(1, len(currencies)):
    for i in range(len(currencies)):
        for j in range(len(currencies)):
            previous_best = best[k-1][j]
            current_best = best[k][i]
            if currencies[i] not in str(previous_best.sequence):
                if previous_best.amount * rate(j, i) > current_best.amount:
                    best[k][i] = add_conversion_step(j, i, previous_best)
                    append_exchange_seq_if_no_risk(best[k][i], i)


seq_list = list(sequences)
if shortest_seq is not None:
    # shortest = seq_list[0]
    # with_more_money = seq_list[0]
    # for s in seq_list:
    #     if s.amount > with_more_money.amount:
    #         with_more_money = s
    #     if len(s.sequence.split(separator)) < len(shortest.sequence.split(separator)):
    #         shortest = s
    print 'shortest:' + str(shortest_seq)
    print 'max profit:' + str(max_profit_seq)
else:
    print 'no risk-free opportunities exist yielding over 1.00% profit exist'
