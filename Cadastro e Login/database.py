import datetime as dt
import hashlib as hs

class DataBase:

    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load_file()
    
    def load_file(self):
        self.file = open(self.filename, 'r')
        self.users = {}

        for line in self.file:
            email, password, username, created = line.strip().split(';')
            self.users[email] = (password, username, created)
        
        self.file.close()
    
    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        return -1

    def add_user(self, email, password, repeat_password, username):
        if email.strip() not in self.users and password == repeat_password:
            hashed_password = hs.sha256(password.encode()).hexdigest()
            self.users[email.strip()] = (hashed_password.strip(), username.strip(), DataBase.get_date())
            self.save()
            return 1
        return 0

    def validate(self, email, password):
        hashed_password = hs.sha256(password.encode()).hexdigest()
        if self.get_user(email) != -1:
            return self.users[email][0] == hashed_password
        return False
    
    def save(self):
        with open(self.filename, 'w') as file:
            for user in self.users:
                file.write(user + ';' + self.users[user][0] + ';' + self.users[user][1] + ';' + self.users[user][2] + '\n')

    @staticmethod
    def get_date():
        return str(dt.datetime.now()).split(' ')[0]
