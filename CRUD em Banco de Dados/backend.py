import sqlite3 as sql

class TransactionObject():
    database = "clients.db"
    connection = None
    cursor = None
    connected = False

    def connect(self):
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()
        self.connected = True
    
    def disconnect(self):
        self.connection.close()
        self.connected = False
    
    def execute(self, sql, parameters = None):
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
    
def initDB():
    try:
        to = TransactionObject()
        to.connect()

        to.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY NOT NULL, firstname TEXT, lastname TEXT, email TEXT, cpf TEXT, phone TEXT)")
        to.persist()
        to.disconnect()

    except:
        print(f"Erro ao acessar o banco de dados!")

    finally:
        if to.connected:
            to.disconnect()

def insert(firstname, lastname, email, cpf, phone):
    try:
        to = TransactionObject()
        to.connect()

        to.execute("INSERT INTO clients (firstname, lastname, email, cpf, phone) VALUES (?, ?, ?, ?, ?)", (firstname, lastname, email, cpf, phone))
        to.persist()
        to.disconnect()

    except:
        print("Erro ao acessar o banco de dados!")

    finally:
        if to.connected:
            to.disconnect()

def view_all():
    try:
        to = TransactionObject()
        to.connect()

        to.execute("SELECT * FROM clients")
        rows = to.fetchall()
        to.disconnect()

        return rows
    
    except:
        print("Erro ao acessar o banco de dados!")
        return []
    
    finally:
        if to.connected:
            to.disconnect()

def search(firstname = "", lastname = "", email = "", cpf = "", phone = ""):
    try:
        to = TransactionObject()
        to.connect()

        to.execute("SELECT * FROM clients WHERE firstname = ? OR lastname = ? OR email = ? OR cpf = ? OR phone = ?", (firstname, lastname, email, cpf, phone))
        rows = to.fetchall()
        to.disconnect()

        return rows
    
    except:
        print("Erro ao acessar o banco de dados!")
        return []
    
    finally:
        if to.connected:
            to.disconnect()

def delete(id):
    try:
        to = TransactionObject()
        to.connect()

        to.execute("DELETE FROM clients WHERE id = ?", (id,))
        to.persist()
        to.disconnect()

    except:
        print("Erro ao acessar o banco de dados!")

    finally:
        if to.connected:
            to.disconnect()

def delete_all():
    try:
        to = TransactionObject()
        to.connect()

        to.execute("DELETE FROM clients")
        to.persist()
        to.disconnect()
    
    except:
        print("Erro ao acessar o banco de dados!")
    
    finally:
        if to.connected:
            to.disconnect()

def update(id, firstname, lastname, email, cpf, phone):
    try:
        to = TransactionObject()
        to.connect()

        to.execute("UPDATE clients SET firstname = ?, lastname = ?, email = ?, cpf = ?, phone = ? WHERE id = ?", (firstname, lastname, email, cpf, phone, id))
        to.persist()
        to.disconnect()

    except:
        print("Erro ao acessar o banco de dados!")

    finally:
        if to.connected:
            to.disconnect()

initDB()
