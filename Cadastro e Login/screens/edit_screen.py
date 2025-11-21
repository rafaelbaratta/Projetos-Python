import customtkinter as ctk


class EditScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        validate = self.register(controller.characters_limit)

        pad_x = 10
        pad_y = 20

        self.build(pad_x, pad_y, validate)

    def build(self, pad_x, pad_y, validate):

        ctk.CTkLabel(self, text="Editar Usuário", font=("Arial", 30)).pack(pady=pad_y)

        form_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        form_frame.pack(fill="both", expand=True, padx=pad_x, pady=pad_y)

        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(form_frame, text="Nome:", font=("Arial", 18)).grid(
            row=0, column=0, sticky="e", padx=pad_x
        )
        self.name_entry = ctk.CTkEntry(
            form_frame, font=("Arial", 18), width=300, height=40
        )
        self.name_entry.grid(row=0, column=1, sticky="w", pady=pad_y, padx=pad_x)
        self.name_entry.configure(validate="key", validatecommand=(validate, "%P", 255))

        ctk.CTkLabel(form_frame, text="Senha:", font=("Arial", 18)).grid(
            row=2, column=0, sticky="e", padx=pad_x
        )

        ctk.CTkLabel(
            form_frame,
            text="(deixe em branco para manter a senha atual)",
            font=("Arial", 12),
            text_color="gray",
        ).grid(row=1, column=1, sticky="nw", padx=pad_x)

        self.password_entry = ctk.CTkEntry(
            form_frame,
            font=("Arial", 18),
            width=300,
            height=40,
            show="*",
        )
        self.password_entry.grid(row=2, column=1, sticky="w", pady=pad_y, padx=pad_x)
        self.password_entry.configure(
            validate="key", validatecommand=(validate, "%P", 40)
        )

        button_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        button_frame.pack(fill="both", expand=True, padx=pad_x, pady=pad_y)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        self.confirm_button = ctk.CTkButton(
            button_frame, height=50, width=150, text="Confirmar", font=("Arial", 18)
        )
        self.confirm_button.grid(row=0, column=0, sticky="e", padx=pad_x)

        self.cancel_button = ctk.CTkButton(
            button_frame,
            height=50,
            width=150,
            text="Cancelar",
            font=("Arial", 18),
        )
        self.cancel_button.grid(row=0, column=1, sticky="w", padx=pad_x)
