import re
from tkinter import messagebox


class InputValidations:

    @staticmethod
    def empty_entries(*strings):
        if "" in strings:
            return True

    @staticmethod
    def cpf_validation(cpf):
        return re.fullmatch(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", cpf)

    @staticmethod
    def phone_validation(phone):
        return re.fullmatch(r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}", phone)

    @staticmethod
    def email_validation(email):
        return re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

    @staticmethod
    def valid_inputs(entries):
        firstname = entries["firstname"].get()
        lastname = entries["lastname"].get()
        cpf = entries["cpf"].get()
        phone = entries["phone"].get()
        email = entries["email"].get()

        if InputValidations.empty_entries(
            firstname, lastname, email, cpf, phone, email
        ):
            messagebox.showerror("Erro!", "Certifique-se de preencher TODOS os campos!")
            return False

        if not InputValidations.email_validation(email):
            messagebox.showerror("Erro!", "Email inválido!")
            return False

        if not InputValidations.phone_validation(phone):
            messagebox.showerror(
                "Erro!",
                "Telefone inválido!"
                "Formatos possíveis: (11)11111-1111 ou 11111111111",
            )
            return False

        if not InputValidations.cpf_validation(cpf):
            messagebox.showerror(
                "Erro!",
                "CPF inválido! Use 11 dígitos!"
                "Formatos possíveis: 111.111.111-11 ou 11111111111",
            )
            return False

        return True
