from datetime import datetime


class Formatters:

    @staticmethod
    def cpf_format(cpf):
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    @staticmethod
    def cnpj_format(cnpj):
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

    @staticmethod
    def phone_format(phone):
        if len(phone) == 11:
            return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
        else:
            return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"

    @staticmethod
    def date_format(date):
        return date.strftime("%d/%m/%Y")
