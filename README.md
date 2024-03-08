# QR Code Scanning and Printing Interface

## Project Overview
This application provides a user-friendly interface for scanning QR codes or barcodes, displaying associated preview graphics, and managing print files for a printing process. Built with `tkinter` in Python, it features a main window for scanning and a settings window for configuration, ensuring easy navigation and functionality.

## Features
- **GUI Interaction**: A straightforward graphical interface for scanning and displaying graphics.
- **Modular Design**: Organized code structure for ease of maintenance and scalability.
- **Image Handling**: Incorporates images within the application, complete with alternate text.
- **Dynamic UI Elements**: Includes labels and buttons with clear navigation and callback functions.
- **Secure Input Validation**: Ensures secure and validated user inputs across the application.

## Installation
1. **Prerequisites**: Ensure you have Python installed on your system. Python 3.6 or later is recommended. Additionally, you will need `Pillow` for image processing.
   
   Install Pillow via pip:

2. **Running the Application**: Navigate to the project directory and run the application Scanning_2.py


## Usage
- **Scanning QR Codes**: Use the main window to scan QR codes by entering the code manually or through a scanning device.
- **Viewing and Printing**: Upon scanning, preview graphics are displayed, and options for printing are provided.
- **Settings Configuration**: Access the settings window to configure folder paths for preview graphics and print files, along with printer IP and USB settings.

## Validation Testing
The application has been thoroughly tested with various data sets to ensure reliability and functionality. Test data included valid and invalid QR codes, varying image sizes, and different file paths.

### Test Results
The testing process revealed the importance of input validation and error handling, leading to improvements in user input checks and the robustness of file operations.

## Acknowledgements
- Tools used: Python, Tkinter, Pillow
- Author: Michael Poe

For more information or to report issues, please visit the project repository or contact the author.
