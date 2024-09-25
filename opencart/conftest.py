import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.events import EventFiringWebDriver
from utils import setup_logging, EventListener, proxy_utils, log_http_requests


BROWSERMOB_PROXY_PATH = (r"C:\Users\favy\Documents\work\browsermob-proxy-2.1.4\bin"
                         r"\browsermob-proxy.bat")


def pytest_addoption(parser):
    """
    Adds custom command-line options for specifying the browser type and implicit wait time.

    :param parser: Parser object to add options.
    """
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to use for tests: chrome, firefox, or both")
    parser.addoption("--wait", action="store", default=10, type=int,
                     help="Implicit wait time for the browser")
    parser.addoption("--proxy-port", action="store", default=8081, type=int,
                     help="Port for the BrowserMob proxy (default: 8081)")


def open_driver(browser, proxy=None):
    """
    Opens the browser driver based on the specified browser.

    :param browser: The browser type to open (chrome or firefox).
    :param proxy: The proxy to use for intercepting HTTP requests (optional).
    If None, no proxy is used.
    :return: WebDriver instance.
    :raises ValueError: If an unsupported browser type is passed.
    """

    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        if proxy:
            options.add_argument(f"--proxy-server={proxy.proxy}")
        driver = webdriver.Firefox(options=options)
    elif browser == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-maximized")
        if proxy:
            options.add_argument(f"--proxy-server={proxy.proxy}")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("http://localhost:8080/")  # Opens the local website
    return driver


@pytest.fixture(scope="module")
def driver(request):
    """
    Fixture to initialize and yield the WebDriver instance with logging and event handling.

    :param request: Pytest request object.
    :param browser: Browser type passed as a parameter (chrome or firefox).
    :yield: EventFiringWebDriver instance.
    """
    browser = request.config.getoption("--browser")
    proxy_port = request.config.getoption("--proxy-port")

    # Set up logging
    logger, test_run_dir = setup_logging(request.module.__file__)
    logger.info(f"Starting test module: {request.module.__name__} with {browser} browser")

    # Start proxy session and capture HTTP traffic
    proxy, server, har_file_path = proxy_utils.start_proxy_session(test_run_dir, port=proxy_port)

    # Set up the WebDriver
    driver_instance = open_driver(browser, proxy)
    driver_instance.implicitly_wait(request.config.getoption("--wait"))

    # Pass the logger and screenshot directory to the EventListener
    event_listener = EventListener(logger, test_run_dir, proxy)

    # Wrap the driver in EventFiringWebDriver to capture events
    event_driver = EventFiringWebDriver(driver_instance, event_listener)

    # Store logger, test_run_dir, and proxy as attributes of event_driver
    event_driver.logger = logger
    event_driver.test_run_dir = test_run_dir
    event_driver.proxy = proxy

    yield event_driver

    # Log HTTP requests
    log_http_requests(proxy, logger)

    # Ensure that the driver is quit and the proxy is stopped
    try:
        event_driver.quit()
        logger.info(f"Driver for {browser} browser quit successfully.")
    except Exception as e:
        logger.error(f"Error quitting driver for {browser}: {e}")

    # Stop proxy and save HAR file
    try:
        proxy_utils.stop_proxy(proxy, server, har_file_path)
        logger.info("Proxy stopped successfully.")
    except Exception as e:
        logger.error(f"Error stopping proxy: {e}")

    logger.info(f"Finishing test module: {request.module.__name__} with {browser} browser")


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
