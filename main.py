import pyautogui
from PIL import Image
import os
import pygetwindow as gw
import numpy as np
import keyboard
import time

# Define the RGB color for the red ball
RED_BALL_COLOR = (138, 11, 0)  # RGB equivalent of hex #8a0b00

# Step 0: Ensure the "ss" directory exists
def ensure_ss_directory():
    if not os.path.exists("ss"):
        os.makedirs("ss")
    print("Directory 'ss' is ready.")

# Step 1: Capture a specific region directly
def capture_region(window_title="AC2001", region=(360, 420, 140, 330)): 
    print(f"Looking for window: {window_title}")

    # Find the window by title
    windows = gw.getWindowsWithTitle(window_title)
    if len(windows) == 0:
        print(f"Window titled '{window_title}' not found!")
        return None
    window = windows[0]
    
    print(f"Found window: {window.title}")
    
    # Calculate the region for screenshot
    left, top = window.left + region[0], window.top + region[1]
    width, height = region[2], region[3]
    
    # Take a screenshot of the specific region
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    
    # Convert to a PIL Image
    screenshot = screenshot.convert("RGB")
    
    return screenshot

# Step 3: Crop the image to keep specified rows and columns (if needed, but not necessary now)
def crop_image(image):
    return image  # Since we're capturing directly, we may not need to crop

# Step 4: Detect red ball in the image and click if found
def detect_and_click_ball(cropped_image, frame_count):
    # Convert the cropped image to numpy array for easy pixel access
    pixels = np.array(cropped_image)

    # Check if the red ball is present in the image
    red_ball_detected = np.any(np.all(pixels == RED_BALL_COLOR, axis=-1))
    
    if red_ball_detected:
        # Click at the current mouse position
        pyautogui.click()
        print("Red ball detected! Clicked.")
        
    # Save the cropped image for verification
    cropped_image_path = os.path.join("ss", f"cropped_screenshot_{frame_count}.png")
    cropped_image.save(cropped_image_path)
    print(f"Cropped image saved to {cropped_image_path}")

# Example Usage:
if __name__ == "__main__":
    ensure_ss_directory()
    
    frame_count = 0  # Counter for naming cropped images
    
    while True:
        # Check for spacebar press to exit the loop
        if keyboard.is_pressed('space'):
            print("Spacebar pressed. Exiting...")
            break
        
        screenshot = capture_region("AC2001", (360, 420, 140, 330))  # Adjust the region as needed

        if screenshot:
            # No need to crop since we're capturing the area directly
            cropped_image = screenshot
            
            # Detect red ball and click if found
            detect_and_click_ball(cropped_image, frame_count)
            
            frame_count += 1  # Increment frame count for naming cropped images

        # Adjust the sleep time to increase capture speed
        #time.sleep(0.005)  # Reducing this will capture faster (50ms)
