import pytest
from pages.AdminPage import AdminPage
from utils.save_screenshot import save_screenshot


def test_admin_category_management(driver):
    """
    Tests the entire workflow for category management, including login, alert handling, and opening the catalog.

    :param driver: WebDriver instance initialized by the fixture.
    """
    admin_page = AdminPage(driver)

    # Open the admin login page
    try:
        admin_page.open_login_page()
    except Exception as e:
        save_screenshot(driver, "test_admin_category_management_open_login_page", driver._listener.screenshot_dir)
        raise AssertionError(f"Failed to open admin login page: {e}")

    # Perform login
    try:
        admin_page.login("admin", "admin")
    except Exception as e:
        save_screenshot(driver, "test_admin_category_management_login", driver._listener.screenshot_dir)
        raise AssertionError(f"Failed to log in as admin: {e}")

    # Close any alerts that appear
    try:
        admin_page.close_alert()
    except Exception as e:
        save_screenshot(driver, "test_admin_category_management_close_alert", driver._listener.screenshot_dir)
        raise AssertionError(f"Failed to close alert: {e}")

    # Open the catalog menu
    try:
        admin_page.open_catalog_menu()
    except Exception as e:
        save_screenshot(driver, "test_admin_category_management_open_catalog_menu", driver._listener.screenshot_dir)
        raise AssertionError(f"Failed to open catalog menu: {e}")
