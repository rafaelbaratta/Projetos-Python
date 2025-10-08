from tkinter import END
from tkinter import messagebox
from frontend import Gui
from validations import InputValidations
import backend as core

app = None
selected = None

def view_all_command():
    rows = core.view_all()
    app.list_clients.delete(0, END)

    for r in rows:
        app.list_clients.insert(END, r)

def search_command():
    app.list_clients.delete(0, END)
    rows = core.search(app.text_firstname.get(), app.text_lastname.get(), app.text_email.get(), app.text_cpf.get(), app.text_phone.get())

    for r in rows:
        app.list_clients.insert(END, r)
    
def insert_command():
    if valid.valid_inputs():
        core.insert(app.text_firstname.get(), app.text_lastname.get(), app.text_email.get(), app.text_cpf.get(), app.text_phone.get())
        view_all_command()
        clean_fields()

def update_command():
    global selected
    if selected:
        if valid.valid_inputs():
            core.update(selected[0], app.text_firstname.get(), app.text_lastname.get(), app.text_email.get(), app.text_cpf.get(), app.text_phone.get())
            view_all_command()
            clean_fields()
    else:
        messagebox.showwarning("Aviso!", "Selecione algum cliente para atualizar!")
    selected = None

def delete_command():
    global selected
    if selected:
        confirm = messagebox.askyesno("Confirmar?", f"Deseja realmente excluir o cliente {selected[1]} {selected[2]}?")
        if confirm:
            core.delete(selected[0])
            view_all_command()
            clean_fields()
    else:
        messagebox.showwarning("Aviso!", "Selecione algum cliente para excluir!")
    selected = None

def delete_all_command():
    confirm = messagebox.askyesno("Confirmar?", f"Deseja realmente excluir TODOS os dados do banco PERMANENTEMENTE?")
    if confirm:
        core.delete_all()
        view_all_command()
        clean_fields()

def clean_fields():
    app.entry_firstname.delete(0, END)
    app.entry_lastname.delete(0, END)
    app.entry_email.delete(0, END)
    app.entry_cpf.delete(0, END)
    app.entry_phone.delete(0, END)

def get_selected_row(event):
    global selected
    
    try:
        if not app.list_clients.curselection():
            return
        
        index = app.list_clients.curselection()[0]
        selected = app.list_clients.get(index)

        clean_fields()
        app.entry_firstname.insert(END, selected[1])
        app.entry_lastname.insert(END, selected[2])
        app.entry_email.insert(END, selected[3])
        app.entry_cpf.insert(END, selected[4])
        app.entry_phone.insert(END, selected[5])
    except IndexError:
        selected = None

    return selected

if __name__ == "__main__":
    app = Gui()
    valid = InputValidations()
    app.list_clients.bind("<<ListboxSelect>>", get_selected_row)

    app.button_clear.configure(command = clean_fields)
    app.button_view_all.configure(command = view_all_command)
    app.button_search.configure(command = search_command)
    app.button_insert.configure(command = insert_command)
    app.button_update.configure(command = update_command)
    app.button_delete.configure(command = delete_command)
    app.button_delete_all.configure(command = delete_all_command)
    app.button_close.configure(command = app.window.destroy)

    app.run()
