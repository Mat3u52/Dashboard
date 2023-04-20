import unittest
from selenium import webdriver
from FakeDataGenerator import FakeDataGenerator


class TestGuidelineMain(unittest.TestCase, FakeDataGenerator):

    # def __init__(self) -> None:
    #     """
    #     Instance of fake data generator.
    #     :return:
    #     """
    #     super().__init__()

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

    def test_initializer(self) -> None:
        """
        Verify webpage.
        :return: Webpage "desk"
        :rtype: None
        """
        # FakeDataGenerator().fake_name()
        self.fake_name()
        self.assertIn('Guideline for AXI', self.driver.page_source, msg=None)

    # def test_admin_login_logout(self) -> None:
    #     """
    #     Verify tak user is login as admin or not
    #     :return: admin panel
    #     :rtype: None
    #     """
    #     pass


    def tearDown(self) -> None:
        """
        CleanUp
        :return: Close the  handler
        :rtype: None
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
