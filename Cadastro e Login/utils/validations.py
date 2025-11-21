import re


class Validations:

    @staticmethod
    def has_blank_space_register(username, email, password, password_repeated):
        return "" in (username, email, password, password_repeated)

    @staticmethod
    def has_blank_space_login(email, password):
        return "" in (email, password)

    @staticmethod
    def email_valid(email):
        return re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

    @staticmethod
    def passwords_match(password, password_repeated):
        return password == password_repeated
