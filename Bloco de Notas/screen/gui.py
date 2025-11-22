import tkinter as tk

import customtkinter as ctk


class Gui(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.font_family = ctk.StringVar(value="Arial")
        self.font_size = ctk.IntVar(value=12)
        self.font_weight = ctk.StringVar(value="normal")
        self.font_slant = ctk.StringVar(value="roman")

        self.text_font = ctk.CTkFont(
            family=self.font_family.get(),
            size=self.font_size.get(),
            weight=self.font_weight.get(),
            slant=self.font_slant.get(),
        )

        self.build()

    def is_system_dark(self):
        if ctk.get_appearance_mode() == "Dark":
            self.menu_bg_color = "#2b2b2b"
            self.menu_fg_color = "#ffffff"
            self.menu_active_bg_color = "#3c3c3c"
            self.menu_active_fg_color = "#ffffff"
        else:
            self.menu_bg_color = "#eeeeee"
            self.menu_fg_color = "#000000"
            self.menu_active_bg_color = "#cccccc"
            self.menu_active_fg_color = "#000000"

    def build(self):
        self.title("Bloco de Notas - Sem Título")
        self.geometry("780x620")
        self._set_appearance_mode("System")

        self.is_system_dark()

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        for i in range(4):
            self.grid_rowconfigure(i, weight=1)

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.menu_configurator()

        self.text = ctk.CTkTextbox(
            self,
            height=50,
            width=50,
            font=self.text_font,
            undo=True,
            autoseparators=True,
        )
        self.text.grid(row=0, column=0, columnspan=4, rowspan=4, sticky="nsew")

    def menu_configurator(self):
        self.menu_file = tk.Menu(
            self.menu,
            tearoff=0,
            bg=self.menu_bg_color,
            fg=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu.add_cascade(label="Arquivo", menu=self.menu_file)
        self.menu_file_configurator()

        self.menu_edit = tk.Menu(
            self.menu,
            tearoff=0,
            bg=self.menu_bg_color,
            fg=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu.add_cascade(label="Editar", menu=self.menu_edit)
        self.menu_edit_configurator()

        self.menu_options = tk.Menu(
            self.menu,
            tearoff=0,
            bg=self.menu_bg_color,
            fg=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
            relief="flat",
            bd=0,
        )
        self.menu.add_cascade(label="Opções", menu=self.menu_options)
        self.menu_options_configurator()

    def menu_file_configurator(self):
        self.menu_file.add_command(
            label="Novo Arquivo",
            accelerator="(Ctrl + N)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_file.add_command(
            label="Nova Janela",
            accelerator="(Ctrl + W)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_file.add_command(
            label="Abrir Arquivo",
            accelerator="(Ctrl + O)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

        self.menu_file.add_separator()

        self.menu_file.add_command(
            label="Salvar Arquivo",
            accelerator="(Ctrl + S)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_file.add_command(
            label="Salvar Como",
            accelerator="(Ctrl + Shift + S)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

        self.menu_file.add_separator()

        self.menu_file.add_command(
            label="Imprimir",
            accelerator="(Ctrl + P)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

        self.menu_file.add_separator()

        self.menu_file.add_command(
            label="Fechar Arquivo",
            accelerator="(Ctrl + Backspace)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

    def menu_edit_configurator(self):
        self.menu_edit.add_command(
            label="Desfazer",
            accelerator="(Ctrl + Z)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_edit.add_command(
            label="Refazer",
            accelerator="(Ctrl + Y)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

        self.menu_edit.add_separator()

        self.menu_edit.add_command(
            label="Recortar",
            accelerator="(Ctrl + X)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_edit.add_command(
            label="Copiar",
            accelerator="(Ctrl + C)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_edit.add_command(
            label="Colar",
            accelerator="(Ctrl + V)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_edit.add_command(
            label="Excluir",
            accelerator="(Ctrl + R)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

        self.menu_edit.add_separator()

        self.menu_edit.add_command(
            label="Selecionar Tudo",
            accelerator="(Ctrl + A)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_edit.add_command(
            label="Apagar Tudo",
            accelerator="(Ctrl + Delete)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

    def menu_options_configurator(self):
        self.menu_options.add_command(
            label="Fonte",
            accelerator="(Ctrl + T)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )

        self.menu_options.add_separator()

        self.menu_options.add_command(
            label="Localizar",
            accelerator="(Ctrl + F)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
        self.menu_options.add_command(
            label="Substituir",
            accelerator="(Ctrl + H)",
            background=self.menu_bg_color,
            foreground=self.menu_fg_color,
            activebackground=self.menu_active_bg_color,
            activeforeground=self.menu_active_fg_color,
        )
