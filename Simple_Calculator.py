import tkinter as tk

def on_button_click(value):
    current_value = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current_value) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def perform_calculation():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying and entering numbers
entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, command=clear_entry)
    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, command=perform_calculation)
        root.bind('<Return>', lambda event=None: perform_calculation())
    else:
        button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col)

# Event loop
root.mainloop()
