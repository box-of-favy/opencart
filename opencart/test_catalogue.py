import pytest
from pages import CataloguePage


@pytest.mark.usefixtures("driver")
def test_product_category(driver):
    """
    Tests navigating to the 'Monitors' category through the 'Components' menu.

    :param driver: WebDriver instance initialized by the fixture.
    """
    menu_page = CataloguePage(driver)
    logger = driver._listener.logger

    try:
        # Log hovering over 'Components' in the menu
        menu_page.hover_over_components()

        # Log clicking on 'Monitors'
        menu_page.click_monitors_link()

        # Check if the 'Monitors' page loaded correctly
        expected_url = "http://localhost:8080/index.php?route=product/category&path=25_28"
        if not menu_page.verify_monitors_page_loaded(expected_url):
            actual_url = driver.current_url
            error_message = (f"Failed to load 'Monitors' page. Expected URL: {expected_url}, "
                             f"but got: {actual_url}. This might indicate a bug on the site.")
            raise AssertionError(error_message)

        logger.info("Successfully navigated to the Monitors page.")

    except Exception as e:
        # Log the error and save a screenshot
        logger.error(f"Test failed due to: {str(e)}")
        from utils.save_screenshot import save_screenshot
        save_screenshot(driver, "test_product_category", driver._listener.screenshot_dir)
        raise
