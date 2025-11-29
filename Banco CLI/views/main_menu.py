from models import Deposit, Payment, Transference, Withdrawal
from utils import Formatters as fmt
from utils import StandardInputs as si
from utils import Utils


class MainMenu:

    @staticmethod
    def deposit(user_account):
        Utils.print_header("Depósito")
        print(user_account)

        money = si.money_input(" - Insira o valor do depósito: ")
        if money is None:
            return
        print(f"\nConfira o valor do depósito: {fmt.money_format(money)}")

        attempts = 0
        while attempts < 3:
            account_password = si.text_input(
                "\n - Digite sua senha para confirmar a transação ou '0' para cancelar: "
            )
            if account_password is None:
                return

            if user_account.passwords_match(account_password):
                break
            else:
                print("Senhas não conferem!")
                attempts += 1
        else:
            print("\nMuitas tentativas erradas!\nOperação cancelada!")
            Utils.pause()
            return None

        deposit = Deposit(user_account, money)
        deposit.execute()

        print(f"\nNovo saldo da conta: {fmt.money_format(user_account.balance)}")

        Utils.pause()

    @staticmethod
    def withdrawal(user_account):
        Utils.print_header("Saque")
        print(user_account)

        money = si.money_input(" - Insira o valor do saque: ")
        if money is None:
            return
        if money > user_account.balance:
            print("\nSaldo insuficiente para completar a transação\nOperação cancelada")
            Utils.pause()
            return

        print(f"\nConfira o valor do saque: {fmt.money_format(money)}")

        attempts = 0
        while attempts < 3:
            account_password = si.text_input(
                "\n - Digite sua senha para confirmar a transação ou '0' para cancelar: "
            )
            if account_password is None:
                return

            if user_account.passwords_match(account_password):
                break
            else:
                print("Senhas não conferem!")
                attempts += 1
        else:
            print("\nMuitas tentativas erradas!\nOperação cancelada!")
            Utils.pause()
            return None

        withdrawal = Withdrawal(user_account, money)
        withdrawal.execute()

        print(f"\nNovo saldo da conta: {fmt.money_format(user_account.balance)}")

        Utils.pause()

    def transference(account_repo, user_account):
        Utils.print_header("Transferência")
        print(user_account)

        money = si.money_input(" - Insira o valor da transferência: ")
        if money is None:
            return
        if money < user_account.balance:
            print("Saldo insuficiente para completar a transação\nOperação cancelada")
            Utils.pause()
            return

        Utils.pause()

    def payment(user_account):
        Utils.print_header("Pagamento")
        print(user_account)

        bill_code = si.bill_code_input()
        if bill_code is None:
            return

        bill_amount = Utils.calculate_bill(bill_code)
        print(f"\nValor do boleto: {fmt.money_format(bill_amount)}")
        if bill_amount > user_account.balance:
            print("\nSaldo insuficiente para completar a transação\nOperação cancelada")
            Utils.pause()
            return

        attempts = 0
        while attempts < 3:
            account_password = si.text_input(
                "\n - Digite sua senha para confirmar a transação ou '0' para cancelar: "
            )
            if account_password is None:
                return

            if user_account.passwords_match(account_password):
                break
            else:
                print("Senhas não conferem!")
                attempts += 1
        else:
            print("\nMuitas tentativas erradas!\nOperação cancelada!")
            Utils.pause()
            return None

        payment = Payment(user_account, bill_amount)
        payment.execute()

        print(f"\nNovo saldo da conta: {fmt.money_format(user_account.balance)}")

        Utils.pause()

    @staticmethod
    def see_balance(user_account):
        Utils.print_header("Consultar Saldo")
        print(user_account)
        print(f"Saldo atual: {fmt.money_format(user_account.balance)}")
        Utils.pause()

    def see_statement(account_repo, user_account):
        Utils.print_header("Verificar Extrato")
        print(user_account)
        Utils.pause()
