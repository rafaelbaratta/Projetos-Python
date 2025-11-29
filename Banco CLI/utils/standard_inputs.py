from .utils import Utils
from .validations import Validations as val


class StandardInputs:
    MAX_ATTEMPTS = 5

    @staticmethod
    def text_input(message_input):
        text = input(message_input)

        if text == "0":
            print("\nOperação cancelada!")
            Utils.pause()
            return None
        else:
            return text

    @staticmethod
    def cpf_input():
        attempts = 0
        while attempts < StandardInputs.MAX_ATTEMPTS:
            cpf = input(" - Digite seu CPF (apenas números): ")

            if cpf == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.cpf_valid(cpf)

            if not valid:
                attempts += 1
                print(message)
            else:
                return cpf
        else:
            print("Muitas tentativas erradas!\nOperação cancelada!")
            Utils.pause()
            return None

    @staticmethod
    def cnpj_input():
        attempts = 0
        while attempts < StandardInputs.MAX_ATTEMPTS:
            cnpj = input(" - Digite o CNPJ (apenas números): ")

            if cnpj == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.cnpj_valid(cnpj)

            if not valid:
                attempts += 1
                print(message)
            else:
                return cnpj
        else:
            print("Muitas tentativas erradas!\nOperação cancelada!")
            Utils.pause()
            return None

    @staticmethod
    def phone_input():
        while True:
            phone = input(" - Digite o telefone (apenas números, com DDD): ")

            if phone == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.phone_valid(phone)

            if not valid:
                print(message)
            else:
                return phone

    @staticmethod
    def email_input():
        while True:
            email = input(" - Digite o e-mail: ")

            if email == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.email_valid(email)

            if not valid:
                print(message)
            else:
                return email

    @staticmethod
    def date_input(what):
        while True:
            date = input(f" - Digite a data de {what} (DD-MM-AAAA): ")

            if date == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.date_valid(date)

            if not valid:
                print(message)
            else:
                return date

    @staticmethod
    def password_input(message_input, chars):
        attempts = 0
        while attempts < StandardInputs.MAX_ATTEMPTS:
            password = input(message_input)

            if password == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.password_valid(password, chars)

            if not valid:
                attempts += 1
                print(message)
            else:
                return password
        else:
            print("Muitas tentativas erradas!\nOperação cancelada!")
            Utils.pause()
            return None

    @staticmethod
    def money_input(message_input):
        while True:
            try:
                amount = float(input(message_input).replace(",", "."))
            except ValueError:
                print("\nDigite apenas números")
                continue

            if amount == 0:
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            if amount < 0:
                print("\nValor digitado deve ser positivo!")
                continue

            return amount

    @staticmethod
    def bill_code_input():
        while True:
            bill_code = input(" - Digite o código de barras do boleto: ")

            if bill_code == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.bill_code_valid(bill_code)

            if not valid:
                print(message)
            else:
                return bill_code
