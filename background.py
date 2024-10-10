import tkinter as tk
from PIL import Image, ImageTk  # We will use PIL for better image support

def set_background(window, image_path):
    """
    Sets the background of the given Tkinter window to the specified image.

    :param window: The Tkinter window to set the background for.
    :param image_path: The path to the background image.
    """
    # Load the background image
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((700, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label to hold the image and place it on the window
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set as background
