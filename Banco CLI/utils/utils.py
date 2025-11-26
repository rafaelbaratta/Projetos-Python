import os


class Utils:

    @staticmethod
    def clean_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def pause():
        input("\nPressione ENTER para continuar...")
