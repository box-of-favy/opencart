from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import SearchPageLocators


class SearchPage:
    """
    Page Object class for search functionality.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def enter_search_term(self, search_term):
        """
        Enters the search term in the search box.

        :param search_term: The term to search for.
        """
        search_box = self.driver.find_element(*SearchPageLocators.SEARCH_BOX)
        assert search_box is not None, "Search box not found"
        search_box.send_keys(search_term)

    def click_search_button(self):
        """
        Clicks the search button to initiate the search.
        """
        search_button = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        search_button.click()

    def wait_for_search_results(self):
        """
        Waits for the search results to appear on the page.

        :return: True if search results are present, False otherwise.
        """
        return WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(SearchPageLocators.SEARCH_RESULTS)
        )

    def get_product_name(self):
        """
        Retrieves the name of the first product from the search results.

        :return: Product name as text.
        """
        product = self.driver.find_element(*SearchPageLocators.SEARCH_RESULTS)
        product_name = product.find_element(*SearchPageLocators.PRODUCT_NAME)
        return product_name.text
