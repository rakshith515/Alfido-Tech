import random
import string
from tkinter import *
from tkinter import ttk

def generate_password(length=8):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(random.choice(alphabet) for _ in range(length))
    while not (any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)):
        password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

def generate_password_gui():
    root = Tk()
    root.title("Password Generator")

    # Create a label for the password length
    label_length = ttk.Label(root, text="Password Length")
    label_length.grid(row=0, column=0, padx=5, pady=5)

    # Create an entry for the password length
    entry_length = ttk.Entry(root)
    entry_length.grid(row=0, column=1, padx=5, pady=5)

    # Create a button to generate the password
    button_generate = ttk.Button(root, text="Generate Password", command=lambda: generate_password_with_length(int(entry_length.get())))
    button_generate.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # Create a variable to store the generated password
    password_var = StringVar()

    # Create a label to display the generated password
    label_password = ttk.Label(root, textvariable=password_var)
    label_password.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def generate_password_with_length(length):
        password = generate_password(length)
        password_var.set(password)

    root.mainloop()

if __name__ == "__main__":
    generate_password_gui()
