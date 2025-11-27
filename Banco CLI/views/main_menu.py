from utils import Utils


class MainMenu:
    def deposit():
        Utils.print_header("Depósito")
        Utils.pause()

    def withdrawal():
        Utils.print_header("Saque")
        Utils.pause()

    def transference():
        Utils.print_header("Transferência")
        Utils.pause()

    def see_balance():
        Utils.print_header("Consultar Saldo")
        Utils.pause()

    def see_statement():
        Utils.print_header("Verificar Extrato")
        Utils.pause()
