import re


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
    def phone_valid(phone):
        if len(phone) != 11:
            return False, "Telefone deve conter 11 ou 12 dígitos"

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

        date = date.split("-")

        if int(date[1]) > 12:
            return False, "Mês digitado inexistente"

        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if int(date[0]) > days[int(date[1]) - 1]:
            return False, "Dia digitado inexistente"

        return True, ""
