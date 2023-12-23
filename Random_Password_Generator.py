import tkinter as tk
from tkinter import messagebox
import secrets
import string

def crt_random_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True, special_chars="!@#$%^&*()_-+=<>?/"):
    character_set = ""
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_digits:
        character_set += string.digits
    if use_special_chars:
        character_set += special_chars

    if not character_set:
        raise ValueError("Please select at least one character type.")

    generated_password = ''.join(secrets.choice(character_set) for _ in range(length))
    return generated_password

def gen_random_password():
    try:
        password_length = int(length_var.get())
        include_lowercase = use_lowercase_var.get()
        include_uppercase = use_uppercase_var.get()
        include_digits = use_digits_var.get()
        include_special_chars = use_special_chars_var.get()
        special_characters = special_chars_var.get() if include_special_chars else ""

        special_chars_entry.config(state="normal" if include_special_chars else "disabled")

        password = crt_random_password(password_length, include_lowercase, include_uppercase, include_digits, include_special_chars, special_characters)
        messagebox.showinfo("Generated Password", f"Secure Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Variables
length_var = tk.StringVar(value="12")
use_lowercase_var = tk.BooleanVar(value=True)
use_uppercase_var = tk.BooleanVar(value=True)
use_digits_var = tk.BooleanVar(value=True)
use_special_chars_var = tk.BooleanVar(value=True)
special_chars_var = tk.StringVar(value='!@#$%^&*()_-+=<>?/')

# Labels
tk.Label(root, text="Desired Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Include Character Types:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Custom Special Characters:").grid(row=2, column=0, sticky="w", padx=10, pady=5)

# Entry for Password Length
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Checkbuttons for Character Types
tk.Checkbutton(root, text="Lowercase", variable=use_lowercase_var).grid(row=1, column=1, sticky="w", padx=10)
tk.Checkbutton(root, text="Uppercase", variable=use_uppercase_var).grid(row=1, column=1, sticky="e", padx=10)
tk.Checkbutton(root, text="Digits", variable=use_digits_var).grid(row=1, column=2, sticky="w", padx=10)
tk.Checkbutton(root, text="Special Characters", variable=use_special_chars_var).grid(row=1, column=2, sticky="e", padx=10)

# Entry for Special Characters
special_chars_entry = tk.Entry(root, textvariable=special_chars_var, state="disabled")
special_chars_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Random Password", command=gen_random_password)
generate_button.grid(row=3, column=0, columnspan=3, pady=10)

# Run the main event loop
root.mainloop()
