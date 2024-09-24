import os
import datetime


def save_screenshot(driver, test_name, screenshots_dir):
    """
    Saves a screenshot of the current state of the browser.

    :param driver: Web driver instance to take the screenshot from.
    :param test_name: Name of the test case to include in the screenshot name.
    :param screenshots_dir: Directory where the screenshot will be saved.
    :raises OSError: If the directory cannot be created or accessed.
    """
    try:
        # Create a unique name for the screenshot using the current date and time
        screenshot_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = os.path.join(screenshots_dir, f"{test_name}_error_{screenshot_time}.png")

        # Ensure the directory exists
        os.makedirs(screenshots_dir, exist_ok=True)

        # Save the screenshot
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved: {screenshot_name}")
    except OSError as e:
        raise OSError(f"Failed to create or access the directory '{screenshots_dir}': {e}")
