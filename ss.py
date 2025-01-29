import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from mss import mss
from PIL import Image

def select_roi_and_screenshot():
    # Capture the entire screen
    with mss() as sct:
        monitor = sct.monitors[0]  # Capture the primary monitor
        screenshot = sct.grab(monitor)
        # Convert to numpy array
        img = np.array(Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX"))
        # Convert from RGB to BGR (OpenCV uses BGR)
        screen = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Select ROI
    roi = cv2.selectROI("Select Region", screen, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    
    # Crop the image
    screenshot = screen[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    return screenshot

def extract_colors(image, num_colors=10):
    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)

    # Count the frequency of each color
    color_count = defaultdict(int)
    for pixel in pixels:
        color_count[tuple(pixel)] += 1

    # Sort colors by frequency and extract the most dominant ones
    sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)[:num_colors]
    dominant_colors = [color[0] for color in sorted_colors]

    return dominant_colors

def display_palette(colors):
    plt.figure(figsize=(8, 2))
    for i, color in enumerate(colors):
        plt.fill_between([i, i + 1], 0, 1, color=[c / 255 for c in color[::-1]])  # BGR to RGB
    plt.xlim(0, len(colors))
    plt.axis('off')
    plt.show()

def main():
    # Step 1: Take a screenshot with region selection
    screenshot = select_roi_and_screenshot()

    # Step 2: Extract dominant colors
    num_colors = 10  # Number of colors to extract
    dominant_colors = extract_colors(screenshot, num_colors)

    # Step 3: Display the color palette
    print("Generated Color Palette:")
    display_palette(dominant_colors)

if __name__ == "__main__":
    main()
