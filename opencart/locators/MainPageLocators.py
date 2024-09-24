from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Locators for elements on the main page.
    """

    # Logo locators
    LOGO = (By.CSS_SELECTOR, "#logo a")

    # Search box locators
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-default.btn-lg')
    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, 'div#content h1')

    # Top panel locators
    TOP_PANEL = (By.CSS_SELECTOR, 'nav#top')
    CURRENCY = (By.CSS_SELECTOR, 'form#form-currency button.dropdown-toggle')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, 'form#form-currency ul.dropdown-menu')
    CURRENCY_ITEMS = {
        "EUR": (By.CSS_SELECTOR, 'button[name="EUR"]'),
        "GBP": (By.CSS_SELECTOR, 'button[name="GBP"]'),
        "USD": (By.CSS_SELECTOR, 'button[name="USD"]')
    }
    MY_ACCOUNT = (By.CSS_SELECTOR, 'a[title="My Account"]')
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, 'ul.dropdown-menu-right')
    MY_ACCOUNT_ITEMS = {
        "Register": (By.CSS_SELECTOR, 'a[href*="account/register"]'),
        "Login": (By.CSS_SELECTOR, 'a[href*="account/login"]')
    }
    WISH_LIST = (By.CSS_SELECTOR, 'a#wishlist-total')
    SHOPPING_CART = (By.CSS_SELECTOR, 'a[title="Shopping Cart"]')
    CHECKOUT = (By.CSS_SELECTOR, 'a[title="Checkout"]')

    # Menu elements locators
    MENU_ELEMENTS = {
        "Desktops": (By.XPATH, "//a[contains(text(), 'Desktops')]"),
        "Laptops & Notebooks": (By.XPATH, "//a[contains(text(), 'Laptops & Notebooks')]"),
        "Components": (By.XPATH, "//a[contains(text(), 'Components')]"),
        "Tablets": (By.XPATH, "//a[contains(text(), 'Tablets')]"),
        "Software": (By.XPATH, "//a[contains(text(), 'Software')]"),
        "Phones & PDAs": (By.XPATH, "//a[contains(text(), 'Phones & PDAs')]"),
        "Cameras": (By.XPATH, "//a[contains(text(), 'Cameras')]"),
        "MP3 Players": (By.XPATH, "//a[contains(text(), 'MP3 Players')]")
    }

    # Slideshow locators
    SLIDESHOW = (By.CSS_SELECTOR, 'div#slideshow0')

    # Footer locators
    FOOTER_SECTIONS = {
        "Information": (By.XPATH, "//footer//h5[text()='Information']"),
        "Customer Service": (By.XPATH, "//footer//h5[text()='Customer Service']"),
        "Extras": (By.XPATH, "//footer//h5[text()='Extras']"),
        "My Account": (By.XPATH, "//footer//h5[text()='My Account']")
    }
