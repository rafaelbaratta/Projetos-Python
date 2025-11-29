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

    @staticmethod
    def calculate_bill(bill_code):
        digits = [int(d) for d in bill_code]
        n = len(digits)

        weighted_sum = sum((i + 1) * digit for i, digit in enumerate(digits))

        prime_positions = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        prime_product = 1
        for pos in prime_positions:
            if pos < n:
                prime_product *= digits[pos] + 1

        alternating_sum = sum(
            digit if i % 2 == 0 else -digit for i, digit in enumerate(digits)
        )

        last_four = int(bill_code[-4:])

        valor = (
            (weighted_sum % 5000)
            + (prime_product % 3000)
            + (abs(alternating_sum) % 1000)
            + (last_four % 1000)
        ) / 10.0

        return valor
