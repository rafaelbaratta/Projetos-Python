from core import EditCore, FileCore, OptionsCore
from screen import Gui
from utils import InitialConfigurations


class MainApp:
    def __init__(self):
        self.gui = Gui()
        self.file = FileCore(self.gui)
        self.edit = EditCore(self.gui)
        self.options = OptionsCore(self.gui)
        self.configurations = InitialConfigurations()

        self.gui.after(100, self.apply_initial_configurations)

    def apply_initial_configurations(self):
        self.configurations.functions_configuration(
            self.gui, self.file, self.edit, self.options
        )
        self.configurations.keys_functions(self.gui, self.file, self.edit, self.options)
        self.gui.protocol("WM_DELETE_WINDOW", self.file.close_file)


if __name__ == "__main__":
    app = MainApp()
    app.gui.mainloop()
