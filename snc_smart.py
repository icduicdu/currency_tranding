from exchange_sequence import ExchangeSequence
from snc_data import get_rate, separator, currencies

shortest_seq = None    # shortest risk free exchange sequence
max_profit_seq = None  # risk free exchange sequence with max profit
best = []              # best[j][i]-maximum counts of currency i on step j


def rate(c_from, c_to):
    """exchange rate for convert i-currency-item to j-currency-item"""
    return get_rate(currencies[c_from], currencies[c_to])


def add_conversion_step(currency_from, currency_to, exchange_seq_object):
    """ Convert ExchangeSequence from currency with index "currency_from" to currency with index "currency_to"
    and saves change history """
    new_amount = exchange_seq_object.amount * rate(currency_from, currency_to)
    new_sequence = exchange_seq_object.sequence + separator + currencies[currency_to]
    new_op_amount = exchange_seq_object.operations_amount + 1
    exc_seq = ExchangeSequence(new_amount, new_sequence, new_op_amount)
    return exc_seq


def save_exchange_seq_if_no_risk(exchange_seq_object, currency_index):
    """ Check object of class ExchangeSequence. If exchange_seq_object better than object we have at current step
    then saves it """
    if (exchange_seq_object.amount * rate(currency_index, 0)) > 1.00:
        global shortest_seq
        global max_profit_seq
        new_amount = exchange_seq_object.amount * rate(currency_index, 0)
        new_seq = exchange_seq_object.sequence + separator + currencies[0]
        op_amount = exchange_seq_object.operations_amount + 1
        new_seq = ExchangeSequence(new_amount, new_seq, op_amount)

        if shortest_seq is None:
            shortest_seq = new_seq

        if new_seq.operations_amount < shortest_seq.operations_amount:
            shortest_seq = new_seq

        if max_profit_seq is None:
            max_profit_seq = new_seq

        if new_seq.amount > max_profit_seq.amount:
            max_profit_seq = new_seq


def init_matrix():
    """ best[1][i]-maximum counts of currency i on step 1 """
    global best
    for i in range(len(currencies)):
        best.append([])
        for j in range(len(currencies)):
            best[i].append(ExchangeSequence(0, currencies[0], 1))


def first_step():
    """ first step: convert one euro to all currencies"""
    global best
    for i in range(len(currencies)):
        if i == 0:
            best[0][i] = ExchangeSequence(rate(0, i), currencies[0], 1)
        else:
            best[0][i] = ExchangeSequence(rate(0, i), currencies[0] + separator + currencies[i], 2)


def run_next_steps():
    for k in range(1, len(currencies)):
        for i in range(len(currencies)):
            for j in range(len(currencies)):
                previous_best = best[k - 1][j]
                current_best = best[k][i]
                if currencies[i] not in str(previous_best.sequence):
                    if previous_best.amount * rate(j, i) > current_best.amount:
                        best[k][i] = add_conversion_step(j, i, previous_best)
                        save_exchange_seq_if_no_risk(best[k][i], i)


def print_result():
    global shortest_seq
    global max_profit_seq
    if shortest_seq is not None:
        print 'shortest:' + str(shortest_seq)
        print 'max profit:' + str(max_profit_seq)
    else:
        print 'no risk-free opportunities exist yielding over 1.00% profit exist'

init_matrix()
first_step()
run_next_steps()
print_result()
