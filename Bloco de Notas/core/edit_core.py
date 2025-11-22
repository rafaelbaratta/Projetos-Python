from utils import Options


class EditCore:
    def __init__(self, gui):
        self.gui = gui
        self.opt = Options(gui)

    def undo(self):
        try:
            self.gui.text.edit_undo()
        except:
            return

    def redo(self):
        try:
            self.gui.text.edit_redo()
        except:
            return

    def cut(self):
        try:
            selected_area = self.gui.text.get("sel.first", "sel.last")
            if selected_area:
                self.gui.clipboard_clear()
                self.gui.clipboard_append(selected_area)
                self.gui.text.delete("sel.first", "sel.last")
        except:
            return

    def copy(self):
        try:
            selected_area = self.gui.text.get("sel.first", "sel.last")
            if selected_area:
                self.gui.clipboard_clear()
                self.gui.clipboard_append(selected_area)
        except:
            return

    def paste(self):
        try:
            selected_area = self.gui.text.get("sel.first", "sel.last")
            if selected_area:
                self.gui.text.delete("sel.first", "sel.last")
        except:
            pass

        try:
            self.gui.text.insert("insert", self.gui.clipboard_get())
        except:
            return

    def remove(self):
        try:
            selected_area = self.gui.text.get("sel.first", "sel.last")
            if selected_area:
                self.gui.text.delete("sel.first", "sel.last")
        except:
            return

    def select_all_content(self):
        self.gui.text.focus()
        self.gui.text.tag_add("sel", "1.0", "end")

    def delete_all_content(self):
        self.gui.text.focus()
        self.gui.text.delete("1.0", "end")
