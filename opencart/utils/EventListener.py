from selenium.webdriver.support.events import AbstractEventListener


class EventListener(AbstractEventListener):
    def __init__(self, logger, screenshot_dir, proxy=None):
        self.logger = logger
        self.screenshot_dir = screenshot_dir
        self.proxy = proxy

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")
        if self.proxy:
            self.proxy.new_har("new_request")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"Navigated to {url}")
        if self.proxy:
            self.logger.info(f"HTTP requests: {self.proxy.har}")

    def on_exception(self, exception, driver):
        self.logger.error(f"Exception occurred: {exception}")
        # Save a screenshot when an exception occurs
        driver.save_screenshot(self.screenshot_dir + "/exception_screenshot.png")

    def get_logger(self):
        return self.logger