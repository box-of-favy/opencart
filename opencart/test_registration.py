from pages import RegistrationPage


class TestRegistration:
    """
    Test cases for user registration.
    """

    def test_my_account(self, driver):
        """
        Tests clicking the 'My Account' link in the top panel.

        :param driver: WebDriver instance initialized by the fixture.
        """
        registration_page = RegistrationPage(driver)
        registration_page.click_my_account()

    def test_dropdown(self, driver):
        """
        Tests the presence of 'Register' and 'Login' links in the dropdown menu.

        :param driver: WebDriver instance initialized by the fixture.
        """
        registration_page = RegistrationPage(driver)
        assert registration_page.check_dropdown_links(), "Register or Login link is not present in the dropdown menu"

    def test_register(self, driver):
        """
        Tests clicking the 'Register' link.

        :param driver: WebDriver instance initialized by the fixture.
        """
        registration_page = RegistrationPage(driver)
        registration_page.click_register()

    def test_input(self, driver, user_email, user_password):
        """
        Tests the user registration form by inputting user details.

        :param driver: WebDriver instance initialized by the fixture.
        :param user_email: Generated email for testing.
        :param user_password: Generated password for testing.
        """
        registration_page = RegistrationPage(driver)
        registration_page.fill_registration_form('John', 'Doe', user_email, '1234567890', user_password)
        assert registration_page.is_registration_successful(), "Account registration failed"

    def test_logout(self, driver):
        """
        Tests logging out of the user account.

        :param driver: WebDriver instance initialized by the fixture.
        """
        registration_page = RegistrationPage(driver)
        assert registration_page.logout(), "Logout failed"

    def test_login(self, driver):
        """
        Tests logging into the user account.

        :param driver: WebDriver instance initialized by the fixture.
        """
        registration_page = RegistrationPage(driver)
        assert registration_page.login(), "Login failed"
