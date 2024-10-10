import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import prototype  # Make sure to import your prototype module

class ElectricityTrackerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Electricity Bill Tracker")
        self.root.geometry("400x300")

        # Image selection
        self.label_img = tk.Label(root, text="Select Image File:")
        self.label_img.pack(pady=5)

        self.btn_img = tk.Button(root, text="Browse", command=self.browse_image)
        self.btn_img.pack(pady=5)

        # Email entry
        self.label_email = tk.Label(root, text="Enter Your Email:")
        self.label_email.pack(pady=5)

        self.entry_email = tk.Entry(root, width=30)
        self.entry_email.pack(pady=5)

        # Password entry
        self.label_pass = tk.Label(root, text="Enter Your Password:")
        self.label_pass.pack(pady=5)

        self.entry_pass = tk.Entry(root, show="*", width=30)
        self.entry_pass.pack(pady=5)

        # Process button
        self.btn_process = tk.Button(root, text="Process & Send Alert", command=self.start_processing)
        self.btn_process.pack(pady=20)

        # Initialize image path and consumption
        self.image_path = ""
        self.consumption = None

    def browse_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            messagebox.showinfo("File Selected", f"Selected: {self.image_path}")

    def start_processing(self):
        # Start processing in a separate thread
        thread = threading.Thread(target=self.process)
        thread.start()

    def process(self):
        print("Processing started")  # Debug statement
        email = self.entry_email.get()
        password = self.entry_pass.get()

        # Check if email and password are entered
        if not email or not password:
            messagebox.showwarning("Warning", "Please enter both email and password!")
            return

        if not self.image_path:
            messagebox.showwarning("Warning", "Please select an image file!")
            return

        try:
            # Extract consumption from the selected image
            self.consumption = prototype.extract_text(self.image_path)  # Your image processing function
            print(f"Extracted consumption: {self.consumption}")  # Debug statement

            if self.consumption is None:
                messagebox.showerror("Error", "Failed to extract consumption from image!")
                return

            # Check consumption and send email if needed
            if self.consumption >= 500:
                subject = "High Consumption Alert"
                body = f"Your electricity consumption has exceeded 500 kWh. Current consumption: {self.consumption} kWh"
                prototype.send_email(subject, body, email, email, password)  # Send email to the entered address
                messagebox.showinfo("Success", "Alert email sent successfully!")
            else:
                messagebox.showinfo("Consumption", f"Consumption is {self.consumption} kWh, below threshold.")

            # Plot the graph after processing
            prototype.plot_bar_with_thresholds(self.consumption)  # Your graph plotting function

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            print(f"Error occurred: {e}")  # Debug statement

        print("Processing completed")  # Debug statement

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ElectricityTrackerUI(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
