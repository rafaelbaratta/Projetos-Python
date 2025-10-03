import re
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

from database import DataBase

class CreateAccountWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    repeat_password = ObjectProperty(None)

    def submit(self):
        if (self.username.text != '' and 
            self.email.text != '' and
            re.match(r"[^@]+@[^@]+\.[^@]+", self.email.text) and
            self.password.text != '' and
            self.repeat_password.text != '' and
            self.password.text == self.repeat_password.text):

            if db.add_user(self.email.text, self.password.text, self.repeat_password.text, self.username.text):
                self.reset()
                sm.current = "login"
            else:
                invalid_form()
        
        else:
            invalid_form()
    
    def login(self):
        self.reset()
        sm.current = "login"
    
    def reset(self):
        self.email.text = ''
        self.username.text = ''
        self.password.text = ''
        self.repeat_password.text = ''


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_button(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalid_login()
    
    def create_button(self):
        self.reset()
        sm.current = "create"
    
    def reset(self):
        self.email.text = ''
        self.password.text = ''


class MainWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    created = ObjectProperty(None)
    current = ""

    def logout(self):
        sm.current = "login"
    
    def on_enter(self, *args):
        password, username, created = db.get_user(self.current)
        self.username.text = username
        self.email.text = self.current
        self.created.text = created


class WindowManager(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return sm


def invalid_login():
    show_popup("Login inválido", "Usuário ou senha inválida.")

def invalid_form():
    show_popup("Campos inválidos ou vazios", "Por favor, preencha todos os campos corretamente.")

def show_popup(title, content):
    layout = BoxLayout(orientation = 'vertical', spacing = 10, padding = 10)
    label = Label(text = content, font_size = 30)
    close_button = Button(text = "Fechar", size_hint = (1, 0.3))

    layout.add_widget(label)
    layout.add_widget(close_button)

    popup = Popup(title = title,
                content = layout)
    
    close_button.bind(on_release = lambda *args: popup.dismiss())

    popup.open()

kv = Builder.load_file("interface.kv")
sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]

for screen in screens:
    sm.add_widget(screen)

if __name__ == "__main__":
    MainApp().run()
