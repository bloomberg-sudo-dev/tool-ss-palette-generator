# Screenshot Palette Generator

## Description
The Screenshot Palette Generator is a desktop application that allows users to capture a selected area of their screen and generate a color palette from the dominant colors in that region. This tool is perfect for designers, artists, and anyone interested in color analysis from digital content.

## Features
- Interactive region selection for screenshots
- Extraction of dominant colors from the selected area
- Visual display of the generated color palette
- Easy-to-use graphical interface

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Required Libraries
Install the following libraries using pip:

```
pip install opencv-python numpy matplotlib mss Pillow
```

### Running the Application
1. Clone or download this repository
2. Navigate to the project directory
3. Run the script:
   ```
   python screenshot_palette_generator.py
   ```

## Usage
1. Launch the application
2. A full-screen capture will be displayed
3. Use your mouse to select the region of interest
4. Press 'Enter' to confirm the selection
5. The application will process the selected area and display the generated color palette

## Building the Executable
To create a standalone executable:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Run PyInstaller:
   ```
   pyinstaller --onefile --windowed screenshot_palette_generator.py
   ```
3. Find the executable in the `dist` folder

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/bloomberg-sudo-dev/tool-ss-palette-generator/issues) if you want to contribute.

## License
MIT License

## Contact
Opemipo Oduntan - opethepope@gmail.com

Project Link: [https://github.com/bloomberg-sudo-dev/tool-ss-palette-generator](https://github.com/bloomberg-sudo-dev/tool-ss-palette-generator)
