import pytest
from pages import AdminPage, ProductPage
import random
import string


def generate_random_string(length):
    """
    Generates a random string of lowercase letters.

    :param length: Length of the random string.
    :return: Random string of specified length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_product_name():
    """
    Generates a random product name.

    :return: Random product name.
    """
    adjectives = ['New', 'Innovative', 'Smart', 'Eco-friendly', 'Advanced']
    nouns = ['Device', 'Gadget', 'Tool', 'Solution', 'Product']
    return f"{random.choice(adjectives)} {random.choice(nouns)} {generate_random_string(5)}"


def generate_model_name():
    """
    Generates a random model name.

    :return: Random model name.
    """
    return f"MOD-{generate_random_string(3)}-{random.randint(100, 999)}"


@pytest.fixture(scope="module")
def product_data():
    """
    Fixture to generate random product data for tests.

    :return: Dictionary containing random product data.
    """
    return {
        "name": generate_product_name(),
        "model": generate_model_name(),
        "description": f"Description for {generate_product_name()}",
        "meta_tag": f"meta,{generate_product_name()},test"
    }


def test_admin_category_management(driver):
    """
    Test the workflow for category management in the admin panel.

    :param driver: WebDriver instance initialized by the fixture.
    """
    admin_page = AdminPage(driver)
    admin_page.open_login_page().login("admin", "admin")
    admin_page.close_alert()
    admin_page.open_catalog_menu()


def test_click_products_submenu(driver):
    """
    Test clicking on the Products submenu in the catalog section.

    :param driver: WebDriver instance initialized by the fixture.
    """
    product_page = ProductPage(driver)
    product_page.open_products_submenu()


def test_click_add_new_product(driver):
    """
    Test clicking on the 'Add New Product' button.

    :param driver: WebDriver instance initialized by the fixture.
    """
    product_page = ProductPage(driver)
    product_page.click_add_new_product()


def test_fill_product_info(driver, product_data):
    """
    Test filling in the product information form.

    :param driver: WebDriver instance initialized by the fixture.
    :param product_data: Data for the product provided by the fixture.
    """
    product_page = ProductPage(driver)
    product_page.fill_product_info(product_data)
