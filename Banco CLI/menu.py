from models import LegalEntity, NaturalPerson
from utils import StandardInputs as s_input
from utils import Utils


class Menu:
    SYSTEM = (
        "======================================\n"
        "== -------- AGÊNCIA BANCÁRIA ------ ==\n"
        "======================================\n"
    )
    LOGIN_MENU = (
        "       [1] Registrar Usuário\n"
        "       [2] Abrir Conta\n"
        "       [3] Listar Usuários\n"
        "       [4] Listar Contas\n"
        "       [5] Entrar no Sistema\n"
        "       [0] Sair do Sistema\n\n"
        "== --> "
    )
    MAIN_MENU = (
        "       [1] Depósito\n"
        "       [2] Saque\n"
        "       [3] Transferência\n"
        "       [4] Consultar Saldo\n"
        "       [5] Verificar Extrato\n"
        "       [0] Desconectar\n\n"
        "== --> "
    )

    @staticmethod
    def print_menu(screen):
        Utils.clean_screen()
        print(Menu.SYSTEM)
        print(f" < {f' {screen} '.center(32, '-')} > \n")

    @staticmethod
    def login_menu():
        while True:
            Menu.print_menu("Menu Inicial")
            opcao = input(Menu.LOGIN_MENU).strip()

            match opcao:
                case "1":
                    LoginMenu.register_user()
                case "2":
                    LoginMenu.create_account()
                case "3":
                    LoginMenu.list_users()
                case "4":
                    LoginMenu.list_accounts()
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
            Menu.print_menu("Menu Principal")
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


class LoginMenu:

    @staticmethod
    def register_user():
        Menu.print_menu("Registrar Usuário")
        opcao = input("Pessoa física ou jurídica [pf/pj]? ").lower().strip()

        while opcao != "pf" and opcao != "pj":
            opcao = input("Digite apenas 'pf' ou 'pj': ")

        if opcao == "pf":
            LoginMenu.register_natural_person()
        else:
            LoginMenu.register_legal_entity()

    @staticmethod
    def register_natural_person():
        Menu.print_menu("Registrar Pessoa Física")
        print("Digite 0 a qualquer momento para cancelar a operação\n")

        cpf = s_input.cpf_input()
        if cpf is None:
            return

        name = s_input.text_input(" - Insira seu nome: ")
        if name is None:
            return

        phone = s_input.phone_input()
        if phone is None:
            return

        email = s_input.email_input()
        if email is None:
            return

        birth_date = s_input.date_input("nascimento")
        if birth_date is None:
            return

        adress = s_input.text_input(" - Insira seu endereço: ")
        if adress is None:
            return

        new_user = NaturalPerson(cpf, name, birth_date, email, phone, adress)
        new_user.add_user()

        Utils.pause()

    def register_legal_entity():
        Menu.print_menu("Registrar Pessoa Jurídica")
        Utils.pause()

    def create_account():
        Menu.print_menu("Abrir Conta")
        Utils.pause()

    def list_users():
        Menu.print_menu("Listar Usuários")
        for user in NaturalPerson.list_users():
            print(user)
        Utils.pause()

    def list_accounts():
        Menu.print_menu("Listar Contas")
        Utils.pause()

    def login():
        Menu.print_menu("Entrar no Sistema")
        Menu.main_menu()


class MainMenu:
    def deposit():
        Menu.print_menu("Depósito")
        Utils.pause()

    def withdrawal():
        Menu.print_menu("Saque")
        Utils.pause()

    def transference():
        Menu.print_menu("Transferência")
        Utils.pause()

    def see_balance():
        Menu.print_menu("Consultar Saldo")
        Utils.pause()

    def see_statement():
        Menu.print_menu("Verificar Extrato")
        Utils.pause()


def menu():
    return """
          ===== AGÊNCIA BANCÁRIA =====

                [d] Depositar
                [s] Sacar
                [e] Extrato
                [u] Cadastrar Usuário
                [c] Criar Conta
                [lu] Listar Usuários
                [lc] Listar Contas
                [q] Sair

          => """


def deposito(saldo, valor, extrato, /):
    print("===== REALIZAR DEPÓSITO =====\n")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print("===== REALIZAR SAQUE =====\n")
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def extrato(saldo, /, *, extrato):
    print("===== VERIFICAR EXTRATO =====\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================")


def cadastrar_usuario(usuarios):
    print("===== CADASTRAR USUÁRIO =====\n")
    nome = input("\nDigite o seu nome: ")
    data_nascimento = input("Insira sua data de nascimento: ")
    cpf = input("Insira seu CPF (apenas numeros): ")
    while not cpf.isnumeric:
        cpf = input("Insira seu CPF CORRETAMENTE (apenas numeros): ")
    endereco = input("Insira seu endereço (logradouro, nº - bairro - cidade/UF): ")

    for dicionario in usuarios:
        if cpf in dicionario.values():
            print("\nCPF inserido já está em uso!")
            return

    usuarios.append(
        {
            "nome": nome,
            "data de nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )


def criar_conta(agencia, contas, usuarios):
    numero_conta = len(contas) + 1
    print("===== CRIAR CONTA =====\n")
    cpf = input("\nDigite cpf do dono da conta: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não cadastrado no sistema!")
        return

    contas.append(
        {"agencia": agencia, "numero da conta": numero_conta, "usuario": usuario}
    )


def filtrar_usuario(cpf, usuarios):
    for dicionario in usuarios:
        if dicionario.get("cpf") == cpf:
            return dicionario.get("nome")
    return None


def listar_usuarios(usuarios):
    print("===== LISTAR USUÁRIOS =====\n")

    if not usuarios:
        print("\nNão há usuários no sistema.")
        return

    for dicionario in usuarios:
        print(f"Nome: {dicionario['nome']}")
        print(f"Data de Nascimento: {dicionario['data de nascimento']}")
        print(f"CPF: {dicionario['cpf']}")
        print(f"Endereço: {dicionario['endereco']}\n")


def listar_contas(contas):
    print("===== LISTAR USUÁRIOS =====\n")

    if not contas:
        print("\nNão há contas no sistema.")
        return

    for dicionario in contas:
        print(
            f"{dicionario['agencia']} - {dicionario['numero da conta']} : {dicionario['usuario']}"
        )


if __name__ == "__main__":
    Menu.login_menu()
