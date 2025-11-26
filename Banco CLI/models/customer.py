from abc import ABC, abstractmethod


class Customer(ABC):

    def __init__(self, adress, email, phone):
        self.adress = adress
        self.email = email
        self.phone = phone
        self.accounts = []


class NaturalPerson(Customer):
    natural_person = []

    def __init__(self, cpf, name, birth_date, email, phone, adress):
        super().__init__(adress, email, phone)
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date


class LegalEntity(Customer):

    def __init__(
        self, cnpj, company_name, trade_name, foundation_date, adress, email, phone
    ):
        super().__init__(adress, email, phone)
        self.cnpj = cnpj
        self.company_name = company_name
        self.trade_name = trade_name
        self.foundation_date = foundation_date
