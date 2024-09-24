from pages import SearchPage


def test_search_functionality(driver):
    """
    Tests the search functionality by entering a search term and clicking the search button.

    :param driver: WebDriver instance initialized by the fixture.
    """
    search_page = SearchPage(driver)
    search_page.enter_search_term("HP LP3065")
    search_page.click_search_button()


def test_results(driver):
    """
    Tests the search results and checks if the correct product is displayed.

    :param driver: WebDriver instance initialized by the fixture.
    """
    search_page = SearchPage(driver)
    search_page.wait_for_search_results()

    product_name = search_page.get_product_name()
    assert product_name == "HP LP3065", "Product 'HP LP3065' not found in search results"

    print("Search was successful, and the product was found in the results.")
