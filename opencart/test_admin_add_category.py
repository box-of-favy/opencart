import pytest
from pages.AdminPage import AdminPage
from pages.CategoryPage import CategoryPage
from utils.save_screenshot import save_screenshot
import time


@pytest.fixture(scope="module")
def category_data():
    """
    Fixture to generate test data for adding a new category.

    :return: Dictionary containing category information.
    """
    return {
        "name": "Camera 24",
        "description": "Description for Camera",
        "meta_tag_title": "Cameras Meta Tag Title",
        "meta_tag_description": "Cameras Meta Tag Description",
        "meta_tag_keywords": "Cameras, Meta, Tag, Keywords"
    }


def test_admin_category_management(driver):
    """
    Test to verify the category management workflow for an admin user.

    :param driver: WebDriver instance initialized by the fixture.
    """
    admin_page = AdminPage(driver)
    admin_page.open_login_page().login("admin", "admin")
    admin_page.close_alert()
    admin_page.open_catalog_menu()


def test_open_categories_submenu(driver):
    """
    Test opening the categories submenu in the catalog section.

    :param driver: WebDriver instance initialized by the fixture.
    """
    category_page = CategoryPage(driver)
    logger = driver._listener.logger

    try:
        category_page.open_categories_submenu()
    except Exception as e:
        save_screenshot(driver, "test_open_categories_submenu",
                        driver._listener.screenshot_dir)
        logger.error(f"Failed to open categories submenu: {e}")
        raise


def test_add_new_category(driver, category_data):
    """
    Test adding a new category to the catalog.

    :param driver: WebDriver instance initialized by the fixture.
    :param category_data: Data for the new category provided by the fixture.
    """
    category_page = CategoryPage(driver)
    logger = driver._listener.logger

    # Click the add new category button
    add_category_result = category_page.click_add_new_category()
    if not add_category_result:
        save_screenshot(driver, "test_add_new_category", driver._listener.screenshot_dir)
        logger.error("Failed to click 'Add New Category' button")
    assert add_category_result, "Failed to click 'Add New Category' button"

    # Fill category info
    try:
        category_page.fill_category_info(category_data)
    except Exception as e:
        save_screenshot(driver, "test_add_new_category_fill_info",
                        driver._listener.screenshot_dir)
        logger.error(f"Failed to fill category info: {e}")
        raise


def test_save_category(driver, category_data):
    """
    Test saving a new category and verifying it was added successfully.

    :param driver: WebDriver instance initialized by the fixture.
    :param category_data: Data for the new category provided by the fixture.
    """
    category_page = CategoryPage(driver)
    logger = driver._listener.logger

    # Save the category
    save_result = category_page.save_category_and_verify()
    if not save_result:
        save_screenshot(driver, "test_save_category", driver._listener.screenshot_dir)
        logger.error("Failed to save category or success message not displayed")
    assert save_result, "Failed to save category or success message not displayed"

    # Check if the category is present
    category_present = category_page.is_category_present(category_data["name"])
    if not category_present:
        save_screenshot(driver, "test_save_category_check_presence",
                        driver._listener.screenshot_dir)
        logger.error(f"New category '{category_data['name']}' not found in the list")
    assert category_present, f"New category '{category_data['name']}' not found in the list"


def test_delete_category(driver, category_data):
    """
    Test deleting a category from the catalog.

    :param driver: WebDriver instance initialized by the fixture.
    :param category_data: Data for the new category provided by the fixture.
    """
    category_page = CategoryPage(driver)
    logger = driver._listener.logger

    # Check if the category is present before deletion
    category_present = category_page.is_category_present(category_data["name"])
    if not category_present:
        save_screenshot(driver, "test_delete_category_check_presence",
                        driver._listener.screenshot_dir)
        logger.error(f"Category '{category_data['name']}' not found before deletion attempt")
    assert category_present, (f"Category '{category_data['name']}' "
                              f"not found before deletion attempt")

    # Select and delete the category
    category_selected = category_page.select_category_by_name(category_data["name"])
    if not category_selected:
        save_screenshot(driver, "test_delete_category_select",
                        driver._listener.screenshot_dir)
        logger.error(f"Failed to select category '{category_data['name']}' for deletion")
    assert category_selected, f"Failed to select category '{category_data['name']}' for deletion"

    # Delete the category and verify success
    delete_result = category_page.delete_selected_category()
    if not delete_result:
        save_screenshot(driver, "test_delete_category", driver._listener.screenshot_dir)
        logger.error("Success message for category deletion did not appear")
    assert delete_result, "Success message for category deletion did not appear"

    time.sleep(3)
    # Verify the category is no longer present
    category_still_present = category_page.is_category_present(category_data["name"])
    if category_still_present:
        save_screenshot(driver, "test_delete_category_check_absence",
                        driver._listener.screenshot_dir)
        logger.error(f"Category '{category_data['name']}' still exists after deletion")
    assert not category_still_present, (f"Category '{category_data['name']}' "
                                        f"still exists after deletion")
