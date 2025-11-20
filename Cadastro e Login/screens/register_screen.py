import customtkinter as ctk


class RegisterScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        validate = self.register(controller.characters_limit)

        pad_x = 10
        pad_y = 15

        self.build(pad_x, pad_y, validate)

    def build(self, pad_x, pad_y, validate):

        ctk.CTkLabel(self, text="Criar uma Conta",
                     font=("Arial", 30)).pack(pady=pad_y)

        form_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        form_frame.pack(fill="both", expand=True, padx=pad_x, pady=pad_y)

        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(form_frame, text="Nome:", font=("Arial", 18)).grid(
            row=0, column=0, sticky='e', padx=pad_x)
        self.name_entry = ctk.CTkEntry(
            form_frame, font=("Arial", 18), width=300, height=40)
        self.name_entry.grid(row=0, column=1, sticky='w',
                             pady=pad_y, padx=pad_x)
        self.name_entry.configure(
            validate="key", validatecommand=(validate, "%P", 255))

        ctk.CTkLabel(form_frame, text="E-mail:", font=("Arial", 18)
                     ).grid(row=1, column=0, sticky='e', padx=pad_x)
        self.email_entry = ctk.CTkEntry(
            form_frame, font=("Arial", 18), width=300, height=40)
        self.email_entry.grid(row=1, column=1, sticky='w',
                              pady=pad_y, padx=pad_x)
        self.email_entry.configure(
            validate="key", validatecommand=(validate, "%P", 255))

        ctk.CTkLabel(form_frame, text="Senha:", font=("Arial", 18)).grid(
            row=2, column=0, sticky='e', padx=pad_x)
        self.password_entry = ctk.CTkEntry(form_frame, font=(
            "Arial", 18), width=300, height=40, show='*')
        self.password_entry.grid(
            row=2, column=1, sticky='w', pady=pad_y, padx=pad_x)
        self.password_entry.configure(
            validate="key", validatecommand=(validate, "%P", 40))

        ctk.CTkLabel(form_frame, text="Repetir Senha:", font=(
            "Arial", 18)).grid(row=3, column=0, sticky='e', padx=pad_x)
        self.password_repeat_entry = ctk.CTkEntry(
            form_frame, font=("Arial", 18), width=300, height=40, show='*')
        self.password_repeat_entry.grid(
            row=3, column=1, sticky='w', pady=pad_y, padx=pad_x)
        self.password_repeat_entry.configure(
            validate="key", validatecommand=(validate, "%P", 40))

        button_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        button_frame.pack(fill="both", expand=True, padx=pad_x, pady=pad_y)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        self.register_button = ctk.CTkButton(
            button_frame, height=50, width=150, text="Criar Conta", font=("Arial", 18))
        self.register_button.grid(row=0, column=0, sticky='e', padx=pad_x)

        self.login_button = ctk.CTkButton(
            button_frame, height=50, width=150, text="Voltar ao Login", font=("Arial", 18))
        self.login_button.grid(row=0, column=1, sticky='w', padx=pad_x)
