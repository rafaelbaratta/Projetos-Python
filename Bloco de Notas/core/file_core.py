import os
import subprocess as sp
import sys
from tkinter import messagebox

import customtkinter as ctk

from utils import Options


class FileCore:
    def __init__(self, gui):
        self.gui = gui
        self.opt = Options(gui)
        self.current_file = None

    def window_name(self, path, name):
        self.current_file = path
        self.gui.title(f"Bloco de Notas - {name}")

    def new_file(self):
        if not self.ask_for_save_if_needed():
            return

        self.window_name(None, "Sem Título")
        self.gui.text.delete("1.0", "end")

    def new_window(self):
        sp.Popen([sys.executable, "app.py"])

    def open_file(self):
        if not self.ask_for_save_if_needed():
            return

        file_path = ctk.filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")]
        )

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.gui.text.delete("1.0", "end")
                    self.gui.text.insert("1.0", file.read())

                self.window_name(file_path, file_path.split("/")[-1])
            except:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(self.gui.text.get("1.0", "end-1c"))
        else:
            self.save_as()

    def save_as(self):
        file_path = ctk.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
        )

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.gui.text.get("1.0", "end-1c"))
            self.window_name(file_path, file_path.split("/")[-1])

    def close_file(self):
        if not self.ask_for_save_if_needed():
            return

        self.gui.destroy()

    def not_saved_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "r", encoding="utf-8") as file:
                    return self.gui.text.get("1.0", "end-1c") != file.read()
            except:
                return True
        else:
            return len(self.gui.text.get("1.0", "end-1c")) > 0

    def ask_for_save_if_needed(self):
        if self.not_saved_file():
            confirm = self.opt.ask_for_save()
            if confirm is None:
                return False
            elif confirm:
                self.save_file()
            return True
        else:
            return True

    def print_file(self):
        if not self.ask_for_save_if_needed():
            return

        if not self.current_file:
            messagebox.showinfo("Info", "Selecione um arquivo para impressão")
            return

        if sys.platform == "win32":
            os.startfile(self.current_file, "print")
        elif sys.platform == "darwin":
            sp.run(["lpr", self.current_file])
        else:
            sp.run(["lp", self.current_file])
