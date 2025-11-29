import re
from datetime import datetime


class Validations:

    @staticmethod
    def cpf_valid(cpf):
        if len(cpf) != 11:
            return False, "CPF deve conter 11 dígitos"

        if not cpf.isdigit():
            return False, "CPF deve conter apenas números"

        if Validations.verify_digits_cpf(cpf, 10) != int(cpf[9]):
            return False, "CPF inserido é inválido"

        if Validations.verify_digits_cpf(cpf, 11) != int(cpf[10]):
            return False, "CPF inserido é inválido"

        return True, ""

    @staticmethod
    def verify_digits_cpf(cpf, multiplier):
        sum = 0
        stop_digit = multiplier - 1
        for i, digit in enumerate(cpf):
            if i == stop_digit:
                break
            sum += int(digit) * multiplier
            multiplier -= 1

        sum %= 11

        if sum < 2:
            return 0
        else:
            return 11 - sum

    @staticmethod
    def cnpj_valid(cnpj):
        if len(cnpj) != 14:
            return False, "CNPJ deve conter 14 dígitos"

        if not cnpj.isalnum():
            return False, "CNPJ deve conter apenas letras e números"

        cnpj = cnpj.upper()

        NOT_ALLOWED_CHARACTERS = [chr(x) for x in range(75, 91)]

        for character in cnpj:
            if character.isalpha() and character in NOT_ALLOWED_CHARACTERS:
                return (
                    False,
                    "CNPJ contém letras inválidas. Use apenas letras de 'A' a 'J'",
                )

        cnpj_numbers = []

        for digit in cnpj:
            if digit.isalpha():
                digit = ord(digit) - ord("A")
            else:
                digit = int(digit)

            cnpj_numbers.append(digit)

        if Validations.verify_digits_cnpj(cnpj_numbers, 12) != int(cnpj_numbers[12]):
            return False, "CNPJ inserido é inválido"

        if Validations.verify_digits_cnpj(cnpj_numbers, 13) != int(cnpj_numbers[13]):
            return False, "CNPJ inserido é inválido"

        return True, ""

    @staticmethod
    def verify_digits_cnpj(cnpj, stop_digit):
        sum = 0
        if stop_digit == 12:
            multiplier = 5
        else:
            multiplier = 6

        for digit in cnpj[:stop_digit]:

            sum += digit * multiplier

            if multiplier == 2:
                multiplier = 9
            else:
                multiplier -= 1

        sum %= 11

        if sum < 2:
            return 0
        else:
            return 11 - sum

    @staticmethod
    def phone_valid(phone):
        if len(phone) != 11 and len(phone) != 10:
            return False, "Telefone deve conter 10 ou 11 dígitos"

        if not phone.isdigit():
            return False, "Telefone deve conter apenas números"

        DDD = [
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "21",
            "22",
            "24",
            "27",
            "28",
            "31",
            "32",
            "33",
            "34",
            "35",
            "37",
            "38",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "48",
            "49",
            "51",
            "53",
            "54",
            "55",
            "61",
            "62",
            "63",
            "64",
            "65",
            "66",
            "67",
            "68",
            "69",
            "71",
            "73",
            "74",
            "75",
            "77",
            "79",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "89",
            "91",
            "92",
            "93",
            "94",
            "95",
            "96",
            "97",
            "98",
            "99",
        ]

        if phone[0:2] not in DDD:
            return False, "DDD inserido não existe"

        return True, ""

    @staticmethod
    def email_valid(email):
        if not re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            return False, "E-mail digitado é inválido"

        return True, ""

    @staticmethod
    def date_valid(date):
        if not re.fullmatch(r"[0-9]{2}+-[0-9]{2}+-[0-9]{4}", date):
            return False, "Data digitada em formato errado"

        today_date = datetime.today().date()
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if int(date[6:]) > today_date.year or int(date[6:]) < 1500:
            return False, "Ano digitado inválido"

        if int(date[3:5]) > 12 or int(date[3:5]) < 1:
            return False, "Mês digitado inválido"

        if int(date[:2]) > days[int(date[3:5]) - 1] or int(date[:2]) < 1:
            return False, "Dia digitado inválido"

        date = datetime.strptime(date, "%d-%m-%Y").date()

        age = (today_date - date).days // 365

        if age < 0:
            return False, "Data digitada é inválida"

        return True, ""

    @staticmethod
    def password_valid(password, chars):
        if len(password) != chars:
            return False, f"Senha deve possuir exatamente {chars} caracteres"

        if not password.isdigit():
            return False, "Senha deve conter apenas números"

        return True, ""

    @staticmethod
    def bill_code_valid(bill_code):
        if len(bill_code) != 47 and len(bill_code) != 48:
            return False, f"Quantidade inválida de dígitos do código de barras"

        if not bill_code.isdigit():
            return False, "Código de barras deve conter apenas números"

        return True, ""
