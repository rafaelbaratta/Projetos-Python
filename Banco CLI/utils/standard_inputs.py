from .utils import Utils
from .validations import Validations as val


class StandardInputs:
    MAX_ATTEMPTS = 5

    @staticmethod
    def cpf_input():
        attempts = 0
        while attempts < StandardInputs.MAX_ATTEMPTS:
            cpf = input(" - Insira seu CPF (apenas números): ")

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
    def text_input(message):
        text = input(message)

        if text == "0":
            print("\nOperação cancelada!")
            Utils.pause()
            return None
        else:
            return text

    @staticmethod
    def phone_input():
        while True:
            phone = input(" - Insira seu telefone (apenas números, com DDD): ")

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
            email = input(" - Insira seu e-mail: ")

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
            date = input(f" - Insira a data de {what}: ")

            if date == "0":
                print("\nOperação cancelada!")
                Utils.pause()
                return None

            valid, message = val.date_valid(date)

            if not valid:
                print(message)
            else:
                return date
