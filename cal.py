import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        # Initialize the display
        self.display = tk.Entry(self.root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        self.create_buttons()

    def create_buttons(self):
        # Button definitions (row, column, button text)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2)
        ]

        # Create each button and add it to the grid
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == 'C':
            # Clear the display
            self.display.delete(0, tk.END)
        elif button_text == '=':
            # Evaluate the expression
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            # Add button text to the display
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + button_text)

# Create the main window
root = tk.Tk()

# Initialize the Calculator app
calc = Calculator(root)

# Run the application
root.mainloop()
