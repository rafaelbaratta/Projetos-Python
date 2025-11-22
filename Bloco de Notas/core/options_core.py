from tkinter import messagebox

import customtkinter as ctk

from utils import Options


class OptionsCore:
    last_found_position = "1.0"

    def __init__(self, gui):
        self.gui = gui
        self.opt = Options(gui)

    def configure_font(self):
        self.opt.font_configurator(
            self.gui.font_family.get(),
            self.gui.font_size.get(),
            self.gui.font_weight.get(),
            self.gui.font_slant.get(),
        )

        self.font_option_configuration()

    def apply_font_changes(self):
        family = self.opt.selected_family.get()
        size = int(self.opt.selected_size.get())
        weight = self.opt.selected_weight.get()
        slant = self.opt.selected_slant.get()

        self.gui.font_family.set(family)
        self.gui.font_size.set(size)
        self.gui.font_weight.set(weight)
        self.gui.font_slant.set(slant)

        self.text_font = ctk.CTkFont(
            family=family, size=size, weight=weight, slant=slant
        )

        self.gui.text.configure(font=self.text_font)

        if hasattr(self.opt, "font_window"):
            self.opt.font_window.destroy()

    def font_option_configuration(self):
        self.opt.apply_font.configure(command=self.apply_font_changes)

    def execute_find_text(self):
        text_to_find = self.opt.find_entry.get()

        if not text_to_find:
            messagebox.showinfo(
                "Campo vazio", "Informe o que deseja encontrar no texto!"
            )
            return

        start_position = f"{self.last_found_position}+1c"

        position = self.gui.text.search(text_to_find, start_position, "end")

        if not position:
            position = self.gui.text.search(text_to_find, "1.0", "end")
            if not position:
                messagebox.showinfo("Info", "Texto não encontrado no bloco de notas")
                return

        end_position = f"{position}+{len(text_to_find)}c"

        self.gui.text.tag_remove("sel", "1.0", "end")
        self.gui.text.tag_add("sel", position, end_position)

        self.last_found_position = position

        self.gui.text.mark_set("insert", position)
        self.gui.text.see(position)

    def find_text(self):
        self.opt.find_text_screen()
        self.find_option_configuration()

    def find_option_configuration(self):
        self.opt.find_button.configure(command=self.execute_find_text)

    def execute_replace_text(self):
        text_to_be_replaced = self.opt.find_to_replace_entry.get()
        text_to_replace = self.opt.replace_entry.get()

        if not text_to_be_replaced:
            messagebox.showinfo(
                "Campo vazio", "Informe o que deseja encontrar no texto!"
            )
            return

        position = self.gui.text.search(text_to_be_replaced, "1.0", "end")

        if not position:
            messagebox.showinfo("Info", "Texto não encontrado no bloco de notas")
            return

        end_position = f"{position}+{len(text_to_be_replaced)}c"

        self.gui.text.tag_remove("sel", "1.0", "end")
        self.gui.text.tag_add("sel", position, end_position)

        try:
            selected_area = self.gui.text.get("sel.first", "sel.last")
            if selected_area:
                self.gui.text.delete("sel.first", "sel.last")
                self.gui.text.insert(position, text_to_replace)
        except:
            return

    def execute_replace_all_text(self):
        text_to_be_replaced = self.opt.find_to_replace_entry.get()
        text_to_replace = self.opt.replace_entry.get()

        if not text_to_be_replaced:
            messagebox.showinfo(
                "Campo vazio", "Informe o que deseja encontrar no texto!"
            )
            return

        position = self.gui.text.search(text_to_be_replaced, "1.0", "end")

        if not position:
            messagebox.showinfo("Info", "Texto não encontrado no bloco de notas")
            return

        while position:

            end_position = f"{position}+{len(text_to_be_replaced)}c"

            self.gui.text.delete(position, end_position)
            self.gui.text.insert(position, text_to_replace)

            last_position = f"{position}+{len(text_to_replace)}c"
            position = self.gui.text.search(text_to_be_replaced, last_position, "end")

        messagebox.showinfo("Info", "Todas as ocorrências foram substituídas")

    def replace_text(self):
        self.opt.replace_text_screen()
        self.replace_option_configuration()

    def replace_option_configuration(self):
        self.opt.replace_button.configure(command=self.execute_replace_text)
        self.opt.replace_all_button.configure(command=self.execute_replace_all_text)
