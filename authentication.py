import mailsend  # Assuming this module sends email notifications
from graph import plot_bar_with_thresholds  # Import the graphing function
from tkinter import messagebox
from PIL import Image
import pytesseract

# Set the tesseract path if needed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Change this to your tesseract installation path if needed

# Simulate a user credentials storage
user_credentials = {}

def extract_number_from_image(image_path):
    """Extract number from the given image using OCR."""
    try:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Convert the image to grayscale for better OCR results
        img = img.convert("L")

        # Optional: Binarize the image (thresholding) for better contrast
        threshold = 150  # Adjust threshold value as needed
        img = img.point(lambda x: 255 if x > threshold else 0)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img, config='--psm 6')  # Use page segmentation mode 6 for better results

        # Extract numbers from the text
        numbers = ''.join(filter(str.isdigit, text))
        
        return int(numbers) if numbers else None
    except Exception as e:
        print(f"Error in extracting number: {e}")
        return None


def register_user(email, password):
    if email in user_credentials:
        messagebox.showerror("Error", "Email already registered.")
    else:
        user_credentials[email] = password
        messagebox.showinfo("Success", "User registered successfully.")

def login_user(email, password, image_path):
    """Modified to accept image_path as an argument."""
    if email in user_credentials and user_credentials[email] == password:
        messagebox.showinfo("Success", "Login successful.")

        # After logging in, process the image and get the consumption
        consumption = process_image(image_path)  # Now retrieves consumption based on the selected image path
        
        if consumption is not None:
            plot_bar_with_thresholds(consumption)  # Display the graph after login
        
        return email  # Return user email after successful login
    else:
        messagebox.showerror("Error", "Invalid email or password.")
        return None

def process_image(image_path):
    """Process the image to extract the consumption value."""
    if image_path:  # Assuming image_path is available
        consumption = extract_number_from_image(image_path)  # Use the new OCR function
        return consumption
    return None
