from utils import Formatters as fmt


class History:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __str__(self):
        history = ""
        for transaction in self.transactions:
            history += (
                f"{transaction[0].strftime('%d/%m/%Y - %H:%M:%S')} "
                + f"{transaction[1]}:".ljust(15, " ")
                + f"{fmt.money_format(transaction[2])} {transaction[3]}".rjust(15, " ")
                + "\n"
            )
        return history
