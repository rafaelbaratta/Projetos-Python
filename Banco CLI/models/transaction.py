from abc import ABC, abstractmethod
from datetime import datetime


class Transaction(ABC):

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.datetime = datetime.now()
        self.description = ""

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def register(self):
        pass


class Deposit(Transaction):

    def __init__(self, account, amount):
        super().__init__(account, amount)

    def execute(self):
        self.account.increase_balance(self.amount)
        self.register()

    def register(self):
        transaction = [datetime.now(), "Depósito", self.amount, "+"]
        self.account.history.add_transaction(transaction)


class Withdrawal(Transaction):

    def __init__(self, account, amount):
        super().__init__(account, amount)

    def execute(self):
        self.account.decrease_balance(self.amount)
        self.register()

    def register(self):
        transaction = [datetime.now(), "Saque", self.amount, "-"]
        self.account.history.add_transaction(transaction)


class Transference(Transaction):

    def __init__(self, origin_account, destiny_account, amount):
        super().__init__(origin_account, amount)
        self.origin_account = origin_account
        self.destiny_account = destiny_account

    def execute(self):
        self.origin_account.decrease_balance(self.amount)
        self.destiny_account.increase_balance(self.amount)
        self.register()

    def register(self):
        transaction = [datetime.now(), "Transferência", self.amount, "-"]
        self.origin_account.history.add_transaction(transaction)

        transaction = [datetime.now(), "Transferência", self.amount, "+"]
        self.destiny_account.history.add_transaction(transaction)


class Payment(Transaction):

    def __init__(self, account, amount):
        super().__init__(account, amount)

    def execute(self):
        self.account.decrease_balance(self.amount)
        self.register()

    def register(self):
        transaction = [datetime.now(), "Pagamento", self.amount, "-"]
        self.account.history.add_transaction(transaction)
