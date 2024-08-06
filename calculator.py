import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the text entry box
def update_expression(value):
    current_text = expression_entry.get()
    new_text = current_text + str(value)
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, new_text)

# Function to evaluate the final expression
def evaluate_expression():
    try:
        current_text = expression_entry.get()
        result = str(eval(current_text))
        expression_entry.delete(0, tk.END)
        expression_entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to clear the text entry box
def clear_expression():
    expression_entry.delete(0, tk.END)

# Setting up the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the expression
expression_entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 18))
expression_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating buttons for the calculator
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for text in button_texts:
    if text == '=':
        button = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 18),
                           command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 18),
                           command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

# Adding a clear button
clear_button = tk.Button(root, text='C', padx=30, pady=20, font=('Arial', 18),
                         command=clear_expression)
clear_button.grid(row=row, column=0, columnspan=4, sticky="nsew")

# Configuring row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Running the main loop
root.mainloop()
