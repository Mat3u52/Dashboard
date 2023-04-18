import unittest
from selenium import webdriver


class TestGuideline(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_run(self) -> None:
        self.driver.get('http://127.0.0.1:8000/')
        self.assertIn('Guideline for AXI', self.driver.page_source, msg=None)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()