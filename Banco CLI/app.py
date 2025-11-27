from repositories import AccountRepository, CustomerRepository
from views import Menu


def main():
    account_repo = AccountRepository()
    customer_repo = CustomerRepository()

    Menu.login_menu(customer_repo, account_repo)


if __name__ == "__main__":
    main()
