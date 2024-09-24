from selenium.common.exceptions import NoSuchElementException, TimeoutException
from locators import CategoryPageLocators


class CategoryPage:
    """Page Object class that encapsulates actions related to Categories on the admin page."""

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: The web driver instance.
        """
        self.driver = driver

    def open_categories_submenu(self):
        """
        Click on the Categories submenu in the admin panel.

        :raises NoSuchElementException: If the submenu is not found.
        """
        try:
            categories_submenu = self.driver.find_element(*CategoryPageLocators.CATEGORIES_SUBMENU)
            categories_submenu.click()
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Categories submenu not found: {e}")

    def click_add_new_category(self):
        """
        Click on the 'Add New Category' button.

        :return: True if the button is successfully clicked, False otherwise.
        :raises TimeoutException: If the 'Add New' button is not clickable.
        """
        try:
            add_new_button = self.driver.find_element(*CategoryPageLocators.ADD_NEW_BUTTON)
            add_new_button.click()
        except TimeoutException as e:
            print(f"Timeout while trying to click 'Add New' button: {e}")
            return False
        return True

    def fill_category_info(self, category_data):
        """
        Fill in the category information form.

        :param category_data: Dictionary containing the category details (name, description, meta tags).
        :raises NoSuchElementException: If any form element is not found.
        """
        try:
            self.driver.find_element(*CategoryPageLocators.CATEGORY_NAME_INPUT).send_keys(category_data["name"])

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
            self.driver.execute_script(description_script, category_data["description"])

            self.driver.find_element(*CategoryPageLocators.META_TAG_TITLE_INPUT).send_keys(category_data["meta_tag_title"])
            self.driver.find_element(*CategoryPageLocators.META_TAG_DESCRIPTION_TEXTAREA).send_keys(category_data["meta_tag_description"])
            self.driver.find_element(*CategoryPageLocators.META_TAG_KEYWORDS_TEXTAREA).send_keys(category_data["meta_tag_keywords"])

        except NoSuchElementException as e:
            raise NoSuchElementException(f"Failed to fill category info, element not found: {e}")

    def save_category(self):
        """
        Click the Save button to save the category.

        :raises NoSuchElementException: If the save button is not found.
        """
        try:
            save_button = self.driver.find_element(*CategoryPageLocators.SAVE_BUTTON)
            save_button.click()
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Save button not found: {e}")

    def is_success_message_present(self):
        """
        Check if the success message is present on the page after an action.

        :return: True if the success message is found, False otherwise.
        :raises NoSuchElementException: If the success message element is not found.
        """
        try:
            success_message = self.driver.find_element(*CategoryPageLocators.SUCCESS_MESSAGE)
            return "Success: You have modified categories!" in success_message.text
        except NoSuchElementException:
            return False

    def save_category_and_verify(self):
        """
        Save the category and verify the success message.

        :return: True if the category is saved successfully, False otherwise.
        """
        self.save_category()
        return self.is_success_message_present()

    def select_category_by_name(self, category_name):
        """
        Find a category by name in the list and click its checkbox.

        :param category_name: Name of the category to select.
        :return: True if the category is found and selected, False otherwise.
        :raises NoSuchElementException: If the category is not found.
        """
        try:
            rows = self.driver.find_elements(*CategoryPageLocators.CATEGORY_ROWS)
            for row in rows:
                name = row.find_element(*CategoryPageLocators.CATEGORY_NAME_CELL).text
                if name == category_name:
                    checkbox = row.find_element(*CategoryPageLocators.CATEGORY_CHECKBOX)
                    checkbox.click()
                    return True
            return False
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Category '{category_name}' not found: {e}")

    def delete_selected_category(self):
        """
        Delete the selected category and verify the success message.

        :return: True if the category is successfully deleted, False otherwise.
        :raises NoSuchElementException: If delete button or alert is not found.
        """
        try:
            delete_button = self.driver.find_element(*CategoryPageLocators.DELETE_BUTTON)
            delete_button.click()

            self.driver.switch_to.alert.accept()
            return self.is_success_message_present()
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Delete button or alert not found: {e}")

    def is_category_present(self, category_name):
        """
        Check if a category is present in the list by its name.

        :param category_name: Name of the category to check.
        :return: True if the category is present, False otherwise.
        :raises NoSuchElementException: If the category table is not found.
        """
        try:
            rows = self.driver.find_elements(*CategoryPageLocators.CATEGORY_ROWS)
            for row in rows:
                name = row.find_element(*CategoryPageLocators.CATEGORY_NAME_CELL).text
                if name == category_name:
                    return True
            return False
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Category '{category_name}' not found in the list: {e}")
