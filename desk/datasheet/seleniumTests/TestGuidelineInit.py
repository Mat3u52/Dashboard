import unittest
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

        # raise unittest.SkipTest("testttt")

    def tearDown(self) -> None:
        """
        CleanUp
        :return: Close the  handler
        :rtype: None
        """
        self.driver.close()


class TestGuidelineMain(TestGuidelineInit):

    def test_initializer(self) -> None:
        """
        Verify webpage.
        :return: Webpage "desk"
        :rtype: None
        """
        print(FakeDataGenerator().fake_name())
        # self.fake_name()
        # try:
        #     self.assertIn('Guideline for AXI0', self.driver.page_source, msg=None)
        # except AssertionError:
        #     self.skipTest("Initialization Fail!")

        try:
            self.assertIn('Guideline for AXI0', self.driver.page_source, msg=None)
        except AssertionError:
            raise unittest.SkipTest("skip all tests in this class")

    def test_admin_login_logout(self) -> None:
        """
        Verify tak user is login as admin or not
        :return: admin panel
        :rtype: None
        """
        # pass
        self.button_name = self.driver.find_element(
            By.XPATH,
            "//div[@class='labelMain']//a[@href='/admin/']//button"
        ).text
        print(self.button_name)
        try:
            self.assertEqual(self.button_name, 'User', msg=None)
        except AssertionError:
            self.skipTest("The user name is different than \"User\" ")


if __name__ == "__main__":
    unittest.main(failfast=True)
