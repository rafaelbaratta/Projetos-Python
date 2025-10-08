from frontend import Gui
from tkinter import messagebox
import re

class InputValidations():

    def cpf_validation(self, cpf):
        return re.fullmatch(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", cpf)
    
    def phone_validation(self, phone):
        return re.fullmatch(r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}", phone)
    
    def email_validation(self, email):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email)
    
    def valid_inputs(self):
        ui = Gui()
        firstname = ui.entry_firstname.get()
        lastname = ui.entry_lastname.get()
        cpf = ui.entry_cpf.get()
        phone = ui.entry_phone.get()
        email = ui.entry_email.get()

        if not all([firstname, lastname, email, cpf, phone, email]):
            messagebox.showerror("Erro!", "Certifique-se de preencher TODOS os campos!")
            return False

        if not self.email_validation(email):
            messagebox.showerror("Erro!", "Email inválido!")
            return False
        
        if not self.phone_validation(phone):
            messagebox.showerror("Erro!", "Telefone inválido!" \
                                 "Formatos possíveis: (11)11111.1111 ou 11111111111")
            return False

        if not self.cpf_validation(cpf):
            messagebox.showerror("Erro!", "CPF inválido! Use 11 dígitos!" \
                                 "Formatos possíveis: 111.111.111-11 ou 11111111111")
            return False
        
        return True
