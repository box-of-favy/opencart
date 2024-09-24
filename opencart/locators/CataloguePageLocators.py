from selenium.webdriver.common.by import By


class CataloguePageLocators:
    """
    Locators for elements on the Catalogue page.
    """

    # Locators for components and monitors
    MONITORS_LINK = (By.CSS_SELECTOR, 'a[href*="route=product/category&path=25_28"]')
    COMPONENTS = (By.CSS_SELECTOR, 'a[href*="product/category&path=25"]')
