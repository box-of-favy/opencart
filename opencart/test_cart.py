from pages import CartPage


def test_add_to_cart(driver):
    """
    Tests adding an item to the cart and verifying the cart update.

    :param driver: WebDriver instance initialized by the fixture.
    """
    cart_page = CartPage(driver)
    cart_page.add_to_cart()
    cart_page.wait_for_cart_update("1 item(s) - $602.00")

    # Verify that the cart has been updated correctly
    cart_total = cart_page.get_cart_total()
    assert cart_total == "1 item(s) - $602.00", "Cart total is incorrect"


def test_cart_click(driver):
    """
    Tests clicking the cart button to open the dropdown menu.

    :param driver: WebDriver instance initialized by the fixture.
    """
    cart_page = CartPage(driver)
    cart_page.click_cart_button()
    cart_page.wait_for_cart_dropdown()


def test_cart_contains(driver):
    """
    Tests that the cart contains the correct product, price, quantity, and total price.

    :param driver: WebDriver instance initialized by the fixture.
    """
    cart_page = CartPage(driver)

    # Verify the correct product was added
    product_name = cart_page.get_product_name()
    assert product_name == "MacBook", "Incorrect product in the cart"

    # Verify the price is correct
    product_price = cart_page.get_product_price()
    assert product_price == "$602.00", "Incorrect product price in the cart"

    # Verify the quantity is correct
    product_quantity = cart_page.get_product_quantity()
    assert product_quantity == "x 1", "Incorrect product quantity in the cart"

    # Verify the total price is correct
    total_price = cart_page.get_total_price()
    assert total_price == "$602.00", "Incorrect total price in the cart"
