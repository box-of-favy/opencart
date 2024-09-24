from selenium.webdriver.common.by import By


class AdminPageLocators:
    """
    Locators for elements on the Admin login and dashboard pages.
    """

    # Login page locators
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Dashboard locators
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href*='route=common/logout']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.close[data-dismiss='modal']")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog > a")
