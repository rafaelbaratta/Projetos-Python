import os


class Utils:

    HEADER = (
        f"{'=' * 50}\n"
        f"== {f' AGÊNCIA BANCÁRIA '.center(44, '-')} ==\n"
        f"{'=' * 50}\n"
    )

    @staticmethod
    def print_header(screen):
        Utils.clean_screen()
        print(Utils.HEADER)
        print(f" < {f' {screen} '.center(44, '-')} > \n")

    @staticmethod
    def clean_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def pause():
        input("\nPressione ENTER para continuar...")
