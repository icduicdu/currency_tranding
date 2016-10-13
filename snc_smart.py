from snc_data import get_rate, separator, convert_seq

currencies = ['EURO', 'USD', 'CNY', 'RUB']
n = len(currencies)
sequences = set()


def rate(i, j):
    return get_rate(currencies[i], currencies[j])


# best[1][i]-maximum counts of currency i on step 1
best = []
for i in range(len(currencies)):
    best.append([])
    for j in range(len(currencies)):
        best[i].append((0, currencies[0]))


# first step: convert one euro to all currencies
for i in range(n):
    if i == 0:
        best[0][i] = (rate(0, i), currencies[0])
    else:
        best[0][i] = (rate(0, i), currencies[0] + separator + currencies[i])


for k in range(1, n):
    for i in range(n):
        for j in range(n):
            if currencies[i] not in best[k - 1][j][1]:
                if best[k-1][j][0] * rate(j, i) > best[k][i][0]:
                    best[k][i] = (best[k-1][j][0] * rate(j, i), best[k-1][j][1] + separator + currencies[i])
                    if (best[k][i][0] * rate(i, 0)) > 1.00:
                        sequences.add((best[k][i][0] * rate(i, 0), best[k][i][1] + separator + currencies[0]))


seq_list = list(sequences)
if len(sequences) > 0:
    shortest = seq_list[0]
    with_more_money = seq_list[0]
    for s in seq_list:
        if s[0] > with_more_money:
            with_more_money = s
        if len(s[1].split(separator)) < len(shortest[1].split(separator)):
            shortest = s
    print 'shortest:' + str(shortest)
    print 'with more %:' + str(with_more_money)
else:
    print 'no risk-free opportunities exist yielding over 1.00% profit exist'