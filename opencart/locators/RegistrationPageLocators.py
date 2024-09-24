from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """
    Locators for elements on the registration page.
    """

    # My Account and dropdown menu locators
    ACCOUNT = (By.CSS_SELECTOR, 'a[title="My Account"]')
    DROPDOWN_MENU = (By.CSS_SELECTOR, '.dropdown-menu.dropdown-menu-right')
    REGISTER_LINK = (By.LINK_TEXT, 'Register')
    LOGIN_LINK = (By.LINK_TEXT, 'Login')

    # Registration form locators
    INPUT_FIRSTNAME = (By.ID, 'input-firstname')
    INPUT_LASTNAME = (By.ID, 'input-lastname')
    INPUT_EMAIL = (By.ID, 'input-email')
    INPUT_TELEPHONE = (By.ID, 'input-telephone')
    INPUT_PASSWORD = (By.ID, 'input-password')
    INPUT_CONFIRM = (By.ID, 'input-confirm')
    PRIVACY_CHECKBOX = (By.NAME, 'agree')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input.btn.btn-primary')

    # Success message and logout link locators
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div#content h1')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href*="route=account/logout"]')
    LOGIN_LINK_IN_ACCOUNT = (By.CSS_SELECTOR, 'a[href*="route=account/login"]')
