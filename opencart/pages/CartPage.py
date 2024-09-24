from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from locators import CartPageLocators


class CartPage:
    """
    Page Object class for the Cart page interactions.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def add_to_cart(self):
        """
        Clicks the 'Add to Cart' button to add a product to the cart.
        """
        add_to_cart_button = self.driver.find_element(*CartPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def wait_for_cart_update(self, expected_text):
        """
        Waits until the cart is updated with the expected text.

        :param expected_text: The expected text in the cart (e.g., "1 item(s) - $602.00").
        """
        WebDriverWait(self.driver, 10).until(
            ec.text_to_be_present_in_element(CartPageLocators.CART_TOTAL, expected_text)
        )

    def get_cart_total(self):
        """
        Returns the cart total as displayed in the cart summary.

        :return: Cart total text.
        """
        return self.driver.find_element(*CartPageLocators.CART_TOTAL).text

    def click_cart_button(self):
        """
        Clicks the cart button to open the cart dropdown menu.
        """
        cart_button = self.driver.find_element(*CartPageLocators.CART_BUTTON)
        cart_button.click()

    def wait_for_cart_dropdown(self):
        """
        Waits until the cart dropdown menu is visible.
        """
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(CartPageLocators.CART_DROPDOWN_MENU)
        )

    def get_product_name(self):
        """
        Returns the name of the product currently in the cart.

        :return: Product name text.
        """
        return self.driver.find_element(*CartPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """
        Returns the price of the product currently in the cart.

        :return: Product price text.
        """
        return self.driver.find_element(*CartPageLocators.PRODUCT_PRICE).text

    def get_product_quantity(self):
        """
        Returns the quantity of the product currently in the cart.

        :return: Product quantity text.
        """
        return self.driver.find_element(*CartPageLocators.PRODUCT_QUANTITY).text

    def get_total_price(self):
        """
        Returns the total price of all products in the cart.

        :return: Total price text.
        """
        return self.driver.find_element(*CartPageLocators.TOTAL_PRICE).text
