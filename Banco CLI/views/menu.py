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
        "            [4] Consultar Saldo\n"
        "            [5] Verificar Extrato\n"
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
                    LoginMenu.login()
                case "0":
                    print("Sistema encerrado!")
                    return
                case _:
                    print("Opção inválida inserida!")
                    Utils.pause()

    @staticmethod
    def main_menu():
        while True:
            Utils.clean_screen()
            Utils.print_header("Menu Principal")
            opcao = input(Menu.MAIN_MENU).strip()

            match opcao:
                case "1":
                    MainMenu.deposit()
                case "2":
                    MainMenu.withdrawal()
                case "3":
                    MainMenu.transference()
                case "4":
                    MainMenu.see_balance()
                case "5":
                    MainMenu.see_statement()
                case "0":
                    print("Sistema encerrado!")
                    return
                case _:
                    print("Opção inválida inserida!")
                    Utils.pause()
