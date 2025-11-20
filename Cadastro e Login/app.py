import customtkinter as ctk
from database import Core
from screens import LoginScreen
from screens import RegisterScreen
from screens import MainScreen


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.core = Core()

        min_width = 580
        min_height = 500

        self.build(min_width, min_height)

    def build(self, min_width, min_height):
        self.title("App Usuários")
        self._set_appearance_mode("System")
        self.geometry(f"{min_width}x{min_height}")
        self.minsize(min_width, min_height)

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.screens = {}

        for screen in (LoginScreen, RegisterScreen, MainScreen):
            screen_name = screen.__name__.replace("Screen", "").lower()
            screen_frame = screen(self.container, self)
            self.screens[screen_name] = screen_frame
            screen_frame.grid(row=0, column=0, sticky="nsew")

        self.configure_buttons()
        self.show_screen("login")

    def configure_buttons(self):
        login_screen = self.screens["login"]
        login_screen.login_button.configure(command=lambda: self.core.login_user(
            login_screen, main_screen, app.show_screen))
        login_screen.register_button.configure(command=lambda: (self.core.clear_entries(
            login_screen.email_entry, login_screen.password_entry), self.show_screen("register")))

        register_screen = self.screens["register"]
        register_screen.login_button.configure(command=lambda: (self.core.clear_entries(
            register_screen.name_entry, register_screen.email_entry, register_screen.password_entry, register_screen.password_repeat_entry), self.show_screen("login")))
        register_screen.register_button.configure(
            command=lambda: self.core.register_user(register_screen, app.show_screen))

        main_screen = self.screens["main"]
        main_screen.exit_button.configure(
            command=lambda: self.show_screen("login"))

    def show_screen(self, screen_name):
        frame = self.screens[screen_name]
        frame.tkraise()

    def characters_limit(self, text, max_chars):
        return len(text) <= int(max_chars)


if __name__ == "__main__":
    app = App()
    app.mainloop()
