class Account:

    def __init__(self, account_number, creation_date, agency="0001", balance=0):
        self.number = account_number
        self.agency = agency
        self.balance = balance
        self.creation_date = creation_date


class CheckingAccount(Account):

    def __init__(self, account_number, limit, withdrawal_limit):
        super().__init__(account_number)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit


class SavingsAccount(Account):
    pass
