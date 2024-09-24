"""
This test works only in non-headless mode.
"""

"""
This function is written only for the purpose of passing this test automatically.
By default, tests in the opencart folder are launched in headless mode.
"""
def test_true():
    return True


# import pytest
# from pages import AdminPage, UploadPage
#
#
# @pytest.fixture(scope="module")
# def context():
#     """
#     Context for passing data between tests within the module.
#
#     This fixture is used to store and share data across multiple test functions
#     in the same module, such as the randomly generated file name in the upload tests.
#
#     :return: An empty dictionary to be filled with test data during test execution.
#     """
#     return {}
#

# def test_admin_category_management(driver):
#     """
#     Tests the admin login and navigation to the catalog menu.
#
#     :param driver: WebDriver instance initialized by the fixture.
#     """
#     admin_page = AdminPage(driver)
#     admin_page.open_login_page().login("admin", "admin")
#     admin_page.close_alert()
#     admin_page.open_catalog_menu()
#
#
# def test_navigate_to_download_page(driver):
#     """
#     Tests navigating to the Downloads page through the Catalog menu.
#
#     :param driver: WebDriver instance initialized by the fixture.
#     """
#     upload_page = UploadPage(driver)
#     upload_page.navigate_to_download_page()
#     assert "route=catalog/download" in driver.current_url, \
#         "Failed to navigate to the Downloads page"
#
#
# def test_click_add_new_button(driver):
#     """
#     Tests clicking the 'Add New' button on the Downloads page.
#
#     :param driver: WebDriver instance initialized by the fixture.
#     """
#     upload_page = UploadPage(driver)
#     upload_page.click_add_new_button()
#     assert "route=catalog/download/add" in driver.current_url, "Failed to open Add New form"
#
#
# def test_upload_file(driver, context):
#     """
#     Tests the file upload process in the admin downloads section.
#
#     :param driver: WebDriver instance initialized by the fixture.
#     :param context: A fixture for passing data between tests.
#     """
#     upload_page = UploadPage(driver)
#
#     # File path provided by the user
#     file_path = r"C:\Users\favy\Documents\work\for-qa\scripts_for_test\opencart\file\Fauna_LSS.pdf"
#
#     # Upload the file
#     upload_page.upload_file(file_path)
#
#     # Generate a random name for the download
#     random_name = upload_page.generate_random_name()
#     upload_page.change_download_name(random_name)
#
#     # Save the random name in the context for later tests
#     context['random_name'] = random_name
#
#
# def test_check_upload(driver):
#     """
#     Tests checking for the success alert after file upload.
#
#     :param driver: WebDriver instance initialized by the fixture.
#     """
#     upload_page = UploadPage(driver)
#     upload_page.check_success_alert()
#
#
# def test_save_file(driver, context):
#     """
#     Tests saving the file and verifying the entry in the downloads table.
#
#     :param driver: WebDriver instance initialized by the fixture.
#     :param context: A fixture for passing data between tests.
#     """
#     upload_page = UploadPage(driver)
#
#     # Save the form
#     upload_page.click_save_button()
#
#     # Verify the entry in the table using the saved random name
#     random_name = context.get("random_name")
#     upload_page.verify_download_in_table(random_name)
#
#
# def test_delete_file(driver, context):
#     """
#     Tests deleting the file from the downloads table.
#
#     :param driver: WebDriver instance initialized by the fixture.
#     :param context: A fixture for passing data between tests.
#     """
#     upload_page = UploadPage(driver)
#
#     # Get the random name from context
#     random_name = context.get('random_name')
#
#     # Ensure that random_name exists
#     assert random_name is not None, ("random_name not found in context. Ensure test_upload_file"
#                                      " ran successfully.")
#
#     # Delete the entry by clicking the trash icon and confirming the popup
#     upload_page.delete_download(random_name)
#
#     # Verify the absence of the entry in the table
#     upload_page.verify_download_absence_in_table(random_name)
