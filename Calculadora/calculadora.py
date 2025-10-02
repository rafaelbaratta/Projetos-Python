from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.operators = ['/', '*', '+', '-']
        self.signals = ['(', ')', '.']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.last_was_operator = None
        self.last_was_number = None
        self.last_character = None
        self.last_button = None
        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(multiline = False,
                                  readonly = True,
                                  halign = "right",
                                  font_size = 30)
        main_layout.add_widget(self.solution)

        buttons = [
            ['C', '<-', '.', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['(', '0', ')', '=']
        ]

        for row in buttons:
            horizontal_layout = BoxLayout()
            for label in row:
                button = Button(text = label,
                                pos_hint = {"center_x": 0.5, "center_y": 0.5})

                if label in self.numbers:
                    button.background_color = (1, 1, 1, 1)
                elif label in self.operators:
                    button.background_color = (0, 0, 1, 1)
                elif label in ['C', '<-']:
                    button.background_color = (1, 0, 0, 1)
                elif label == '=':
                    button.background_color = (0, 1, 0, 1)
                else:
                    button.background_color = (0.8, 0.8, 0.8, 1)

                if label == '=':
                    button.bind(on_press=self.on_solution)
                else:
                    button.bind(on_press=self.on_button_press)
                horizontal_layout.add_widget(button)
            main_layout.add_widget(horizontal_layout)
        
        return main_layout

    def parenthesis_counter(self, text):        
        return text.count('('), text.count(')')
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ''
            self.last_character = None
        elif button_text == '<-':
            x = len(self.solution.text)
            self.solution.text = self.solution.text[:-1]
            if self.solution.text:
                self.last_character = self.solution.text[-1]
            else:
                self.last_character = None
        else:
            if current and (not(self.last_was_number) and self.last_character != ')' and button_text in self.operators):
                return
            elif current == '' and (button_text in self.operators or button_text in self.signals):
                return
            elif self.last_character == '.' and (button_text in self.operators or button_text in self.signals):
                return
            elif not(self.last_was_number) and button_text == '.':
                return
            elif not(self.last_was_operator) and self.last_character != '(' and (button_text == '('):
                return
            elif not(self.last_was_number) and button_text == ')':
                return
            elif (current == '' or (self.last_character in self.signals and self.last_character != '.')) and button_text == '0':
                return
            else:
                left_parenthesis, right_parenthesis = self.parenthesis_counter(current)                
                
                if button_text == ')' and right_parenthesis >= left_parenthesis:
                    return

                new_text = current + button_text
                self.solution.text = new_text
        
        self.last_button = button_text

        if (self.last_button in self.operators) or (self.last_button in self.signals) or (self.last_button in self.numbers):
            self.last_character = self.last_button

        self.last_was_number = self.last_character in self.numbers
        self.last_was_operator = self.last_character in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        left_parenthesis, right_parenthesis = self.parenthesis_counter(text)

        if left_parenthesis != right_parenthesis:
            return
        elif self.last_was_operator:
            return
        elif text:
            try:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception:
                self.solution.text = ''


if __name__ == "__main__":
    MainApp().run()
