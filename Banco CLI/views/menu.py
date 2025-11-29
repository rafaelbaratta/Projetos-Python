from utils import Utils

from .login_menu import LoginMenu
from .main_menu import MainMenu


class Menu:

    LOGIN_MENU = (
        "            [1] Registrar Usuário\n"
        "            [2] Abrir Conta\n"
        "            [3] Listar Usuários\n"
        "            [4] Listar Contas\n"
        "            [5] Entrar no Sistema\n"
        "            [0] Sair do Sistema\n\n"
        "== --> "
    )
    MAIN_MENU = (
        "            [1] Depósito\n"
        "            [2] Saque\n"
        "            [3] Transferência\n"
        "            [4] Pagamento\n"
        "            [5] Consultar Saldo\n"
        "            [6] Verificar Extrato\n"
        "            [0] Desconectar\n\n"
        "== --> "
    )

    @staticmethod
    def login_menu(customer_repo, account_repo):
        while True:
            Utils.print_header("Menu Inicial")
            opcao = input(Menu.LOGIN_MENU).strip()

            match opcao:
                case "1":
                    LoginMenu.register_user(customer_repo)
                case "2":
                    LoginMenu.create_account(customer_repo, account_repo)
                case "3":
                    LoginMenu.list_users(customer_repo)
                case "4":
                    LoginMenu.list_accounts(account_repo)
                case "5":
                    user_account = LoginMenu.login(account_repo)
                    if user_account:
                        Menu.main_menu(account_repo, user_account)
                case "0":
                    print("Sistema encerrado!")
                    return
                case _:
                    print("Opção inválida inserida!")
                    Utils.pause()

    @staticmethod
    def main_menu(account_repo, user_account):
        while True:
            Utils.clean_screen()
            print(user_account.owner)
            Utils.print_header("Menu Principal")
            opcao = input(Menu.MAIN_MENU).strip()

            match opcao:
                case "1":
                    MainMenu.deposit(user_account)
                case "2":
                    MainMenu.withdrawal(user_account)
                case "3":
                    MainMenu.transference(account_repo, user_account)
                case "4":
                    MainMenu.payment(user_account)
                case "5":
                    MainMenu.see_balance(user_account)
                case "6":
                    MainMenu.see_statement(account_repo, user_account)
                case "0":
                    print("Sistema encerrado!")
                    return
                case _:
                    print("Opção inválida inserida!")
                    Utils.pause()
