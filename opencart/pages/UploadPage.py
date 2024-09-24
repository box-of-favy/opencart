import random
import string
import time
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import UploadPageLocators


class UploadPage:
    """
    Page Object class for handling file uploads in the admin panel.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def navigate_to_download_page(self):
        """
        Navigates to the Downloads page through the Catalog menu.
        """
        catalog_menu = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(UploadPageLocators.CATALOG_MENU)
        )
        catalog_menu.click()

        downloads_submenu = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(UploadPageLocators.DOWNLOADS_SUBMENU)
        )
        downloads_submenu.click()

    def click_add_new_button(self):
        """
        Clicks the 'Add New' button to initiate the file upload process.
        """
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(UploadPageLocators.ADD_NEW_BUTTON)
        ).click()

    def upload_file(self, file_path):
        """
        Uploads a file by opening the file dialog and typing the path.

        :param file_path: Path of the file to upload.
        """
        upload_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(UploadPageLocators.UPLOAD_BUTTON)
        )
        upload_button.click()

        time.sleep(3)  # Wait for file dialog to open

        # Simulate typing the file path and pressing Enter
        keyboard = Controller()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def check_success_alert(self):
        """
        Verifies if the success alert is displayed after file upload.
        """
        WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        assert "Your file was successfully uploaded!" in alert.text, \
            "Success message not found"
        time.sleep(2)
        alert.accept()

    def generate_random_name(self):
        """
        Generates a random name for the download.

        :return: Random string to be used as a download name.
        """
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return f"Fauna_{random_string}"

    def change_download_name(self, new_name):
        """
        Changes the download name in the form to the provided new name.

        :param new_name: New name to set for the download.
        """
        download_name_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(UploadPageLocators.DOWNLOAD_NAME_INPUT)
        )
        download_name_input.clear()
        download_name_input.send_keys(new_name)

    def click_save_button(self):
        """
        Clicks the 'Save' button to save the new download.
        """
        save_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(UploadPageLocators.SAVE_BUTTON)
        )
        save_button.click()

    def verify_download_in_table(self, download_name):
        """
        Verifies if the new download appears in the table after saving.

        :param download_name: The name of the download to verify.
        """
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(UploadPageLocators.DOWNLOAD_ROW(download_name))
        )

    def delete_download(self, download_name):
        """
        Deletes the download by selecting its checkbox and clicking the trash icon.

        :param download_name: The name of the download to delete.
        """
        checkbox = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(UploadPageLocators.DOWNLOAD_CHECKBOX(download_name))
        )
        self.driver.execute_script("arguments[0].click();", checkbox)

        trash_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(UploadPageLocators.TRASH_BUTTON)
        )
        trash_button.click()

        WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def verify_download_absence_in_table(self, download_name):
        """
        Verifies that the download is no longer present in the table after deletion.

        :param download_name: The name of the download to verify.
        """
        time.sleep(3)
        elements = self.driver.find_elements(*UploadPageLocators.DOWNLOAD_ROW(download_name))
        assert not elements, f"Download '{download_name}' is still present in the table after deletion."
