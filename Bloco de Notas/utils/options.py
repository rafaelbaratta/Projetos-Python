from tkinter import messagebox

import customtkinter as ctk


class Options:

    def __init__(self, app):
        self.parent = app

    def ask_for_save(self):
        return messagebox.askyesnocancel(
            "Salvar?", "Deseja salvar os dados alterados no documento?", icon="question"
        )

    def font_configurator(self, family, size, weight, slant):

        self.font_window = ctk.CTkToplevel(self.parent)
        self.font_window.title("Definir o Tipo da Fonte")
        self.font_window.resizable(False, False)
        self.font_window.grab_set()

        ctk.CTkLabel(self.font_window, text="Tipo da Fonte:", font=("Arial", 14)).grid(
            row=0, column=0, padx=20, pady=10, sticky="nsew"
        )

        self.fonts = [
            "Arial",
            "Calibri",
            "Cambria",
            "Candara",
            "Comic Sans MS",
            "Consolas",
            "Constantia",
            "Corbel",
            "Courier New",
            "Ebrima",
            "Franklin Gothic",
            "Gabriola",
            "Georgia",
            "Impact",
            "Javanese Text",
            "Leelawadee UI",
            "Lucida Console",
            "Malgun Gothic",
            "Microsoft Himalaya",
            "Microsoft JhengHei",
            "Microsoft New Tai Lue",
            "Microsoft PhagsPa",
            "Microsoft Sans Serif",
            "Microsoft Tai Le",
            "Microsoft YaHei",
            "Microsoft Yi Baiti",
            "Mongolian Baiti",
            "MS Gothic",
            "MV Boli",
            "Myanmar Text",
            "Nirmala UI",
            "Palatino Linotype",
            "Segoe UI",
            "SimSun",
            "Sitka",
            "Sylfaen",
            "Symbol",
            "Tahoma",
            "Times New Roman",
            "Trebuchet MS",
            "Verdana",
            "Webdings",
            "Wingdings",
            "Yu Gothic",
        ]

        self.selected_family = ctk.StringVar(value=family)
        self.font_menu = ctk.CTkOptionMenu(
            self.font_window,
            values=self.fonts,
            variable=self.selected_family,
            dynamic_resizing=False,
        )
        self.font_menu.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            self.font_window, text="Tamanho da Fonte:", font=("Arial", 14)
        ).grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        self.selected_size = ctk.StringVar(value=size)
        self.font_menu = ctk.CTkOptionMenu(
            self.font_window,
            values=[str(x) for x in range(1, 101)],
            variable=self.selected_size,
            dynamic_resizing=False,
        )
        self.font_menu.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.selected_weight = ctk.StringVar(value=weight)
        self.font_weight = ctk.CTkCheckBox(
            self.font_window,
            text="Negrito",
            font=("Arial", 14, "bold"),
            checkbox_height=14,
            checkbox_width=14,
            border_width=2,
            corner_radius=2,
            onvalue="bold",
            offvalue="normal",
            variable=self.selected_weight,
        )
        self.font_weight.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.selected_slant = ctk.StringVar(value=slant)
        self.font_slant = ctk.CTkCheckBox(
            self.font_window,
            text="Itálico",
            font=("Arial", 14, "italic"),
            checkbox_height=14,
            checkbox_width=14,
            border_width=2,
            corner_radius=2,
            onvalue="italic",
            offvalue="roman",
            variable=self.selected_slant,
        )
        self.font_slant.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.apply_font = ctk.CTkButton(self.font_window, text="Aplicar")
        self.apply_font.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        cancel = ctk.CTkButton(
            self.font_window, text="Cancelar", command=self.font_window.destroy
        )
        cancel.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    def find_text_screen(self):

        self.find_text_window = ctk.CTkToplevel(self.parent)
        self.find_text_window.title("Localizar Texto")
        self.find_text_window.resizable(False, False)

        self.find_text_window.lift()
        self.find_text_window.focus()
        self.find_text_window.attributes("-topmost", True)

        frame = ctk.CTkFrame(self.find_text_window, fg_color="transparent")
        frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=3)

        ctk.CTkLabel(frame, text="Localizar:", font=("Arial", 14)).grid(
            row=0, column=0, pady=10, sticky="nsew"
        )

        self.find_entry = ctk.CTkEntry(frame, width=100)
        self.find_entry.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        self.find_button = ctk.CTkButton(self.find_text_window, text="Localizar")
        self.find_button.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        cancel = ctk.CTkButton(
            self.find_text_window,
            text="Cancelar",
            command=self.find_text_window.destroy,
        )
        cancel.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    def replace_text_screen(self):

        self.replace_text_window = ctk.CTkToplevel(self.parent)
        self.replace_text_window.title("Substituir Texto")
        self.replace_text_window.resizable(False, False)

        self.replace_text_window.lift()
        self.replace_text_window.focus()
        self.replace_text_window.attributes("-topmost", True)

        frame = ctk.CTkFrame(self.replace_text_window, fg_color="transparent")
        frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=3)

        ctk.CTkLabel(frame, text="Localizar:", font=("Arial", 14)).grid(
            row=0, column=0, pady=10, sticky="nsew"
        )

        self.find_to_replace_entry = ctk.CTkEntry(frame, width=100)
        self.find_to_replace_entry.grid(
            row=0, column=1, pady=10, padx=10, sticky="nsew"
        )

        ctk.CTkLabel(frame, text="Substituir:", font=("Arial", 14)).grid(
            row=1, column=0, pady=10, sticky="nsew"
        )

        self.replace_entry = ctk.CTkEntry(frame, width=100)
        self.replace_entry.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

        self.replace_button = ctk.CTkButton(self.replace_text_window, text="Substituir")
        self.replace_button.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.replace_all_button = ctk.CTkButton(
            self.replace_text_window, text="Substituir Tudo"
        )
        self.replace_all_button.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        cancel = ctk.CTkButton(
            self.replace_text_window,
            text="Cancelar",
            command=self.replace_text_window.destroy,
        )
        cancel.grid(
            row=3, column=0, rowspan=2, columnspan=2, padx=20, pady=10, sticky="nsew"
        )
