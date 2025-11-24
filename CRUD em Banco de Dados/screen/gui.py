import tkinter as tk

import customtkinter as ctk


class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.x_pad = 5
        self.y_pad = 10
        self.y_pad_button = 5
        self.font = ("Arial", 16)

        self.build()

    def build(self):
        self.title("CRUD de Clientes em Python com SQLite")
        self.geometry("700x500")
        self.minsize(700, 500)
        self._set_appearance_mode("System")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=4)
        self.grid_columnconfigure(6, weight=0)

        for i in range(5):
            self.grid_rowconfigure(i, weight=0)

        for i in range(5, 10):
            self.grid_rowconfigure(i, weight=1)

        ctk.CTkLabel(self, text="Nome:", font=self.font).grid(
            row=0, column=0, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )
        self.entry_firstname = ctk.CTkEntry(self, font=self.font)
        self.entry_firstname.grid(
            row=0, column=1, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )

        ctk.CTkLabel(self, text="Sobrenome:", font=self.font).grid(
            row=1, column=0, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )
        self.entry_lastname = ctk.CTkEntry(self, font=self.font)
        self.entry_lastname.grid(
            row=1, column=1, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )

        ctk.CTkLabel(self, text="E-mail:", font=self.font).grid(
            row=2, column=0, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )
        self.entry_email = ctk.CTkEntry(
            self, font=self.font, placeholder_text="exemplo@email.com"
        )
        self.entry_email.grid(
            row=2, column=1, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )

        ctk.CTkLabel(self, text="CPF:", font=self.font).grid(
            row=3, column=0, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )
        self.entry_cpf = ctk.CTkEntry(
            self, font=self.font, placeholder_text="123.456.789-10 / 12345678910"
        )
        self.entry_cpf.grid(
            row=3, column=1, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )

        ctk.CTkLabel(self, text="Telefone:", font=self.font).grid(
            row=4, column=0, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )
        self.entry_phone = ctk.CTkEntry(
            self, font=self.font, placeholder_text="(19) 12345-6789 / 19123456789"
        )
        self.entry_phone.grid(
            row=4, column=1, padx=self.x_pad, pady=self.y_pad, sticky="nsew"
        )

        self.list_clients = tk.Listbox(self)
        self.list_clients.grid(
            row=0, column=2, padx=self.x_pad, pady=self.y_pad, rowspan=13, sticky="nsew"
        )

        self.scroll_clients = ctk.CTkScrollbar(self)
        self.scroll_clients.grid(
            row=0, column=6, padx=self.x_pad, pady=self.y_pad, rowspan=13, sticky="ns"
        )

        self.list_clients.configure(yscrollcommand=self.scroll_clients.set)
        self.scroll_clients.configure(command=self.list_clients.yview)

        buttons_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        buttons_frame.grid(
            row=5, column=0, columnspan=2, sticky="nsew", padx=self.x_pad
        )
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)

        self.button_clear_entries = ctk.CTkButton(
            buttons_frame, text="Limpar Entradas", font=self.font
        )
        self.button_clear_entries.grid(
            row=5,
            column=0,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_clear_selection = ctk.CTkButton(
            buttons_frame, text="Limpar Seleção", font=self.font
        )
        self.button_clear_selection.grid(
            row=5,
            column=1,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_insert = ctk.CTkButton(
            buttons_frame, text="Inserir", font=self.font
        )
        self.button_insert.grid(
            row=6,
            column=0,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_update = ctk.CTkButton(
            buttons_frame, text="Atualizar", font=self.font
        )
        self.button_update.grid(
            row=6,
            column=1,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_search = ctk.CTkButton(buttons_frame, text="Buscar", font=self.font)
        self.button_search.grid(
            row=7,
            column=0,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_search_all = ctk.CTkButton(
            buttons_frame, text="Buscar todos", font=self.font
        )
        self.button_search_all.grid(
            row=7,
            column=1,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_delete = ctk.CTkButton(
            buttons_frame, text="Excluir", font=self.font
        )
        self.button_delete.grid(
            row=8,
            column=0,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_delete_all = ctk.CTkButton(
            buttons_frame, text="Excluir Tudo", font=self.font
        )
        self.button_delete_all.grid(
            row=8,
            column=1,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_generate_txt_file = ctk.CTkButton(
            buttons_frame, text="Gerar Arquivo txt", font=self.font
        )
        self.button_generate_txt_file.grid(
            row=9,
            column=0,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_generate_csv_file = ctk.CTkButton(
            buttons_frame, text="Gerar Arquivo csv", font=self.font
        )
        self.button_generate_csv_file.grid(
            row=9,
            column=1,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )

        self.button_close = ctk.CTkButton(buttons_frame, text="Fechar", font=self.font)
        self.button_close.grid(
            row=10,
            column=0,
            padx=self.x_pad,
            pady=self.y_pad_button,
            sticky="nsew",
        )
