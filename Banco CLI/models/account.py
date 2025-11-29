from datetime import datetime

from utils import Formatters as fmt

from .history import History


class Account:
    _total_accounts = 0

    def __init__(self, customer, account_password, app_password):
        self.agency = "0001"
        self._balance = 0

        self.number = Account.generate_account_number()
        self.opening_date = datetime.now()

        self.owner = customer
        self.account_password = account_password
        self.app_password = app_password

        self.history = History()

    @classmethod
    def generate_account_number(cls):
        cls._total_accounts += 1
        return str(cls._total_accounts + 1000)

    def get_account_number(self):
        return self.number

    def get_age(self):
        today_date = datetime.today().date()
        return (today_date - self.opening_date.date()).days // 365

    @property
    def balance(self):
        return self._balance

    def increase_balance(self, amount):
        self._balance += amount

    def decrease_balance(self, amount):
        self._balance -= amount

    def passwords_match(self, password):
        return self.account_password == password


class CheckingAccount(Account):

    def __init__(self, customer, account_password, app_password, limit=6000):
        super().__init__(customer, account_password, app_password)
        self.limit = limit

    def __str__(self):
        return (
            f" == {f' Conta Corrente '.center(22, '-')} == \n"
            f"Ag.: {self.agency} - Conta: {self.number}\n"
            f"{fmt.date_format(self.opening_date.date())} : {self.get_age()} anos\n"
            f"{self.owner.get_id()} - {self.owner.get_name()}\n"
        )


class SavingsAccount(Account):

    def __init__(self, customer, account_password, app_password, limit=4000):
        super().__init__(customer, account_password, app_password)
        self.limit = limit

    def __str__(self):
        return (
            f" == {f' Conta Poupança '.center(22, '-')} == \n"
            f"Ag.: {self.agency} - Conta: {self.number}\n"
            f"{fmt.date_format(self.opening_date.date())} : {self.get_age()} anos\n"
            f"{self.owner.get_id()} - {self.owner.get_name()}\n"
        )
