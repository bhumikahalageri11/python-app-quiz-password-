import tkinter as tk
from tkinter import messagebox
import random
import string

# -----------------------------
# Password Generator Function
# -----------------------------
def generate_password():
    name = name_entry.get().strip()

    if name == "":
        messagebox.showerror("Error", "Please enter your name.")
        return

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}<>?/"

    all_characters = uppercase + lowercase + numbers + symbols

    # Randomly include up to 3 characters from the user's name
    name_part = ''.join(random.sample(name, min(len(name), 3)))

    password = []

    # Ensure password strength
    password.append(random.choice(uppercase))
    password.append(random.choice(lowercase))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))

    # Add name characters
    password.extend(name_part)

    # Fill remaining characters
    while len(password) < 12:
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, final_password)
    password_entry.config(state="readonly")


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("500x300")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Strong Password Generator",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

name_label = tk.Label(root, text="Enter Your Name", font=("Arial", 12))
name_label.pack()

name_entry = tk.Entry(root, width=35, font=("Arial", 12))
name_entry.pack(pady=8)

generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=generate_password
)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password", font=("Arial", 12))
password_label.pack()

password_entry = tk.Entry(
    root,
    width=35,
    font=("Consolas", 14),
    justify="center",
    state="readonly"
)
password_entry.pack(pady=10)

copy_button = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    width=18,
    command=copy_password
)
copy_button.pack(pady=10)

root.mainloop()