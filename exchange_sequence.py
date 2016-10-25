class ExchangeSequence:
    """
        Class for describe convert sequence, amount is amount of money, sequence is a string like "curr1-curr2-curr3".
        The last "curr" is a currency which amount we have in amount attr
    """
    amount = 0
    sequence = ''
    operations_amount = 0

    def __init__(self, amount, sequence, operations_amount):
        self.amount = amount
        self.sequence = sequence
        self.operations_amount = operations_amount

    def __str__(self):
        return str(self.amount) + ' | ' + self.sequence
