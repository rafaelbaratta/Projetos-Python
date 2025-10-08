import tkinter as tk

class Gui():
    x_pad = 5
    y_pad = 3
    width_entry = 30

    window = tk.Tk()
    window.wm_title("CRUD de Clientes em Python com SQLite")

    text_firstname = tk.StringVar()
    text_lastname = tk.StringVar()
    text_email = tk.StringVar()
    text_cpf = tk.StringVar()
    text_phone = tk.StringVar()

    label_firstname = tk.Label(window, text = "Nome:")
    label_lastname = tk.Label(window, text = "Sobrenome:")
    label_email = tk.Label(window, text = "E-mail:")
    label_cpf = tk.Label(window, text = "CPF:")
    label_phone = tk.Label(window, text = "Telefone:")

    entry_firstname = tk.Entry(window, textvariable = text_firstname, width = width_entry)
    entry_lastname = tk.Entry(window, textvariable = text_lastname, width = width_entry)
    entry_email = tk.Entry(window, textvariable = text_email, width = width_entry)
    entry_cpf = tk.Entry(window, textvariable = text_cpf, width = width_entry)
    entry_phone = tk.Entry(window, textvariable = text_phone, width = width_entry)

    list_clients = tk.Listbox(window, width=100)
    scroll_clients = tk.Scrollbar(window)

    button_clear = tk.Button(window, text = "Limpar")
    button_view_all = tk.Button(window, text = "Ver todos")
    button_search = tk.Button(window, text = "Buscar")
    button_insert = tk.Button(window, text = "Inserir")
    button_update = tk.Button(window, text = "Atualizar")
    button_delete = tk.Button(window, text = "Excluir")
    button_delete_all = tk.Button(window, text = "Excluir Tudo")
    button_close = tk.Button(window, text = "Fechar")

    label_firstname.grid(row = 0, column = 0)
    label_lastname.grid(row = 1, column = 0)
    label_email.grid(row = 2, column = 0)
    label_cpf.grid(row = 3, column = 0)
    label_phone.grid(row = 4, column = 0)

    entry_firstname.grid(row = 0, column = 1, padx = 50, pady = 50)
    entry_lastname.grid(row = 1, column = 1)
    entry_email.grid(row = 2, column = 1)
    entry_cpf.grid(row = 3, column = 1)
    entry_phone.grid(row = 4, column = 1)

    list_clients.grid(row = 0, column = 2, rowspan = 10)
    scroll_clients.grid(row = 0, column = 6, rowspan = 10)
    list_clients.configure(yscrollcommand = scroll_clients.set)
    scroll_clients.configure(command = list_clients.yview)

    button_clear.grid(row = 5, column = 0, columnspan = 2)
    button_view_all.grid(row = 6, column = 0, columnspan = 2)
    button_search.grid(row = 7, column = 0, columnspan = 2)
    button_insert.grid(row = 8, column = 0, columnspan = 2)
    button_update.grid(row = 9, column = 0, columnspan = 2)
    button_delete.grid(row = 10, column = 0, columnspan = 2)
    button_delete_all.grid(row = 11, column = 0, columnspan = 2)
    button_close.grid(row = 12, column = 0, columnspan = 2)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky = "WE", padx = x_pad, pady = y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(sticky = "NS", padx = 0, pady = 0)
        elif widget_class == "Scrollbar":
            child.grid_configure(sticky = "NS", padx = 0, pady = 0)
        else:
            child.grid_configure(sticky = 'N', padx = x_pad, pady = y_pad)

    def run(self):
        self.window.mainloop()

