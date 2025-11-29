from models import Account


class AccountRepository:

    def __init__(self):
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def list_all_accounts(self):
        return self._accounts.copy()

    def count_accounts(self):
        return len(self._accounts)

    def search_account_by_number(self, account_number):
        for account in self._accounts:
            if account.get_account_number() == account_number:
                return account

        return None
