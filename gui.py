import tkinter as tk
from tkinter import messagebox, font
from authentication import register_user, login_user

# Define window-specific font inside the function
def create_new_user_window(root):
    new_user_win = tk.Toplevel(root)
    new_user_win.title("New User Registration")
    new_user_win.geometry("700x600")

    # Initialize font after window creation
    default_font = font.Font(family="Helvetica", size=16)

    # Label and Entry for Email
    tk.Label(new_user_win, text="Enter your email address:", font=default_font).place(x=200, y=150)
    email_entry = tk.Entry(new_user_win, width=40, font=default_font)
    email_entry.place(x=200, y=180)

    # Label and Entry for Password
    tk.Label(new_user_win, text="Enter your password:", font=default_font).place(x=200, y=220)
    password_entry = tk.Entry(new_user_win, show='*', width=40, font=default_font)
    password_entry.place(x=200, y=250)

    # Register Button
    def register():
        email = email_entry.get()
        password = password_entry.get()
        register_user(email, password)

    tk.Button(new_user_win, text="Register", command=register, font=default_font, width=15, height=2).place(x=250, y=300)

def create_existing_user_window(root):
    existing_user_win = tk.Toplevel(root)
    existing_user_win.title("Existing User Login")
    existing_user_win.geometry("700x600")

    # Initialize font after window creation
    default_font = font.Font(family="Helvetica", size=16)

    tk.Label(existing_user_win, text="Enter your email address:", font=default_font).place(x=200, y=150)
    email_entry = tk.Entry(existing_user_win, width=40, font=default_font)
    email_entry.place(x=200, y=180)

    tk.Label(existing_user_win, text="Enter your password:", font=default_font).place(x=200, y=220)
    password_entry = tk.Entry(existing_user_win, show='*', width=40, font=default_font)
    password_entry.place(x=200, y=250)

    def login():
        email = email_entry.get()
        password = password_entry.get()
        login_user(email, password)

    tk.Button(existing_user_win, text="Login", command=login, font=default_font, width=15, height=2).place(x=250, y=300)
