from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import AdminPageLocators
from selenium.common.exceptions import TimeoutException


class AdminPage:
    """
    Page Object class that encapsulates Admin Login and Dashboard actions.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def open_login_page(self):
        """
        Opens the Admin Login page.

        :return: Self for method chaining.
        """
        self.driver.get("http://localhost:8080/admin/")
        return self

    def login(self, username, password):
        """
        Logs in to the admin panel using provided username and password.

        :param username: Admin username.
        :param password: Admin password.
        """
        self.driver.find_element(*AdminPageLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*AdminPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*AdminPageLocators.LOGIN_BUTTON).click()

    def close_alert(self):
        """
        Closes any alert or modal present on the page.
        """
        try:
            WebDriverWait(self.driver, 5).until(ec.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass  # No alert present, continue

        try:
            close_button = self.driver.find_element(*AdminPageLocators.MODAL_CLOSE_BUTTON)
            close_button.click()
        except TimeoutException:
            pass  # No modal close button found, continue

    def open_catalog_menu(self):
        """
        Clicks on the Catalog menu in the admin panel.
        """
        catalog_menu = self.driver.find_element(*AdminPageLocators.CATALOG_MENU)
        catalog_menu.click()
