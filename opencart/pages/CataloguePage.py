from selenium.webdriver.common.action_chains import ActionChains
from locators import CataloguePageLocators


class CataloguePage:
    """
    Page Object class for interacting with the Catalogue page.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def hover_over_components(self):
        """
        Hovers over the 'Components' menu item.
        """
        components = self.driver.find_element(*CataloguePageLocators.COMPONENTS)
        ActionChains(self.driver).move_to_element(components).perform()

    def click_monitors_link(self):
        """
        Clicks on the 'Monitors' link in the dropdown menu.
        """
        monitors_link = self.driver.find_element(*CataloguePageLocators.MONITORS_LINK)
        monitors_link.click()

    def verify_monitors_page_loaded(self, expected_url):
        """
        Verifies that the 'Monitors' page has loaded by checking the URL.

        :param expected_url: The expected URL of the 'Monitors' page.
        :return: True if the page is loaded correctly, False otherwise.
        """
        actual_url = self.driver.current_url
        return actual_url == expected_url
