import customtkinter as ctk


class MainScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        pad_x = 10
        pad_y = 20

        self.build(pad_x, pad_y)

    def build(self, pad_x, pad_y):

        ctk.CTkLabel(self, text="Suas Informações", font=("Arial", 30)).pack(pady=pad_y)

        form_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        form_frame.pack(fill="both", expand=True, padx=pad_x)

        form_frame.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(form_frame, text="Nome:", font=("Arial", 18)).grid(
            row=0, column=0, sticky="e", padx=pad_x
        )
        self.name_entry = ctk.CTkEntry(
            form_frame, font=("Arial", 18), width=300, height=40, state="disabled"
        )
        self.name_entry.grid(row=0, column=1, sticky="w", pady=pad_y, padx=pad_x)

        ctk.CTkLabel(form_frame, text="E-mail:", font=("Arial", 18)).grid(
            row=1, column=0, sticky="e", padx=pad_x
        )
        self.email_entry = ctk.CTkEntry(
            form_frame, font=("Arial", 18), width=300, height=40, state="disabled"
        )
        self.email_entry.grid(row=1, column=1, sticky="w", pady=pad_y, padx=pad_x)

        ctk.CTkLabel(form_frame, text="Senha:", font=("Arial", 18)).grid(
            row=2, column=0, sticky="e", padx=pad_x
        )
        self.password_entry = ctk.CTkEntry(
            form_frame, font=("Arial", 18), width=300, height=40, state="disabled"
        )
        self.password_entry.grid(row=2, column=1, sticky="w", pady=pad_y, padx=pad_x)

        button_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        button_frame.pack(fill="both", expand=True, padx=pad_x, pady=pad_y)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        self.edit_button = ctk.CTkButton(
            button_frame, height=50, width=150, text="Editar", font=("Arial", 18)
        )
        self.edit_button.grid(row=0, column=0, sticky="e", padx=pad_x)

        self.delete_button = ctk.CTkButton(
            button_frame, height=50, width=150, text="Excluir", font=("Arial", 18)
        )
        self.delete_button.grid(row=0, column=1, sticky="w", padx=pad_x)

        self.exit_button = ctk.CTkButton(
            self, height=50, width=150, text="Desconectar", font=("Arial", 18)
        )
        self.exit_button.pack(padx=pad_x, pady=(0, pad_y))
