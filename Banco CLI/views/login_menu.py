from models import CheckingAccount, LegalEntity, NaturalPerson, SavingsAccount
from utils import StandardInputs as si
from utils import Utils


class LoginMenu:

    @staticmethod
    def register_user(customer_repo):
        Utils.print_header("Registrar Usuário")
        print("Digite 0 a qualquer momento para cancelar a operação\n")
        opcao = input("Pessoa física ou jurídica [pf/pj]? ").lower().strip()

        while opcao != "pf" and opcao != "pj" and opcao != "0":
            opcao = input("Digite apenas 'pf', 'pj' ou '0' para cancelar: ")

        if opcao == "pf":
            LoginMenu.register_natural_person(customer_repo)
        elif opcao == "pj":
            LoginMenu.register_legal_entity(customer_repo)
        else:
            print("Operação cancelada!")
            Utils.pause()

    @staticmethod
    def register_natural_person(customer_repo):
        Utils.print_header("Registrar Pessoa Física")
        print("Digite 0 a qualquer momento para cancelar a operação\n")

        cpf = si.cpf_input()
        if customer_repo.id_already_exists(cpf):
            print("CPF inserido já está em uso!\nOperação cancelada!")
            Utils.pause()
            return

        if cpf is None:
            return

        name = si.text_input(" - Digite seu nome: ")
        if name is None:
            return

        phone = si.phone_input()
        if phone is None:
            return

        email = si.email_input()
        if email is None:
            return

        birth_date = si.date_input("nascimento")
        if birth_date is None:
            return

        adress = si.text_input(" - Insira seu endereço: ")
        if adress is None:
            return

        new_customer = NaturalPerson(cpf, name, birth_date, email, phone, adress)

        print(f"\nConfira os dados\n\n{new_customer}\n")

        confirm = input(
            "Digite '0' para cancelar a operação ou qualquer outra tecla para confirmar: "
        )

        if confirm == "0":
            del new_customer
            print("\nOperação cancelada!")
        else:
            customer_repo.add_customer(new_customer)
            print("\nUsuário cadastrado com sucesso!")

        Utils.pause()

    @staticmethod
    def register_legal_entity(customer_repo):
        Utils.print_header("Registrar Pessoa Jurídica")
        print("Digite 0 a qualquer momento para cancelar a operação\n")

        cnpj = si.cnpj_input()
        if customer_repo.id_already_exists(cnpj):
            print("CNPJ inserido já está em uso!\nOperação cancelada!")
            Utils.pause()
            return

        if cnpj is None:
            return

        company_name = si.text_input(" - Digite a razão social da empresa: ")
        if company_name is None:
            return

        trade_name = si.text_input(" - Digite o nome fantasia da empresa: ")
        if trade_name is None:
            return

        phone = si.phone_input()
        if phone is None:
            return

        email = si.email_input()
        if email is None:
            return

        foundation_date = si.date_input("fundação")
        if foundation_date is None:
            return

        adress = si.text_input(" - Insira o endereço da empresa: ")
        if adress is None:
            return

        new_customer = LegalEntity(
            cnpj, company_name, trade_name, foundation_date, email, phone, adress
        )

        print(f"\nConfira os dados\n\n{new_customer}\n")

        confirm = input(
            "Digite '0' para cancelar a operação ou qualquer outra tecla para confirmar: "
        )

        if confirm == "0":
            del new_customer
            print("\nOperação cancelada!")
        else:
            customer_repo.add_customer(new_customer)
            print("\nUsuário cadastrado com sucesso!")

        Utils.pause()

    @staticmethod
    def create_account(customer_repo, account_repo):
        Utils.print_header("Abrir Conta")
        print("Digite 0 a qualquer momento para cancelar a operação\n")
        opcao = input("Conta corrente ou poupança [cc/cp]? ").lower().strip()

        while opcao != "cc" and opcao != "cp" and opcao != "0":
            opcao = input("Digite apenas 'cc', 'cp' ou '0' para cancelar: ")

        if opcao == "cc":
            LoginMenu.create_checking_account(customer_repo, account_repo)
        elif opcao == "cp":
            LoginMenu.create_savings_account(customer_repo, account_repo)
        else:
            print("Operação cancelada!")
            Utils.pause()

    @staticmethod
    def ask_natural_person_or_legal_entity():
        opcao = (
            input("Abrir a partir de pessoa física ou jurídica [pf/pj]? ")
            .lower()
            .strip()
        )

        while opcao != "pf" and opcao != "pj" and opcao != "0":
            opcao = input("Digite apenas 'pf', 'pj' ou '0' para cancelar: ")

        return opcao

    @staticmethod
    def create_checking_account(customer_repo, account_repo):
        Utils.print_header("Abrir Conta Corrente")
        print("Digite 0 a qualquer momento para cancelar a operação\n")

        opcao = LoginMenu.ask_natural_person_or_legal_entity()

        if opcao == "pf":
            id = si.cpf_input()
        elif opcao == "pj":
            id = si.cnpj_input()
        else:
            print("Operação cancelada!")
            Utils.pause()
            return

        if id is None:
            return

        customer = customer_repo.search_customer_by_id(id)
        if not customer:
            print("\nDado inserido não existe no sistema!")
            Utils.pause()
            return

        print(f"\n{customer}")

        confirm = input(
            "\nDigite '0' para cancelar ou qualquer outra tecla para confirmar o usuário: "
        )

        if confirm == "0":
            print("\nOperação cancelada!")
            Utils.pause()
            return

        account_password = si.password_input(
            "\n - Digite uma senha de seis dígitos para transações da conta: ", 6
        )
        if account_password is None:
            return

        app_password = si.password_input(
            " - Digite uma senha de oito dígitos para login no app: ", 8
        )
        if app_password is None:
            return

        new_account = CheckingAccount(customer, account_password, app_password)
        print(f"\nConfira os dados da conta\n\n{new_account}")

        confirm = input(
            "Digite '0' para cancelar a operação ou qualquer outra tecla para confirmar: "
        )

        if confirm == "0":
            del new_account
            print("\nOperação cancelada!")
        else:
            account_repo.add_account(new_account)
            customer.link_account(new_account)
            print("\nUsuário cadastrado com sucesso!")

        Utils.pause()

    @staticmethod
    def create_savings_account(customer_repo, account_repo):
        Utils.print_header("Abrir Conta Poupança")
        print("Digite 0 a qualquer momento para cancelar a operação\n")

        opcao = LoginMenu.ask_natural_person_or_legal_entity()

        if opcao == "pf":
            id = si.cpf_input()
        elif opcao == "pj":
            id = si.cnpj_input()
        else:
            print("Operação cancelada!")
            Utils.pause()
            return

        if id is None:
            return

        customer = customer_repo.search_customer_by_id(id)
        if not customer:
            print("\nDado inserido não existe no sistema!")
            Utils.pause()
            return

        print(f"\n{customer}")

        confirm = input(
            "\nDigite '0' para cancelar ou qualquer outra tecla para confirmar o usuário: "
        )

        account_password = si.password_input(
            "\n - Digite uma senha de seis dígitos para transações da conta: ", 6
        )
        if account_password is None:
            return

        app_password = si.password_input(
            " - Digite uma senha de oito dígitos para login no app: ", 8
        )
        if app_password is None:
            return

        if confirm == "0":
            print("\nOperação cancelada!")
            Utils.pause()
            return

        new_account = SavingsAccount(customer, account_password, app_password)
        account_repo.add_account(new_account)
        customer.link_account(new_account)

        Utils.pause()

    @staticmethod
    def list_users(customer_repo):
        Utils.print_header("Listar Usuários")
        customers = customer_repo.list_all_customers()

        if not customers:
            print("Não há clientes cadastrados")
        else:
            print(f"Total de clientes: {customer_repo.count_customers()}\n")
            for customer in customers:
                print(f"{customer}")

        Utils.pause()

    @staticmethod
    def list_accounts(account_repo):
        Utils.print_header("Listar Contas")
        accounts = account_repo.list_all_accounts()

        if not accounts:
            print("Não há contas criadas")
        else:
            print(f"Total de contas: {account_repo.count_accounts()}\n")
            for account in accounts:
                print(f"{account}")

        Utils.pause()

    @staticmethod
    def login(account_repo):
        Utils.print_header("Entrar no Sistema")
        print("Digite 0 a qualquer momento para cancelar a operação\n")

        account_number = si.text_input(" - Número da conta: ")
        if account_number is None:
            return

        account = account_repo.search_account_by_number(account_number)
        if not account:
            print("\nConta não encontrada no sistema!")
            Utils.pause()
            return

        print(f"\n{account}")

        attempts = 0
        while attempts < 5:
            account_password = si.text_input(" - Senha do aplicativo: ")
            if account_password is None:
                return

            if account.app_password == account_password:
                print("\nLogin feito com sucesso!")
                Utils.pause()
                return account
            else:
                print("\nSenhas não conferem!")
                attempts += 1
        else:
            print("\nMuitas tentativas erradas!\nOperação cancelada!")
            Utils.pause()
            return None
