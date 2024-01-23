import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def resize_image(input_path, size):
    if not os.path.isfile(input_path):
        messagebox.showerror("Error", "Invalid file path")
        return

    directory, original_filename = os.path.split(input_path)
    filename, extension = os.path.splitext(original_filename)
    output_path = os.path.join(directory, f"{filename}_resized{extension}")

    try:
        with Image.open(input_path) as img:
            resized_img = img.resize(size)
            resized_img.save(output_path)
        messagebox.showinfo("Success", f"Image resized and saved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename()
    if file_path:  # Only update if a file was selected
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def resize_action():
    input_path = input_entry.get()
    if not input_path:
        messagebox.showwarning("Warning", "Please select an image to resize")
        return

    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        resize_image(input_path, (width, height))
    except ValueError:
        messagebox.showerror("Error", "Invalid width or height")


# Set up the GUI
root = tk.Tk()
root.title("Image Resizer")

# Input file selection
tk.Label(root, text="Select Image to Resize:").grid(row=0, column=0, sticky=tk.W)
input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Size inputs
tk.Label(root, text="Width:").grid(row=1, column=0, sticky=tk.W)
width_entry = tk.Entry(root, width=10)
width_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
tk.Label(root, text="Height:").grid(row=2, column=0, sticky=tk.W)
height_entry = tk.Entry(root, width=10)
height_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

# Resize button
resize_button = tk.Button(root, text="Resize Image", command=resize_action)
resize_button.grid(row=3, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

root.mainloop()
