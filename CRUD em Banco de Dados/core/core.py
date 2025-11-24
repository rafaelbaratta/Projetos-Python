from tkinter import messagebox

from customtkinter import filedialog

from utils import InputValidations as val

from .database import Database as db


class Core:
    selected = None

    @staticmethod
    def clear_fields(entries):
        for entry in entries.values():
            entry.delete(0, "end")

    @staticmethod
    def clear_selection(listbox):
        Core.selected = None
        listbox.selection_clear(0, "end")

    @staticmethod
    def insert_command(listbox, entries):
        if val.valid_inputs(entries):
            db.insert(
                entries["firstname"].get(),
                entries["lastname"].get(),
                entries["email"].get(),
                entries["cpf"].get(),
                entries["phone"].get(),
            )

            Core.search_all_command(listbox)
            Core.clear_fields(entries)

    @staticmethod
    def search_all_command(listbox):
        rows = db.view_all()
        listbox.delete(0, "end")

        for row in rows:
            listbox.insert("end", " - ".join(map(str, row)))

    @staticmethod
    def search_command(listbox, entries):
        listbox.delete(0, "end")
        rows = db.search(
            entries["firstname"].get(),
            entries["lastname"].get(),
            entries["email"].get(),
            entries["cpf"].get(),
            entries["phone"].get(),
        )

        for row in rows:
            listbox.insert("end", " - ".join(map(str, row)))

    @staticmethod
    def update_command(listbox, entries):
        if Core.selected:
            if val.valid_inputs(entries):
                db.update(
                    Core.selected[0],
                    entries["firstname"].get(),
                    entries["lastname"].get(),
                    entries["email"].get(),
                    entries["cpf"].get(),
                    entries["phone"].get(),
                )
                Core.search_all_command(listbox)
                Core.clear_fields(entries)
        else:
            messagebox.showwarning("Aviso!", "Selecione algum cliente para atualizar!")
        Core.selected = None

    @staticmethod
    def get_selected_row(event, listbox, entries):
        try:
            if not listbox.curselection():
                return

            index = listbox.curselection()[0]
            Core.selected = listbox.get(index)
            Core.selected = Core.selected.split(" - ")

            Core.clear_fields(entries)
            for i, entry in enumerate(entries.values()):
                entry.insert("end", Core.selected[i + 1])

        except IndexError:
            Core.selected = None

        return Core.selected

    @staticmethod
    def delete_command(listbox, entries):
        Core.selected
        if Core.selected:
            confirm = messagebox.askyesno(
                "Confirmar?",
                f"Deseja realmente excluir o cliente {Core.selected[1]} {Core.selected[2]}?",
            )
            if confirm:
                db.delete(Core.selected[0])
                Core.search_all_command(listbox)
                Core.clear_fields(entries)
        else:
            messagebox.showwarning("Aviso!", "Selecione algum cliente para excluir!")
        Core.selected = None

    @staticmethod
    def delete_all_command(listbox, entries):
        confirm = messagebox.askyesno(
            "Confirmar?",
            f"Deseja realmente excluir TODOS os dados do banco PERMANENTEMENTE?",
        )
        if confirm:
            db.delete_all()
            Core.search_all_command(listbox)
            Core.clear_fields(entries)

    @staticmethod
    def generate_txt_file_command(listbox):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
        )

        text = listbox.get(0, "end")

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                for line in text:
                    file.write(line + "\n")

    @staticmethod
    def generate_csv_file_command(listbox):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")],
        )

        text = listbox.get(0, "end")

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                for line in text:
                    file.write((",").join(line.split(" - ")) + "\n")
