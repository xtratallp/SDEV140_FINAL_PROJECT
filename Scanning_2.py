#Author: Michael Poe
#Date written: 02/26/24
#Assignment: Final Project_TESTING
#Short Desc: SCANNING INTERFACE

import os
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cairosvg

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        
        # Create and configure a label widget
        self.label = tk.Label(root, text="Select the folder containing PNG files:")
        self.label.pack()

        # Create and configure an entry widget
        self.folder_path = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.folder_path)
        self.entry.pack()

        # Create and configure a button widget to browse for a folder
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.browse_button.pack()

        # Create and configure a button widget to start processing
        self.process_button = tk.Button(root, text="Process", command=self.process_images)
        self.process_button.pack()

    def browse_folder(self):
        folder = filedialog.askdirectory()
        self.folder_path.set(folder)

    def generate_jpegs(self, png_files, input_folder, output_folder):
        # Define the background dimensions and resolution
        background_width = 1152  # pixels
        background_height = 972  # pixels
        dpi = 300  # dots per inch

        # Calculate the dimensions in inches
        background_width_inches = background_width / dpi
        background_height_inches = background_height / dpi

        # Calculate the thumbnail size for images
        thumbnail_size = (300, 300)  # Maximum size for each image

        # Calculate positions for the images
        positions = [(29, 189), (335, 189), (700, 189), (29, 810), (335, 810), (700, 810)]

        # Create a white background image with the specified dimensions and resolution
        background = Image.new("RGB", (background_width, background_height), "white")

        for i, png_file in enumerate(png_files[:6]):  # Process up to 6 images
            img = Image.open(os.path.join(input_folder, png_file))
    
            # Resize the image while preserving its aspect ratio to fit within the thumbnail size
            img.thumbnail(thumbnail_size)

            # Calculate the position for the current image
            x, y = positions[i]

            # Paste the image onto the background at the calculated position
            background.paste(img, (x, y))

            # Add filename text below the image (wrapped to 2 lines if needed)
            draw = ImageDraw.Draw(background)
            font = ImageFont.truetype("arial.ttf", 8)
            filename = os.path.splitext(png_file)[0]
            max_text_width = 300  # Maximum width for filename text
            text_lines = [filename[i:i + max_text_width] for i in range(0, len(filename), max_text_width)]
            text_height = 20
            for j, line in enumerate(text_lines):
                text_width, _ = draw.textsize(line, font=font)
                x_text = x + (thumbnail_size[0] - text_width) / 2  # Center text horizontally
                y_text = y + thumbnail_size[1] + (j * text_height)
                draw.text((x_text, y_text), line, font=font, fill="black")

        # Add the logo image to the background
        logo = Image.open("logo.pdf")
        logo.thumbnail((215, 47))
        logo_width, logo_height = logo.size
        logo_x = (background_width - logo_width) // 2
        logo_y = 900
        background.paste(logo, (logo_x, logo_y))

        # Save the generated JPEG.
        jpeg_path = os.path.join(output_folder, "output.jpg")
        background.save(jpeg_path, dpi=(dpi, dpi))


    def create_pdf(self, output_folder, jpeg_files):
        pdf_path = os.path.join(output_folder, "output.pdf")

        # Create a PDF document.
        c = canvas.Canvas(pdf_path, pagesize=letter)
    
        # Add the generated JPEG to the PDF as a page.
        jpeg_path = os.path.join(output_folder, "output.jpg")
        c.drawImage(jpeg_path, 0, 0, width=letter[0], height=letter[1])
        c.showPage()

        # Save the PDF.
        c.save()

    def process_images(self):
        input_folder = self.folder_path.get()

        # Check if the selected folder exists and contains PNG files
        if not os.path.exists(input_folder):
            messagebox.showerror("Error", "Invalid folder path.")
            return

        png_files = [file for file in os.listdir(input_folder) if file.endswith(".png")]

        if not png_files:
            messagebox.showerror("Error", "No PNG files found in the selected folder.")
            return

        # Create an output folder for the generated JPEG and PDF
        output_folder = os.path.join(input_folder, "output")
        os.makedirs(output_folder, exist_ok=True)

        # Generate JPEG
        self.generate_jpegs(png_files, input_folder, output_folder)

        # Create PDF
        self.create_pdf(output_folder, ["output.jpg"])

def main():
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
