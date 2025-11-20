import sqlite3 as sql
from tkinter import messagebox


class DatabaseConnection:
    database = "data/users.db"
    connection = None
    cursor = None
    is_connected = False

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()
        self.is_connected = True

    def disconnect(self):
        self.connection.close()
        self.is_connected = False

    def execute(self, sql, parameters=None):
        if self.is_connected:
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
        if self.is_connected:
            self.connection.commit()
            return True
        else:
            return False


class Database:

    @staticmethod
    def init_database():
        try:
            with DatabaseConnection() as db:
                db.execute("CREATE TABLE IF NOT EXISTS users "
                           "(id INTEGER PRIMARY KEY NOT NULL,"
                           "email VARCHAR(256) UNIQUE,"
                           "name VARCHAR(256),"
                           "password VARCHAR(100) NOT NULL)")
                db.persist()
        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao iniciar o banco de dados")

    @staticmethod
    def insert_user(email, name, password):
        try:
            with DatabaseConnection() as db:
                db.execute(
                    "INSERT INTO users (email, name, password) VALUES (?, ?, ?)", (email, name, password))
                db.persist()

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao inserir usuário no banco de dados")

    @staticmethod
    def search_user(email):
        try:
            with DatabaseConnection() as db:
                db.execute("SELECT * FROM users WHERE email = ?", (email,))
                user = db.fetchall()
                return user

        except:
            messagebox.showerror(
                "Erro!", "Houve um erro ao procurar usuário no banco de dados")
            return []


Database.init_database()
