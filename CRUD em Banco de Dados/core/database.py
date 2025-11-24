import sqlite3 as sql
from tkinter import messagebox


class DatabaseConnection:
    database = "data/clients.db"
    connection = None
    cursor = None
    connected = False

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()
        self.connected = True

    def disconnect(self):
        self.connection.close()
        self.connected = False

    def execute(self, sql, parameters=None):
        if self.connected:
            if parameters == None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, parameters)
            return True
        else:
            return False

    def fetchall(self):
        return self.cursor.fetchall()

    def persist(self):
        if self.connected:
            self.connection.commit()
            return True
        else:
            return False


class Database:

    @staticmethod
    def init_database():
        try:
            with DatabaseConnection() as db:

                db.execute(
                    "CREATE TABLE IF NOT EXISTS clients "
                    "(id INTEGER PRIMARY KEY NOT NULL,"
                    "firstname TEXT,"
                    "lastname TEXT, "
                    "email TEXT, "
                    "cpf TEXT, "
                    "phone TEXT)"
                )
                db.persist()

        except:
            messagebox.showerror("Erro!", "Houve um erro ao iniciar o banco de dados")

    @staticmethod
    def insert(firstname, lastname, email, cpf, phone):
        try:
            with DatabaseConnection() as db:

                db.execute(
                    "INSERT INTO clients (firstname, lastname, email, cpf, phone) VALUES (?, ?, ?, ?, ?)",
                    (firstname, lastname, email, cpf, phone),
                )
                db.persist()

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao inserir usuário no banco de dados"
            )

    @staticmethod
    def view_all():
        try:
            with DatabaseConnection() as db:

                db.execute("SELECT * FROM clients")
                rows = db.fetchall()

                return rows

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao buscar todos os usuários no banco de dados"
            )
            return []

    @staticmethod
    def search(firstname="", lastname="", email="", cpf="", phone=""):
        try:
            with DatabaseConnection() as db:

                db.execute(
                    "SELECT * FROM clients "
                    "WHERE firstname LIKE ? "
                    "AND lastname LIKE ? "
                    "AND email LIKE ? "
                    "AND cpf LIKE ? "
                    "AND phone LIKE ? ",
                    (
                        f"%{firstname}%",
                        f"%{lastname}%",
                        f"%{email}%",
                        f"%{cpf}%",
                        f"%{phone}%",
                    ),
                )
                rows = db.fetchall()

                return rows

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao procurar usuário no banco de dados"
            )
            return []

    @staticmethod
    def delete(id):
        try:
            with DatabaseConnection() as db:

                db.execute("DELETE FROM clients WHERE id = ?", (id,))
                db.persist()

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao excluir usuário do banco de dados"
            )

    @staticmethod
    def delete_all():
        try:
            with DatabaseConnection() as db:

                db.execute("DELETE FROM clients")
                db.persist()

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao excluir todos os usuários do banco de dados"
            )

    @staticmethod
    def update(id, firstname, lastname, email, cpf, phone):
        try:
            with DatabaseConnection() as db:

                db.execute(
                    "UPDATE clients SET firstname = ?, lastname = ?, email = ?, cpf = ?, phone = ? WHERE id = ?",
                    (firstname, lastname, email, cpf, phone, id),
                )
                db.persist()

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao atualizar usuário no banco de dados"
            )


Database.init_database()
