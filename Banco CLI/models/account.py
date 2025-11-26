class Account:
    def __init__(self, numero_conta, cliente):
        self.numero = numero_conta
        self.agencia = "0001"
        self.cliente = cliente
        self.saldo = 0


class CheckingAccount(Account):
    def __init__(self, numero_conta, cliente, limite, limite_saques):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques


class SavingsAccount(Account):
    pass
