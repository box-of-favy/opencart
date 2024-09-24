from locators import RegistrationPageLocators


class RegistrationPage:
    """
    Page Object class for user registration functionality.
    """

    def __init__(self, driver):
        """
        Initialize with a web driver.

        :param driver: Web driver instance.
        """
        self.driver = driver

    def click_my_account(self):
        """
        Clicks on the 'My Account' link in the top panel.
        """
        my_account = self.driver.find_element(*RegistrationPageLocators.ACCOUNT)
        my_account.click()

    def check_dropdown_links(self):
        """
        Checks for 'Register' and 'Login' links in the dropdown menu.

        :return: True if both links are present, False otherwise.
        """
        dropdown_menu = self.driver.find_element(*RegistrationPageLocators.DROPDOWN_MENU)
        register_link = dropdown_menu.find_element(*RegistrationPageLocators.REGISTER_LINK)
        login_link = dropdown_menu.find_element(*RegistrationPageLocators.LOGIN_LINK)
        return register_link is not None and login_link is not None

    def click_register(self):
        """
        Clicks on the 'Register' link in the dropdown menu.
        """
        register = self.driver.find_element(*RegistrationPageLocators.REGISTER_LINK)
        register.click()

    def fill_registration_form(self, first_name, last_name, email, telephone, password):
        """
        Fills out the registration form with the provided user data.

        :param first_name: User's first name.
        :param last_name: User's last name.
        :param email: User's email.
        :param telephone: User's telephone number.
        :param password: User's password.
        """
        self.driver.find_element(*RegistrationPageLocators.INPUT_FIRSTNAME).send_keys(first_name)
        self.driver.find_element(*RegistrationPageLocators.INPUT_LASTNAME).send_keys(last_name)
        self.driver.find_element(*RegistrationPageLocators.INPUT_EMAIL).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.INPUT_TELEPHONE).send_keys(telephone)
        self.driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.INPUT_CONFIRM).send_keys(password)

        # Accept privacy policy
        privacy_checkbox = self.driver.find_element(*RegistrationPageLocators.PRIVACY_CHECKBOX)
        privacy_checkbox.click()

        # Submit the registration form
        submit_button = self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def is_registration_successful(self):
        """
        Checks if the registration was successful.

        :return: True if the success message is displayed and URL is correct, False otherwise.
        """
        success_message = "Congratulations! Your new account has been successfully created!"
        return (success_message in self.driver.page_source and
                "route=account/success" in self.driver.current_url)

    def logout(self):
        """
        Logs out of the user account.

        :return: True if logout was successful, False otherwise.
        """
        self.click_my_account()
        logout_link = self.driver.find_element(*RegistrationPageLocators.LOGOUT_LINK)
        logout_link.click()
        return "route=account/logout" in self.driver.current_url

    def login(self):
        """
        Logs into the user account.

        :return: True if login was successful, False otherwise.
        """
        self.click_my_account()
        login = self.driver.find_element(*RegistrationPageLocators.LOGIN_LINK_IN_ACCOUNT)
        login.click()
        return "route=account/login" in self.driver.current_url
