from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import ProductPageLocators


class ProductPage:
    """
    Page Object class that encapsulates actions related to Products.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def open_products_submenu(self):
        """
        Click on the Products submenu in the admin panel.
        """
        products_submenu = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(ProductPageLocators.PRODUCTS_SUBMENU)
        )
        products_submenu.click()

    def click_add_new_product(self):
        """
        Click on the 'Add New Product' button and verify navigation.

        :raises AssertionError: If the URL does not match the expected add product URL.
        """
        add_new_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_NEW_BUTTON)
        )
        add_new_button.click()

        expected_url = "http://localhost:8080/admin/index.php?route=catalog/product/add&user_token="
        assert expected_url in self.driver.current_url, "Failed to navigate to add new product page"

    def fill_product_info(self, product_data):
        """
        Fill in the product information form.

        :param product_data: Dictionary containing product details.
        :raises Exception: If the Summernote editor is not initialized properly.
        """
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(ProductPageLocators.PRODUCT_NAME_INPUT)
        ).send_keys(product_data["name"])

        # JavaScript to handle the Summernote editor for description
        description_script = """
        var editor = $('#input-description1').data('summernote');
        if (editor) {
            editor.code(arguments[0]);
            $('#input-description1').val(arguments[0]);
            $('#input-description1').summernote('onChange');
        } else {
            console.error('Summernote editor not initialized');
        }
        """
        self.driver.execute_script(description_script, product_data["description"])

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(ProductPageLocators.META_TAG_INPUT)
        ).send_keys(product_data["meta_tag"])

        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(ProductPageLocators.DATA_TAB)
        ).click()

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(ProductPageLocators.MODEL_INPUT)
        ).send_keys(product_data["model"])
