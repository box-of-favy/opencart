from selenium.webdriver.common.by import By


class SearchPageLocators:
    """
    Locators for elements on the search page.
    """

    # Search box and button locators
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-default.btn-lg')

    # Search results locators
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'div.product-thumb')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h4 a')
