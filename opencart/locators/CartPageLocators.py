from selenium.webdriver.common.by import By


class CartPageLocators:
    """
    Locators for elements on the Cart page.
    """

    # Locators for adding products and viewing cart details
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(., 'Add to Cart')]")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    CART_DROPDOWN_MENU = (By.CSS_SELECTOR, "#cart .dropdown-menu")

    # Locators for product information inside the cart
    PRODUCT_NAME = (By.CSS_SELECTOR, "#cart td[class='text-left'] a")
    PRODUCT_PRICE = (By.XPATH, "//div[@id='cart']//td[contains(@class, 'text-right')][2]")
    PRODUCT_QUANTITY = (By.XPATH, "//td[normalize-space()='x 1']")

    # Locator for the total price in the cart
    TOTAL_PRICE = (By.XPATH, "//tbody/tr[4]/td[2]")
