from core import Core as core
from screen import Gui


class MainApp:
    def __init__(self):
        self.gui = Gui()

        entries = {
            "firstname": self.gui.entry_firstname,
            "lastname": self.gui.entry_lastname,
            "email": self.gui.entry_email,
            "cpf": self.gui.entry_cpf,
            "phone": self.gui.entry_phone,
        }

        self.configure_buttons(entries)
        core.search_all_command(self.gui.list_clients)
        self.gui.mainloop()

    def configure_buttons(self, entries):
        self.gui.list_clients.bind(
            "<<ListboxSelect>>",
            lambda event: core.get_selected_row(event, self.gui.list_clients, entries),
        )

        self.gui.button_clear_entries.configure(
            command=lambda: core.clear_fields(entries)
        )
        self.gui.button_clear_selection.configure(
            command=lambda: core.clear_selection(self.gui.list_clients)
        )

        self.gui.button_search.configure(
            command=lambda: core.search_command(self.gui.list_clients, entries)
        )
        self.gui.button_search_all.configure(
            command=lambda: core.search_all_command(self.gui.list_clients)
        )

        self.gui.button_insert.configure(
            command=lambda: core.insert_command(self.gui.list_clients, entries)
        )
        self.gui.button_update.configure(
            command=lambda: core.update_command(self.gui.list_clients, entries)
        )

        self.gui.button_delete.configure(
            command=lambda: core.delete_command(self.gui.list_clients, entries)
        )
        self.gui.button_delete_all.configure(
            command=lambda: core.delete_all_command(self.gui.list_clients, entries)
        )

        self.gui.button_generate_txt_file.configure(
            command=lambda: core.generate_txt_file_command(self.gui.list_clients)
        )
        self.gui.button_generate_csv_file.configure(
            command=lambda: core.generate_csv_file_command(self.gui.list_clients)
        )

        self.gui.button_close.configure(command=self.gui.destroy)


if __name__ == "__main__":
    app = MainApp()
