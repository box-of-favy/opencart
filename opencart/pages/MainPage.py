from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class MainPage:
    """
    Page Object class for actions and verifications on the main page.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def open(self):
        """
        Opens the main page.

        :return: Self instance for method chaining.
        """
        self.driver.get("http://localhost:8080")
        return self

    def is_logo_present(self):
        """
        Checks if the logo is present on the main page.

        :return: True if logo is present, False otherwise.
        """
        return self.driver.find_element(*MainPageLocators.LOGO) is not None

    def click_logo(self):
        """
        Clicks the logo and navigates to the main page.
        """
        self.driver.find_element(*MainPageLocators.LOGO).click()

    def is_top_panel_present(self):
        """
        Checks if the top panel is present.

        :return: True if top panel is present, False otherwise.
        """
        return self.driver.find_element(*MainPageLocators.TOP_PANEL) is not None

    def get_top_panel_element(self, name):
        """
        Returns a specific element from the top panel by name.

        :param name: Name of the top panel element.
        :return: Web element if found, raises ValueError otherwise.
        """
        top_panel_elements = {
            "CURRENCY": MainPageLocators.CURRENCY,
            "MY_ACCOUNT": MainPageLocators.MY_ACCOUNT,
            "WISH_LIST": MainPageLocators.WISH_LIST,
            "SHOPPING_CART": MainPageLocators.SHOPPING_CART,
            "CHECKOUT": MainPageLocators.CHECKOUT
        }
        if name not in top_panel_elements:
            raise ValueError(f"Top panel item '{name}' not found.")
        return self.driver.find_element(*top_panel_elements[name])

    def check_menu_elements(self):
        """
        Verifies if all menu elements are present.

        :return: List of missing elements, if any.
        """
        menu_elements = ["Desktops", "Laptops & Notebooks", "Components",
                         "Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]
        missing_elements = []

        for name in menu_elements:
            try:
                WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located(MainPageLocators.MENU_ELEMENTS[name])
                )
            except TimeoutException:
                missing_elements.append(name)

        return missing_elements

    def is_slideshow_present(self):
        """
        Checks if the slideshow is present on the main page.

        :return: True if slideshow is present, False otherwise.
        """
        return self.driver.find_element(*MainPageLocators.SLIDESHOW) is not None

    def click_currency(self):
        """
        Clicks on the currency selection dropdown.
        """
        self.driver.find_element(*MainPageLocators.CURRENCY).click()

    def get_currency_dropdown_items(self):
        """
        Returns items from the currency dropdown.

        :return: Dictionary of currency dropdown items.
        """
        dropdown = self.driver.find_element(*MainPageLocators.CURRENCY_DROPDOWN)
        return {
            name: dropdown.find_element(*locator)
            for name, locator in MainPageLocators.CURRENCY_ITEMS.items()
        }

    def click_my_account(self):
        """
        Clicks on the 'My Account' dropdown.
        """
        self.driver.find_element(*MainPageLocators.MY_ACCOUNT).click()

    def get_my_account_dropdown_items(self):
        """
        Returns items from the 'My Account' dropdown.

        :return: Dictionary of 'My Account' dropdown items.
        """
        dropdown = self.driver.find_element(*MainPageLocators.MY_ACCOUNT_DROPDOWN)
        return {
            name: dropdown.find_element(*locator)
            for name, locator in MainPageLocators.MY_ACCOUNT_ITEMS.items()
        }

    def is_footer_section_present(self, name):
        """
        Checks if a footer section is present by name.

        :param name: Name of the footer section.
        :return: True if section is present, False otherwise.
        """
        if name not in MainPageLocators.FOOTER_SECTIONS:
            raise ValueError(f"Footer section '{name}' not found.")
        locator = MainPageLocators.FOOTER_SECTIONS[name]
        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def verify_footer_sections(self):
        """
        Verifies that all footer sections are present.

        :return: True if all sections are present, raises AssertionError otherwise.
        """
        missing_sections = [
            name for name in MainPageLocators.FOOTER_SECTIONS.keys()
            if not self.is_footer_section_present(name)
        ]
        if missing_sections:
            raise AssertionError(
                f"These footer sections are missing: {', '.join(missing_sections)}"
            )
        return True
