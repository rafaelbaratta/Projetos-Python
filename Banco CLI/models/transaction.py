from abc import ABC, abstractmethod


class Transaction(ABC):

    @abstractmethod
    def register(account):
        pass


class Deposit(Transaction):
    pass


class Withdrawal(Transaction):
    pass
