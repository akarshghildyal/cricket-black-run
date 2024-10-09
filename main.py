import pyautogui
from PIL import Image, ImageDraw
import os
import pygetwindow as gw

# Step 0: Ensure the "ss" directory exists
def ensure_ss_directory():
    if not os.path.exists("ss"):
        os.makedirs("ss")
    print("Directory 'ss' is ready.")

# Step 1: Screenshot function for a specific window
def take_screenshot(window_title="AC2001"):
    print(f"Looking for window: {window_title}")
    
    # Find the window by title
    windows = gw.getWindowsWithTitle(window_title)
    if len(windows) == 0:
        print(f"Window titled '{window_title}' not found!")
        return None
    window = windows[0]
    
    print(f"Found window: {window.title}")
    
    # Take a screenshot of the window
    left, top, width, height = window.left, window.top, window.width, window.height
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    
    # Convert to a PIL Image
    screenshot = screenshot.convert("RGB")
    
    # Save screenshot to the "ss" folder
    screenshot_path = os.path.join("ss", "screenshot.png")
    screenshot.save(screenshot_path)
    
    print(f"Screenshot saved to {screenshot_path}")
    
    return screenshot

# Step 2: Function to divide the screen into grids and draw grid lines
def divide_and_draw_grids(image, grid_size):
    print("Dividing screenshot into grids and drawing grid lines...")
    
    img_width, img_height = image.size
    grid_width, grid_height = grid_size

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Draw vertical grid lines
    for i in range(0, img_width, grid_width):
        draw.line([(i, 0), (i, img_height)], fill="red", width=2)

    # Draw horizontal grid lines
    for j in range(0, img_height, grid_height):
        draw.line([(0, j), (img_width, j)], fill="red", width=2)

    print(f"Grid lines drawn with grid size {grid_size}.")

    # Save the image with grid overlay
    grid_image_path = os.path.join("ss", "screenshot_with_grids.png")
    image.save(grid_image_path)
    print(f"Screenshot with grids saved to {grid_image_path}")

    return image

# Step 3: Crop the image to keep specified rows and columns, without verification
def crop_image(image, col_start, col_end, row_start, row_end):
    print(f"Cropping image to keep columns {col_start}-{col_end} and rows {row_start}-{row_end}...")

    # Crop the image
    cropped_image = image.crop((col_start, row_start, col_end, row_end))
    
    # Save the cropped image without any rectangles
    cropped_image_path = os.path.join("ss", "cropped_screenshot.png")
    cropped_image.save(cropped_image_path)  # Save only the cropped image
    print(f"Cropped screenshot saved to {cropped_image_path}")

    return cropped_image

# Example Usage:
if __name__ == "__main__":
    # Step 0: Ensure the "ss" directory exists
    ensure_ss_directory()

    # Step 1: Take a screenshot of the specific window (scrcpy in this case)
    screenshot = take_screenshot("AC2001")  # Adjust the window title as needed

    # Proceed only if screenshot was successfully captured
    if screenshot:
        # Step 2: Divide the screenshot into grids (arbitrary grid size for now, e.g., 50x50) and draw grids
        grid_size = (20, 15)  # Modify based on the size of the ball in the game
        screenshot_with_grids = divide_and_draw_grids(screenshot, grid_size)
        
        # Step 3: Crop the image to keep specific columns and rows
        # Columns: 200-340 and Rows: 360-690
        cropped_image = crop_image(screenshot, 200, 340, 360, 690)
        
        print("All steps completed successfully!")
