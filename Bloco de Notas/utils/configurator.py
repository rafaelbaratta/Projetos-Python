class InitialConfigurations:

    @staticmethod
    def functions_configuration(gui, file, edit, options):
        gui.menu_file.entryconfig(0, command=file.new_file)
        gui.menu_file.entryconfig(1, command=file.new_window)
        gui.menu_file.entryconfig(2, command=file.open_file)
        gui.menu_file.entryconfig(4, command=file.save_file)
        gui.menu_file.entryconfig(5, command=file.save_as)
        gui.menu_file.entryconfig(7, command=file.print_file)
        gui.menu_file.entryconfig(9, command=file.close_file)

        gui.menu_edit.entryconfig(0, command=edit.undo)
        gui.menu_edit.entryconfig(1, command=edit.redo)
        gui.menu_edit.entryconfig(3, command=edit.cut)
        gui.menu_edit.entryconfig(4, command=edit.copy)
        gui.menu_edit.entryconfig(5, command=edit.paste)
        gui.menu_edit.entryconfig(6, command=edit.remove)
        gui.menu_edit.entryconfig(8, command=edit.select_all_content)
        gui.menu_edit.entryconfig(9, command=edit.delete_all_content)

        gui.menu_options.entryconfig(0, command=options.configure_font)
        gui.menu_options.entryconfig(2, command=options.find_text)
        gui.menu_options.entryconfig(3, command=options.replace_text)

    @staticmethod
    def keys_functions(gui, file, edit, options):
        gui.bind("<Control-w>", lambda event: file.new_window())
        gui.bind("<Control-n>", lambda event: file.new_file())
        gui.bind("<Control-o>", lambda event: file.open_file())
        gui.bind("<Control-s>", lambda event: file.save_file())
        gui.bind("<Control-Shift-S>", lambda event: file.save_as())
        gui.bind("<Control-BackSpace>", lambda event: file.close_file())

        gui.bind("<Control-r>", lambda event: edit.remove())
        gui.bind("<Control-Delete>", lambda event: edit.delete_all_content())

        gui.bind("<Control-t>", lambda event: options.configure_font())
        gui.bind("<Control-f>", lambda event: options.find_text())
        gui.bind("<Control-h>", lambda event: options.replace_text())
