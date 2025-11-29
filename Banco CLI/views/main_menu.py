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

        print(
            "\nDepósito realizado com sucesso!"
            f"\nNovo saldo da conta: {fmt.money_format(user_account.balance)}"
        )

        Utils.pause()

    @staticmethod
    def withdrawal(user_account):
        Utils.print_header("Saque")
        print(user_account)

        money = si.money_input(" - Insira o valor do saque: ")
        if money is None:
            return
        if money > user_account.balance:
            print(
                "\nSaldo insuficiente para completar a transação\nOperação cancelada!"
            )
            Utils.pause()
            return
        elif money > user_account.limit:
            print(
                "\nValor muito alto para saque\nDirija-se à uma agência para sacar essa quantia"
            )
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

        print(
            "\nSaque realizado com sucesso!"
            f"\nNovo saldo da conta: {fmt.money_format(user_account.balance)}"
        )

        Utils.pause()

    @staticmethod
    def transference(account_repo, user_account):
        Utils.print_header("Transferência")
        print(user_account)

        destiny_account_number = si.text_input(" - Número da conta: ")
        if destiny_account_number is None:
            return

        destiny_account = account_repo.search_account_by_number(destiny_account_number)
        if not destiny_account:
            print("\nConta não encontrada no sistema!\nOperação cancelada!")
            Utils.pause()
            return
        elif destiny_account == user_account:
            print(
                "\nImpossível transferir dinheiro para sua própria conta!\nOperação cancelada!"
            )
            Utils.pause()
            return

        print(f"\n{destiny_account}")

        confirm = input(
            "\nDigite '0' para cancelar ou qualquer outra tecla para confirmar a conta destino: "
        )

        if confirm == "0":
            print("\nOperação cancelada!")
            Utils.pause()
            return

        money = si.money_input(" - Insira o valor da transferência: ")
        if money is None:
            return
        if money > user_account.balance:
            print(
                "\nSaldo insuficiente para completar a transação\nOperação cancelada!"
            )
            Utils.pause()
            return
        elif money > user_account.limit:
            print(
                "\nValor muito alto para transferência\nDirija-se à uma agência para transferir essa quantia"
            )
            Utils.pause()
            return

        print(f"\nConfira o valor da transferência: {fmt.money_format(money)}")

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

        transference = Transference(user_account, destiny_account, money)
        transference.execute()

        print(
            "\nTransferência realizada com sucesso!"
            f"\nNovo saldo da conta: {fmt.money_format(user_account.balance)}"
        )

        Utils.pause()

    @staticmethod
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

        print(
            "\nPagamento realizado com sucesso!"
            f"\nNovo saldo da conta: {fmt.money_format(user_account.balance)}"
        )

        Utils.pause()

    @staticmethod
    def see_balance(user_account):
        Utils.print_header("Consultar Saldo")

        print(user_account)
        print(f"Saldo atual: {fmt.money_format(user_account.balance)}")

        Utils.pause()

    @staticmethod
    def see_statement(account_repo, user_account):
        Utils.print_header("Verificar Extrato")

        print(user_account)
        print(user_account.history)
        print(f"Saldo atual: {fmt.money_format(user_account.balance)}")

        Utils.pause()
