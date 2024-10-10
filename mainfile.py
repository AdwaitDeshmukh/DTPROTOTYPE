import cv2
import pytesseract
import mailsend
import graph
import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk  # We will use PIL for better image support

# Global dictionary to store user credentials (for demo purposes)
user_credentials = {}

# Function to create a background with the uploaded image
def set_background(window):
    # Load the background image
    bg_image = Image.open("bg.png")
    bg_image = bg_image.resize((700, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label to hold the image and place it on the window
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set as background

# Create the main window
root = tk.Tk()
root.title("Electricity Bill Tracker")
root.geometry("700x600")  # Set to 700 pixels wide and 600 pixels tall

# Set font for the UI
default_font = font.Font(family="Helvetica", size=16)

# Set background for the main window
set_background(root)

def register_user(email, password):
    if email in user_credentials:
        messagebox.showerror("Error", "Email already registered.")
    else:
        user_credentials[email] = password
        messagebox.showinfo("Success", "User registered successfully.")

def login_user(email, password):
    if email in user_credentials and user_credentials[email] == password:
        messagebox.showinfo("Success", "Login successful.")
        process_image(email)  # Process the image after login
    else:
        messagebox.showerror("Error", "Invalid email or password.")

def process_image(email):
    # Read and process the image
    image = cv2.imread('200kw.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    text = pytesseract.image_to_string(thresh)
    print(text)

    # Extract the number from the text
    number_str = ''.join(filter(str.isdigit, text))
    
    if number_str:
        number = int(number_str)
        
        if number >= 500:
            mailsend.email_structure("High Consumption", "500kw", email)
            messagebox.showinfo("Success", "Mail sent for high consumption.")
        else:
            mailsend.email_structure("Consumption Alert", str(number), email)
            messagebox.showinfo("Success", "Mail sent for consumption alert.")
        
        graph.plot_bar_with_thresholds(number)
    else:
        messagebox.showerror("Error", "No valid number found in the extracted text.")

def new_user_window():
    # Create a new window for registering a user
    new_user_win = tk.Toplevel(root)
    new_user_win.title("New User Registration")
    new_user_win.geometry("700x600")  # Set to 700 pixels wide and 600 pixels tall

    # Set background for the new user window
    set_background(new_user_win)

    # Label and Entry for email
    tk.Label(new_user_win, text="Enter your email address:", font=default_font, bg="#FDF5E6").place(x=150, y=100, width=400, height=40)
    email_entry = tk.Entry(new_user_win, width=40, font=default_font)
    email_entry.place(x=150, y=150, width=400, height=40)

    # Label and Entry for password
    tk.Label(new_user_win, text="Enter your password:", font=default_font, bg="#FDF5E6").place(x=150, y=200, width=400, height=40)
    password_entry = tk.Entry(new_user_win, show='*', width=40, font=default_font)
    password_entry.place(x=150, y=250, width=400, height=40)

    def register():
        email = email_entry.get()
        password = password_entry.get()
        if email in user_credentials:
            messagebox.showerror("Error", f"User with email {email} already exists!")
        else:
            register_user(email, password)

    # Register button
    tk.Button(new_user_win, text="Register", command=register, font=default_font, width=15, height=2).place(x=250, y=300, width=200, height=50)

def existing_user_window():
    # Create a new window for existing user login
    existing_user_win = tk.Toplevel(root)
    existing_user_win.title("Existing User Login")
    existing_user_win.geometry("700x600")  # Set to 700 pixels wide and 600 pixels tall

    # Set background for the existing user window
    set_background(existing_user_win)

    # Label and Entry for email
    tk.Label(existing_user_win, text="Enter your email address:", font=default_font, bg="#FDF5E6").place(x=150, y=100, width=400, height=40)
    email_entry = tk.Entry(existing_user_win, width=40, font=default_font)
    email_entry.place(x=150, y=150, width=400, height=40)

    # Label and Entry for password
    tk.Label(existing_user_win, text="Enter your password:", font=default_font, bg="#FDF5E6").place(x=150, y=200, width=400, height=40)
    password_entry = tk.Entry(existing_user_win, show='*', width=40, font=default_font)
    password_entry.place(x=150, y=250, width=400, height=40)

    def login():
        email = email_entry.get()
        password = password_entry.get()
        login_user(email, password)

    # Login button
    tk.Button(existing_user_win, text="Login", command=login, font=default_font, width=15, height=2).place(x=250, y=300, width=200, height=50)

# Main window buttons
tk.Button(root, text="New User", command=new_user_window, font=default_font, width=15, height=2).place(x=250, y=200, width=200, height=50)
tk.Button(root, text="Existing User", command=existing_user_window, font=default_font, width=15, height=2).place(x=250, y=300, width=200, height=50)

# Start the Tkinter event loop
root.mainloop()
