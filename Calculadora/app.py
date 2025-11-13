import customtkinter as ctk

class MainApp(ctk.CTk):
    
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        self.numbers = [str(i) for i in range(10)]
        self.signals = ['(', ')', '.']

        self.last_was_operator = False
        self.last_was_number = False
        self.last_was_signal = False

        self.last_character = ''
        self.MAX_CHARACTERS = 28

        buttons = [
            ['C', '←', '.', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['(', '0', ')', '=']
        ]

        super().__init__()
        self.build(buttons)

    def is_system_dark(self):
        if ctk.get_appearance_mode() == "Dark":
            buttons_colors = [
                ["dark red", "dark red", "gray25", "dark blue"],
                ["gray17", "gray17", "gray17", "dark blue"],
                ["gray17", "gray17", "gray17", "dark blue"],
                ["gray17", "gray17", "gray17", "dark blue"],
                ["gray25", "gray17", "gray25", "dark green"]
            ]

            text_color = "light gray"
        else:
            buttons_colors = [
                ["light salmon", "light salmon", "light gray", "light blue"],
                ["white", "white", "white", "light blue"],
                ["white", "white", "white", "light blue"],
                ["white", "white", "white", "light blue"],
                ["light gray", "white", "light gray", "light green"]
            ]

            text_color = "dim gray"
        
        return buttons_colors, text_color

    def build(self, buttons):
        self.title("Calculadora")
        self.geometry("400x450")
        self.minsize(width=250, height=300)
        self.iconbitmap("images/calculator.ico")
        self._set_appearance_mode("System")

        buttons_colors, text_color = self.is_system_dark()

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

        self.solution = ctk.CTkEntry(self, height=50, font=("Arial", 24))
        self.solution.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        for i, row in enumerate(buttons):
            for j, char in enumerate(row):
                if char == '=':
                    button = ctk.CTkButton(self, text=char, width=80, height=60, fg_color=buttons_colors[i][j], text_color=text_color, font=("Arial", 20), command=lambda: self.on_solution_calculate())
                else:
                    button = ctk.CTkButton(self, text=char, width=80, height=60, fg_color=buttons_colors[i][j], text_color=text_color, font=("Arial", 20), command=lambda ch=char: self.on_button_click(ch))
                button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
                
        self.solution.bind("<Key>", self.on_key_press)

        self.mainloop()
        
    def clear_solution(self, position=None):

        if position is None:
            self.solution.delete(0, ctk.END)

            self.last_was_operator = False
            self.last_was_number = False
            self.last_was_signal = False
            self.last_character = ''

        else:
            if position >= 0:
                self.solution.delete(position, ctk.END)

                if self.solution.get():
                    self.last_character = self.solution.get()[-1]
                    self.last_was_operator = self.last_character in self.operators
                    self.last_was_number = self.last_character in self.numbers
                    self.last_was_signal = self.last_character in self.signals
                else:
                    self.last_was_operator = False
                    self.last_was_number = False
                    self.last_was_signal = False
                    self.last_character = ''

    def parenthesis_counter(self, text):
        return text.count('('), text.count(')')

    def cannot_be_number_zero(self):
        return self.last_was_number and self.last_character == '0' and (self.solution.get() == '0' or self.solution.get()[-2] in self.operators + ['('])
    
    def cannot_be_number(self):
        if not self.solution.get():
            return False
        
        cannot_be_zero = False
        if self.last_character == '0':
            cannot_be_zero = self.cannot_be_number_zero()
        
        return (self.last_was_signal and self.last_character == ')') or cannot_be_zero
    
    def cannot_be_operator(self):
        return (self.last_was_operator or self.last_character == '') or (self.last_was_signal and self.last_character == '(') or self.last_character == '.'
    
    def cannot_be_signal(self, char):
        if char == '(':
            return self.last_was_number or (self.last_was_signal and self.last_character == ')')
        elif char == ')':
            right_parentheses, left_parentheses = self.parenthesis_counter(self.solution.get())
            return (self.last_was_operator or self.last_character == '') or (self.last_was_signal and self.last_character == '(') or right_parentheses <= left_parentheses
        elif char == '.':
            for i in range(len(self.solution.get())-1, -1, -1):
                if self.solution.get()[i] in self.operators + ['(']:
                    break
                if self.solution.get()[i] == '.':
                    return True
            return self.last_was_operator or self.last_character == '' or self.last_was_signal
    
    def on_key_press(self, event):
        if event.char == '\x03':
            self.clipboard_clear()
            self.clipboard_append(self.solution.get())
            return "break"
        elif event.char == '\x16':
            clipboard_content = self.clipboard_get()
            if clipboard_content:
                self.clear_solution()
                for char in clipboard_content:
                    self.on_button_click(char)
            return "break"
    
        if event.char == '\r':
            self.on_solution_calculate()
        elif event.char == ',':
            self.on_button_click('.')
        elif event.char == '\x08':
            self.on_button_click('←')
        elif event.char == '\x1b' or event.char == '\x7f':
            self.on_button_click('C')
        else:
            self.on_button_click(event.char)
        return "break"

    def on_button_click(self, char):
        if char == 'C':
            self.clear_solution()
        elif char == '←':
            self.clear_solution(self.solution.index(ctk.END)-1)
        else:
            if len(self.solution.get()) == self.MAX_CHARACTERS:
                return
            elif char in self.numbers:
                if self.cannot_be_number():
                    return
            elif char in self.operators:
                if self.cannot_be_operator():
                    return
            elif char in self.signals:
                if self.cannot_be_signal(char):
                    return
            else:
                return
                    
            self.solution.insert(ctk.END, char)

            self.last_was_operator = False
            self.last_was_number = False
            self.last_was_signal = False

            self.last_character = char

            if char in self.operators:
                self.last_was_operator = True
            elif char in self.numbers:
                self.last_was_number = True
            elif char in self.signals:
                self.last_was_signal = True

    def on_solution_calculate(self):
        expression = self.solution.get()
        rigth_parentheses, left_parentheses = self.parenthesis_counter(expression)

        if rigth_parentheses != left_parentheses:
            return
        elif self.last_was_operator:
            return

        self.solution.delete(0, ctk.END)

        try:
            result = str(eval(expression))
            self.solution.insert(0, result)
        except ZeroDivisionError:
            self.solution.insert(0, "Error: Division by zero")
        except:
            return

if __name__ == "__main__":
    app = MainApp()
