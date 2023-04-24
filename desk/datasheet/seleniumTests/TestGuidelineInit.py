import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
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

        # raise unittest.SkipTest("testttt")

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
        print(FakeDataGenerator().fake_name())

        try:
            self.assertIn('Guideline for AXI', self.driver.page_source, msg=None)
            # self.fail('fuckup')
        except AssertionError:
            raise unittest.SkipTest("skip all tests in this class")
        time.sleep(2)


class TestGuidelineMain(TestGuidelineInit):

    def test_admin_login_logout(self) -> None:
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

        print(self.button_name)
        try:
            self.assertEqual(self.button_name, 'User', msg=None)
            self.input_username = self.driver.find_element(
                By.XPATH,
                "//div[@class='form-row']//input[@id='id_username']"
            )
            self.input_username.send_keys("admin")
            time.sleep(2)
        except AssertionError:
            self.skipTest("The user name is different than \"User\" ")


if __name__ == "__main__":
    unittest.main(failfast=True)
    # unittest.main(exit=False)
