#Author: Michael Poe
#Date written: 03/7/24
#Assignment: Final Project
#Short Desc: Scanning Interface for Printing


import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import webbrowser

# Define global variables to store folder locations and logo image
preview_graphic_folder = ""
print_file_folder = ""
logo_image = None  # Initialize logo_image

# Function to scan QR/Barcode
def scan_qr_code(scanned_data):
    search_files(scanned_data)

# Function to search for files
def search_files(scanned_data):
    global preview_graphic_folder, print_file_folder

    # Use the stored folder locations
    preview_graphic_path = preview_graphic_folder
    print_file_path = print_file_folder
    
    # Search for the preview graphic
    preview_graphic_filename = os.path.join(preview_graphic_path, scanned_data + ".png")
    if os.path.exists(preview_graphic_filename):
        # Load the preview graphic while preserving transparency
        preview_image = Image.open(preview_graphic_filename)
        
        # Calculate the size to fit within the black border box without distortion
        max_width = 540
        max_height = 590
        width, height = preview_image.size
        
        if width > max_width or height > max_height:
            width_ratio = max_width / width
            height_ratio = max_height / height
            scale_ratio = min(width_ratio, height_ratio)
            
            # Reduce the size by 5%
            scale_ratio -= 0.00
            new_width = int(width * scale_ratio)
            new_height = int(height * scale_ratio)
            preview_image = preview_image.resize((new_width, new_height), Image.LANCZOS)
        
        # Create a transparent background image of the same size as the border box
        transparent_bg = Image.new("RGBA", (border_box.winfo_width() - 10, border_box.winfo_height() - 10))
        
        # Paste the resized image onto the transparent background
        x_offset = (transparent_bg.width - preview_image.width) // 2
        y_offset = (transparent_bg.height - preview_image.height) // 2
        transparent_bg.paste(preview_image, (x_offset, y_offset))
        
        # Display the image with transparency over the #CCCCCC background
        preview_image = ImageTk.PhotoImage(transparent_bg)
        preview_label.config(image=preview_image)
        preview_label.image = preview_image
    
    # Search for the print file
    print_file_filename = os.path.join(print_file_path, scanned_data + ".ARX4")
    if os.path.exists(print_file_filename):
        # Implement logic to send the print file to the designated IP address for printing
        # You can use libraries like sockets or requests for this task
    
    # Display the graphic name
     graphic_name_label.config(text="Graphic Name: " + scanned_data)

# Function to handle changes in the manual QR entry field
def on_manual_entry_change(event):
    scanned_data = manual_entry.get()
    scan_qr_code(scanned_data)

# Function to open settings popup
def open_settings_popup():
    def browse_preview_folder():
        global preview_graphic_folder
        folder_path = filedialog.askdirectory()
        preview_graphic_folder = folder_path  # Update the global variable
        preview_graphic_entry.delete(0, tk.END)
        preview_graphic_entry.insert(0, preview_graphic_folder)
    
    def browse_print_folder():
        global print_file_folder
        folder_path = filedialog.askdirectory()
        print_file_folder = folder_path  # Update the global variable
        print_file_entry.delete(0, tk.END)
        print_file_entry.insert(0, print_file_folder)
    
    settings_popup = tk.Toplevel(root)
    settings_popup.title("Settings")
    
    # Create labels and entry widgets for each setting
    preview_graphic_label = tk.Label(settings_popup, text="Preview Graphic Folder:")
    preview_graphic_label.grid(row=0, column=0)
    preview_graphic_entry = tk.Entry(settings_popup)
    preview_graphic_entry.grid(row=0, column=1)
    browse_preview_button = tk.Button(settings_popup, text="Browse", command=browse_preview_folder)
    browse_preview_button.grid(row=0, column=2)
    
    print_file_label = tk.Label(settings_popup, text="Print File Folder:")
    print_file_label.grid(row=1, column=0)
    print_file_entry = tk.Entry(settings_popup)
    print_file_entry.grid(row=1, column=1)
    browse_print_button = tk.Button(settings_popup, text="Browse", command=browse_print_folder)
    browse_print_button.grid(row=1, column=2)
    
    # Set the initial values of the entry fields
    preview_graphic_entry.insert(0, preview_graphic_folder)
    print_file_entry.insert(0, print_file_folder)
    
    printer_ip_label = tk.Label(settings_popup, text="Printer IP Address:")
    printer_ip_label.grid(row=2, column=0)
    printer_ip_entry = tk.Entry(settings_popup)
    printer_ip_entry.grid(row=2, column=1)
    
    printer_usb_label = tk.Label(settings_popup, text="Printer USB Device:")
    printer_usb_label.grid(row=3, column=0)
    printer_usb_entry = tk.Entry(settings_popup)
    printer_usb_entry.grid(row=3, column=1)
    
    # Function to save the settings when the OK button is clicked
    def save_settings():
        global preview_graphic_folder, print_file_folder
        preview_graphic_folder = preview_graphic_entry.get()
        print_file_folder = print_file_entry.get()
        printer_ip = printer_ip_entry.get()
        printer_usb = printer_usb_entry.get()
        
        # You can save these settings to a configuration file or use them as needed
        
        settings_popup.destroy()
    
    ok_button = tk.Button(settings_popup, text="OK", command=save_settings)
    ok_button.grid(row=4, columnspan=3)

# Function to open the website when the logo is clicked
def open_website():
    webbrowser.open("https://latailyr.com")

# Create the main application window
root = tk.Tk()
root.geometry("1366x768")
root.title("HOMAGE MVP")

# Create and configure widgets
logo_image = Image.open("homage-logo-primary.png")
logo_image = logo_image.resize((197, 43), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_image)
logo_label.place(x=100, y=55)

scan_label = tk.Label(root, text="SCAN NEXT QR CODE", font=("Arial", 50, "bold"), fg="#0000ff")
scan_label.place(x=94, y=229)

# Create a manual entry box
manual_entry = tk.Entry(root, width=57)
manual_entry.place(x=100, y=300)  # Adjust the position as needed

# Bind manual entry field change to the on_manual_entry_change function
manual_entry.bind("<KeyRelease>", on_manual_entry_change)

# Create a 4px black border empty box
border_box = tk.Label(root, width=65, height=40, bd=4, relief="solid", bg="#CCCCCC")
border_box.place(x=708, y=40)

# Create a label for displaying the preview image within the border box
preview_label = tk.Label(root, bd=0, bg="#CCCCCC")
preview_label.place(x=713, y=45)

graphic_name_label = tk.Label(root, font=("Arial", 25), fg="#000000")
graphic_name_label.place(x=362, y=563)

settings_button_image = Image.open("gearicon.png")
settings_button_image = settings_button_image.resize((47, 47), Image.LANCZOS)
settings_button_image = ImageTk.PhotoImage(settings_button_image)
settings_button = tk.Button(root, image=settings_button_image, command=open_settings_popup)
settings_button.place(x=59, y=700)

# Create a hidden button for the logo in the lower right corner
def open_latailyr():
    webbrowser.open("https://latailyr.com")

logo_button_image = Image.open("PBLatailyr.png")
logo_button_image = logo_button_image.resize((151, 25), Image.LANCZOS)
logo_button_image = ImageTk.PhotoImage(logo_button_image)
logo_button = tk.Button(root, image=logo_button_image, command=open_latailyr, borderwidth=0, highlightthickness=0)
logo_button.place(x=root.winfo_width() + 950, y=root.winfo_height() + 500)

# Start the main event loop
root.mainloop()
