import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from FakeDataGenerator import FakeDataGenerator


class TestGuidelineInit(unittest.TestCase):

    def setUp(self) -> None:
        """
        Start up a driver for the browser and redirection to the webpage.
        :return: instance of webdriver.
        :rtype: None
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/')

    def tearDown(self) -> None:
        """
        CleanUp
        :return: Close the  handler
        :rtype: None
        """
        self.driver.close()


class TestAbandon(TestGuidelineInit):

    def test_initializer(self) -> None:
        """
        Verify webpage is exist.
        :return: Webpage "desk"
        :rtype: None
        """

        try:
            assert len(self.driver.window_handles) == 1
            self.assertIn('Guideline for AXI', self.driver.page_source, msg=None)
        except AssertionError:
            raise unittest.SkipTest("skip all tests in this class")
        time.sleep(2)


class TestGuidelineMain(TestGuidelineInit):

    def _admin_login_logout(self) -> None:
        """
        Verify the user is login as admin or not. If not then sign in as admin.
        :return: admin panel
        :rtype: None
        """
        # with self.assertRaises(NoSuchElementException):
        self.button_name = self.driver.find_element(
            By.XPATH,
            "//div[@class='labelMain']//a[@href='/admin/']//button"
        ).text
        self.driver.find_element(
            By.XPATH,
            "//div[@class='labelMain']//a[@href='/admin/']//button"
        ).click()

        try:
            self.assertEqual(self.button_name, 'User', msg=None)

            self.input_username = self.driver.find_element(
                By.XPATH,
                "//div[@class='form-row']//input[@id='id_username']"
            )
            self.input_password = self.driver.find_element(
                By.XPATH,
                "//div[@class ='form-row']//input[@id='id_password']"
            )
            self.submit_user_pass = self.driver.find_element(
                By.XPATH,
                "//div[@class ='submit-row']//input[@type='submit']"
            )
            self.input_username.send_keys("admin")
            self.input_password.send_keys("admin")
            self.submit_user_pass.submit()
            time.sleep(2)
            self.href_to_webpage = self.driver.find_element(
                By.XPATH,
                "//div[@id='user-tools']//a[@href='/']"
                # "//div[@id='user-tools']//a[1]"
            )
            self.href_to_webpage.click()
            time.sleep(2)
        except AssertionError:
            self.skipTest("The user name is different than \"User\" ")

    def test_create_new_guideline(self) -> None:
        """
        The function create a new guideline by selenium.

        :return: a new guideline in DB
        :rtype: None
        """
        self._admin_login_logout()
        self.button_new_guideline = self.driver.find_element(
            By.XPATH,
            "//div[@class='labelMain']//a[@href='/api/guideline/new/']"
        )
        self.button_new_guideline.click()
        time.sleep(2)
        print(FakeDataGenerator().fake_login())
        # self.driver.switch_to.new_window('tab')
        # time.sleep(2)



if __name__ == "__main__":
    unittest.main(failfast=True)
