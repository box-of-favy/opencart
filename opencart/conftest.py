import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.events import EventFiringWebDriver
from utils import setup_logging, EventListener


def pytest_addoption(parser):
    """
    Adds custom command-line options for specifying the browser type and implicit wait time.

    :param parser: Parser object to add options.
    """
    parser.addoption("--browser", action="store", default="both",
                     help="Browser to use for tests: chrome, firefox, or both")
    parser.addoption("--wait", action="store", default=10, type=int,
                     help="Implicit wait time for the browser")


def pytest_generate_tests(metafunc):
    """
    Parametrizes the test suite to run tests across different browsers as per the command-line option.

    :param metafunc: The metafunc object representing the current test function.
    """
    if "driver" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("browser")
        if browsers == "both":
            metafunc.parametrize("browser", ["chrome", "firefox"], scope="module")
        else:
            metafunc.parametrize("browser", [browsers], scope="module")


def open_driver(browser, proxy=None):
    """
    Opens the browser driver based on the specified browser.

    :param browser: The browser type to open (chrome or firefox).
    :return: WebDriver instance.
    :raises ValueError: If an unsupported browser type is passed.
    """
    try:
        if browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Firefox(options=options)
            if proxy:
                options.add_argument(f"--proxy-server={proxy.proxy}")
        elif browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
            if proxy:
                options.add_argument(f"--proxy-server={proxy.proxy}")
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.get("http://localhost:8080/")  # Opens the local website
        return driver
    except Exception as e:
        raise RuntimeError(f"Failed to open {browser} browser: {e}")


@pytest.fixture(scope="module")
def driver(request, browser):
    """
    Fixture to initialize and yield the WebDriver instance with logging and event handling.

    :param request: Pytest request object.
    :param browser: Browser type passed as a parameter (chrome or firefox).
    :yield: EventFiringWebDriver instance.
    """
    logger, test_run_dir = setup_logging(request.module.__file__)
    logger.info(f"Starting test module: {request.module.__name__} with {browser} browser")

    driver = open_driver(browser)
    driver.implicitly_wait(request.config.getoption("--wait"))

    # Pass the logger and screenshot directory to the EventListener
    event_listener = EventListener(logger, test_run_dir)

    # Wrap the driver in EventFiringWebDriver to capture events
    event_driver = EventFiringWebDriver(driver, event_listener)

    yield event_driver

    logger.info(f"Finishing test module: {request.module.__name__} with {browser} browser")
    event_driver.quit()


@pytest.fixture(autouse=True)
def log_test_status(request):
    """
    Fixture that logs the start and end of each test automatically.

    :param request: Pytest request object to access test information.
    """
    driver = request.node.funcargs.get('driver')
    if hasattr(driver, '_listener'):
        logger = driver._listener.logger
        logger.info(f"Starting test: {request.node.name}")
        yield
        logger.info(f"Finishing test: {request.node.name}")
    else:
        yield


@pytest.fixture(scope="function")
def user_email():
    """
    Fixture to generate a fake user email for testing.

    :return: Fake email address.
    """
    return Faker().email()


@pytest.fixture(scope="function")
def user_password():
    """
    Fixture to generate a fake user password for testing.

    :return: Fake password.
    """
    return Faker().password()


def pytest_collection_modifyitems(items):
    """
    Ensures that the 'test_smoke' test is always run first by reordering the test list.

    :param items: List of collected test items.
    """
    for item in items:
        if "test_smoke" in item.name:
            items.insert(0, items.pop(items.index(item)))


def pytest_runtest_makereport(item, call):
    """
    Exits the test suite if 'test_smoke' fails, preventing the remaining tests from running.

    :param item: Test item object.
    :param call: Test call object to check for exceptions.
    """
    if "test_smoke" in item.name and call.excinfo is not None:
        pytest.exit("Smoke test failed, exiting the test suite.")
