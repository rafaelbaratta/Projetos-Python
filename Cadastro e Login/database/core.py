from tkinter import messagebox
from database import Database as db
from utils import Validations as val
from utils import Security as sec


class Core:

    @staticmethod
    def clear_entries(*entries):
        for entry in entries:
            entry.delete(0, "end")

    @staticmethod
    def register_user(register, show):
        username = register.name_entry.get()
        email = register.email_entry.get().lower()
        password = register.password_entry.get()
        password_repeated = register.password_repeat_entry.get()

        if val.has_blank_space_register(username, email, password, password_repeated):
            messagebox.showwarning(
                "Atenção!", "Certifique-se de preencher TODOS os campos!")
            return

        if len(password) < 6:
            messagebox.showwarning(
                "Atenção!", "A senha do usuário deve possuir no mínimo 6 dígitos!")
            return

        if not val.email_valid(email):
            messagebox.showwarning("Atenção!", "E-mail inválido inserido!")
            return

        if not val.passwords_match(password, password_repeated):
            messagebox.showwarning(
                "Atenção!", "As senhas inseridas não conferem!")
            return

        if db.search_user(email):
            messagebox.showwarning(
                "Atenção!", "O e-mail inserido já está em uso!")
            return

        password_hashed = sec.hash_password(password)

        db.insert_user(email, username, password_hashed)

        show("login")

        Core.clear_entries(register.name_entry, register.email_entry,
                           register.password_entry, register.password_repeat_entry)

    @staticmethod
    def login_user(login, main, show):
        email = login.email_entry.get().lower()
        password = login.password_entry.get()

        if val.has_blank_space_login(email, password):
            messagebox.showwarning(
                "Atenção!", "Certifique-se de preencher TODOS os campos!")
            return

        user = db.search_user(email)

        if not user:
            messagebox.showerror(
                "Erro!", "Usuário não existe no banco de dados!")
            return

        if not sec.verify_password(password, user[0][3]):
            messagebox.showerror("Erro!", "A senha inserida está incorreta!")
            return

        Core.load_user(main, user)

        show("main")

        Core.clear_entries(login.email_entry, login.password_entry)

        return user

    @staticmethod
    def load_user(main, user):
        if not user:
            return

        for entry in (main.name_entry, main.email_entry, main.password_entry):
            entry.configure(state="normal")

        Core.clear_entries(main.name_entry, main.email_entry,
                           main.password_entry)

        main.name_entry.insert(0, user[0][2])
        main.email_entry.insert(0, user[0][1])
        main.password_entry.insert(0, user[0][3])

        for entry in (main.name_entry, main.email_entry, main.password_entry):
            entry.configure(state="disabled")
