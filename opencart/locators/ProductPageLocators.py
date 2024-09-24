from selenium.webdriver.common.by import By


class ProductPageLocators:
    """
    Locators for elements on the Product management page in the admin panel.
    """

    # Locators for the Products submenu and Add New Product button
    PRODUCTS_SUBMENU = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")

    # Locators for the Add/Edit Product form
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    PRODUCT_DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "#input-description1")
    META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_TAB = (By.CSS_SELECTOR, "a[href='#tab-data']")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    # Locators for the Product table and its rows
    PRODUCT_TABLE = (By.CSS_SELECTOR, "table.table-bordered")
    PRODUCT_ROWS = (By.CSS_SELECTOR, "table.table-bordered tbody tr")
