from abc import ABC, abstractmethod
from datetime import datetime

from utils import Formatters as fmt


class Customer(ABC):

    def __init__(self, email, phone, adress):
        self.adress = adress
        self.email = email
        self.phone = phone
        self.accounts = []

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class NaturalPerson(Customer):

    def __init__(self, cpf, name, birth_date, email, phone, adress):
        super().__init__(email, phone, adress)
        self.cpf = cpf
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()

    def get_id(self):
        return self.cpf

    def get_name(self):
        return self.name

    def get_age(self):
        today_date = datetime.today().date()
        return (today_date - self.birth_date).days // 365

    def __str__(self):
        return (
            f"{fmt.cpf_format(self.cpf)} - {self.name}\n"
            f"{fmt.date_format(self.birth_date)} : {self.get_age()} anos\n"
            f"{self.email} | {fmt.phone_format(self.phone)}\n"
            f"{self.adress}"
        )


class LegalEntity(Customer):

    def __init__(
        self, cnpj, company_name, trade_name, foundation_date, email, phone, adress
    ):
        super().__init__(email, phone, adress)
        self.cnpj = cnpj
        self.company_name = company_name
        self.trade_name = trade_name
        self.foundation_date = datetime.strptime(foundation_date, "%d-%m-%Y").date()

    def get_id(self):
        return self.cnpj

    def get_name(self):
        return self.company_name or self.trade_name

    def get_age(self):
        today_date = datetime.today().date()
        return (today_date - self.foundation_date).days // 365

    def __str__(self):
        return (
            f"{fmt.cnpj_format(self.cnpj)} - {self.company_name} ({self.trade_name})\n"
            f"{fmt.date_format(self.foundation_date)} : {self.get_age()} anos\n"
            f"{self.email} | {fmt.phone_format(self.phone)}\n"
            f"{self.adress}"
        )
