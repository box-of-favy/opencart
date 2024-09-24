from selenium.webdriver.common.by import By


class CategoryPageLocators:
    """
    Locators for elements on the Category management page in the admin panel.
    """

    # Locators for the Categories submenu and Add New Category button
    CATEGORIES_SUBMENU = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(1) > a")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")

    # Locators for the Add/Edit Category form
    CATEGORY_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    CATEGORY_DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "#input-description1")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    META_TAG_DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "#input-meta-description1")
    META_TAG_KEYWORDS_TEXTAREA = (By.CSS_SELECTOR, "#input-meta-keyword1")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    # Locators for the Category table and its elements
    CATEGORY_TABLE = (By.CSS_SELECTOR, "table.table-bordered")
    CATEGORY_ROWS = (By.CSS_SELECTOR, "table.table-bordered tbody tr")
    CATEGORY_NAME_COLUMN = (By.CSS_SELECTOR, "td.text-left")
    SELECT_CHECKBOX = (By.CSS_SELECTOR, "input[name='selected[]']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success")
    CATEGORY_NAME_CELL = (By.CSS_SELECTOR, "td.text-left")
    CATEGORY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    # Locator for the delete confirmation alert and Delete button
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    CONFIRM_DELETE_ALERT = (By.CSS_SELECTOR, ".modal-footer .btn-primary")
