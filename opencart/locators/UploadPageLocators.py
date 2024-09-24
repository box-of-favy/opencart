from selenium.webdriver.common.by import By


class UploadPageLocators:
    """
    Locators for elements on the Upload page in the admin panel.
    """

    # Button and menu locators
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, ".fa.fa-plus")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "#button-upload")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog > a")
    DOWNLOADS_SUBMENU = (By.CSS_SELECTOR, "a[href*='route=catalog/download']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.close")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".fa.fa-save")
    TRASH_BUTTON = (By.CSS_SELECTOR, ".fa.fa-trash-o")

    # Input locators
    DOWNLOAD_NAME_INPUT = (By.CSS_SELECTOR, "input[name='download_description[1][name]']")

    # Checkbox and row locators for verifying downloads
    @staticmethod
    def DOWNLOAD_CHECKBOX(download_name):
        return (By.XPATH, f"//td[contains(text(), '{download_name}')]/"
                          f"preceding-sibling::td[@class='text-center']/"
                          f"input[@type='checkbox']")

    @staticmethod
    def DOWNLOAD_ROW(download_name):
        return (By.XPATH, f"//td[contains(text(), '{download_name}')]")
