import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Image Size Finder")

# Create a label and a button to select an image file
label = tk.Label(text="Select an image:")
label.pack()

# Create a global variable to store the thumbnail label
thumbnail_label = None

def open_image():
  # Open a file dialog to select an image file
  file_path = filedialog.askopenfilename()

  # Open the image using PIL
  image = Image.open(file_path)

  # Get the size of the image
  width, height = image.size

  # Calculate the size of the thumbnail
  thumbnail_width = width // 4
  thumbnail_height = height // 4

  # Create a thumbnail of the image
  thumbnail = image.resize((thumbnail_width, thumbnail_height), resample=Image.LANCZOS)
  thumbnail = ImageTk.PhotoImage(thumbnail)

  # Remove the previous thumbnail label, if it exists
  global thumbnail_label
  if thumbnail_label:
    thumbnail_label.pack_forget()

  # Create a new thumbnail label to display the thumbnail
  thumbnail_label = Label(image=thumbnail)
  thumbnail_label.image = thumbnail  # keep a reference to the image to prevent garbage collection
  thumbnail_label.pack()

  # Update the label with the size of the image
  label["text"] = f"Selected image has size: {width} x {height}"

button = tk.Button(text="Select Image", command=open_image)
button.pack()

# Run the main loop
window.mainloop()
