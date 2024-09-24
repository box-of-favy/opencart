from pages import MainPage


def test_logo_presence(driver):
    """
    Tests that the logo is present on the main page.

    :param driver: WebDriver instance initialized by the fixture.
    """
    assert MainPage(driver).open().is_logo_present(), "Logo is not present"


def test_logo_click(driver):
    """
    Tests that clicking the logo navigates to the main page.

    :param driver: WebDriver instance initialized by the fixture.
    """
    main_page = MainPage(driver).open()
    main_page.click_logo()
    assert driver.current_url == "http://localhost:8080/index.php?route=common/home", \
        "Logo does not lead to the main page"


def test_top_panel(driver):
    """
    Tests that the top panel is present on the main page.

    :param driver: WebDriver instance initialized by the fixture.
    """
    assert MainPage(driver).open().is_top_panel_present(), "Top panel is not present"


def test_elements(driver):
    """
    Tests that all elements are present in the top panel.

    :param driver: WebDriver instance initialized by the fixture.
    """
    main_page = MainPage(driver).open()
    elements = ["CURRENCY", "MY_ACCOUNT", "WISH_LIST", "SHOPPING_CART", "CHECKOUT"]

    for name in elements:
        assert main_page.get_top_panel_element(name) is not None, f"{name} is not present"


def test_currency_dropdown(driver):
    """
    Tests that the currency dropdown is functional and all elements are present.

    :param driver: WebDriver instance initialized by the fixture.
    """
    main_page = MainPage(driver).open()
    main_page.click_currency()
    dropdown_items = main_page.get_currency_dropdown_items()
    for name, element in dropdown_items.items():
        assert element is not None, f"{name} in Currency dropdown is not present"


def test_my_account_dropdown(driver):
    """
    Tests that the 'My Account' dropdown is functional and all elements are present.

    :param driver: WebDriver instance initialized by the fixture.
    """
    main_page = MainPage(driver).open()
    main_page.click_my_account()
    dropdown_items = main_page.get_my_account_dropdown_items()
    for name, element in dropdown_items.items():
        assert element is not None, f"{name} in My Account dropdown is not present"


def test_menu_elements(driver):
    """
    Tests that all elements in the navigation menu are present.

    :param driver: WebDriver instance initialized by the fixture.
    """
    main_page = MainPage(driver).open()
    missing_elements = main_page.check_menu_elements()
    assert not missing_elements, (f"The following menu elements are missing: "
                                  f"{', '.join(missing_elements)}")


def test_slideshow_presence(driver):
    """
    Tests that the slideshow is present on the main page.

    :param driver: WebDriver instance initialized by the fixture.
    """
    assert MainPage(driver).open().is_slideshow_present(), "Slideshow is not present"


def test_footer(driver):
    """
    Tests that all footer sections are present on the main page.

    :param driver: WebDriver instance initialized by the fixture.
    """
    main_page = MainPage(driver).open()
    main_page.verify_footer_sections()
