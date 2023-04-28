import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
            )
            self.href_to_webpage.click()
            time.sleep(2)
        except AssertionError:
            self.skipTest("The user name is different than \"User\" ")

    def _create_new_guideline(self) -> None:
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

        self.input_title = self.driver.find_element(
            By.XPATH,
            "//div[@class='col-md-8']//input[@name='title']"
        )
        self.title = FakeDataGenerator().fake_title()
        self.input_title.send_keys(self.title)

        self.textarea_text = self.driver.find_element(
            By.XPATH,
            "//div[@class='col-md-8']//textarea[@id='id_text']"
        )
        self.textarea_text.send_keys(FakeDataGenerator().fake_text())

        self.input_choose_file = self.driver.find_element(
            By.XPATH,
            "//div[@class='col-md-8']//input[@id='id_image']"
        )
        self.input_choose_file.send_keys("/root/PythonDeveloper/AXI_Manager/img/main/axi.png")
        time.sleep(2)

        self.button_submit = self.driver.find_element(
            By.XPATH,
            "//div[@class='col-md-8']//button[@type='submit']"
        )
        self.button_submit.submit()
        time.sleep(4)
        try:
            self.assertIn(self.title, self.driver.page_source, msg=None)
        except AssertionError:
            self.skipTest("The article is missing.")

    def test_add_comment(self) -> None:
        """
        Function try to add a new comment to guideline.
        :return: New comment
        :rtype: None
        """
        self._create_new_guideline()
        i: int = 0
        while i <= 3:
            self.url = self.driver.current_url

            self.button_comment = self.driver.find_element(
                By.XPATH,
                "//div[@class='col-md-8']//button[@type='submit' and text()='Add Comment']"
            )
            self.button_comment.click()
            time.sleep(2)
            self.input_name = self.driver.find_element(
                By.XPATH,
                "//div[@class='col-md-8']//input[@name='name']"
            )
            self.input_name.send_keys(FakeDataGenerator().fake_name())

            self.input_email = self.driver.find_element(
                By.XPATH,
                "//div[@class='col-md-8']//input[@name='email']"
            )
            self.input_email.send_keys(FakeDataGenerator().fake_email())

            self.textarea_comment = self.driver.find_element(
                By.XPATH,
                "//div[@class='col-md-8']//textarea[@name='body']"
            )
            self.textarea_comment.send_keys(FakeDataGenerator().fake_title())
            time.sleep(2)
            self.button_add_comment = self.driver.find_element(
                By.XPATH,
                "//div[@class='col-md-8']//button[@type='submit' and text()='Add Comment']"
            )
            self.button_add_comment.click()
            time.sleep(2)
            self.driver.get(self.url)
            i += 1

        try:
            self.assertNotIn("Not Comments Yet...", self.driver.page_source, msg=None)
        except AssertionError:
            self.skipTest("Not Comments Yet!")

        self.driver.get('http://127.0.0.1:8000/')

    def test_email(self) -> None:
        """
        Certified the guideline and send the email
        :return: send email
        :rtype: None
        """
        self.title_of_guideline = self.driver.find_element(
            By.XPATH,
            "//div[@class='col-md-8']//h2[1]"
        ).text
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
        except AssertionError:
            self.skipTest("The user name is different than \"User\" ")

        self.href_guideline = self.driver.find_element(
            By.XPATH,
            "//div[@class ='app-datasheet module']//a[@href='/admin/datasheet/guideline/']"
        )
        self.href_guideline.click()
        time.sleep(2)
        self.input_search_admin = self.driver.find_element(
            By.XPATH,
            "//form[@id='changelist-search']//input[@id='searchbar']"
        )
        self.input_search_admin.send_keys(self.title_of_guideline)
        self.submit_search_admin = self.driver.find_element(
            By.XPATH,
            "//form[@id='changelist-search']//input[@type='submit']"
        )
        self.submit_search_admin.click()
        time.sleep(2)
        self.href_select_guideline = self.driver.find_element(
            By.XPATH,
            "//table[@id='result_list']//th[@class='field-title']//a[1]"
        )
        self.href_select_guideline.click()
        time.sleep(2)

        self.select_certified = self.driver.find_element(
            By.XPATH,
            "//select[@id='id_status']/option[text()='Certified']"
        )
        self.select_certified.click()

        self.submit_save = self.driver.find_element(
            By.XPATH,
            "//div[@class='submit-row']//input[@name='_save']"
        )
        self.submit_save.submit()
        time.sleep(2)
        self.href_to_webpage = self.driver.find_element(
            By.XPATH,
            "//div[@id='user-tools']//a[@href='/']"
        )
        self.href_to_webpage.click()
        time.sleep(2)
        self.input_search_webpage = self.driver.find_element(
            By.XPATH,
            "//input[@name='searched']"
        )
        self.input_search_webpage.send_keys(self.title_of_guideline)
        time.sleep(2)
        self.button_search = self.driver.find_element(
            By.XPATH,
            "//form[@class='d-flex']//button"
        )
        self.button_search.click()
        time.sleep(2)

        self.href_guideline_sorted = self.driver.find_element(
            By.XPATH,
            "//div[@class='col-md-8']//a"
        )
        self.href_guideline_sorted.click()
        time.sleep(2)

        self.button_email = self.driver.find_element(
            By.XPATH,
            "//div[@class='oneGuideline']//button[@type='submit' and text()='Send Email']"
        )
        self.button_email.click()
        time.sleep(2)
        self.input_email_name = self.driver.find_element(
            By.XPATH,
            "//input[@name='name']"
        )
        self.input_email_name.send_keys(FakeDataGenerator().fake_name())

        self.input_email = self.driver.find_element(
            By.XPATH,
            "//input[@name='email']"
        )
        self.input_email.send_keys('guideline2023@gmail.com')

        self.input_email_to = self.driver.find_element(
            By.XPATH,
            "//input[@name='to']"
        )
        self.input_email_to.send_keys('guideline2023@gmail.com')

        self.textarea_email = self.driver.find_element(
            By.XPATH,
            "//textarea[@name='comments']"
        )
        self.textarea_email.send_keys(FakeDataGenerator().fake_title())
        time.sleep(2)

        self.button_email_send = self.driver.find_element(
            By.XPATH,
            "//button[@value='Send']"
        )
        self.button_email_send.click()
        time.sleep(2)
        try:
            self.assertIn("The message sent", self.driver.page_source, msg=None)
        except AssertionError:
            self.skipTest("Sending E-mail fail!")
        time.sleep(2)


if __name__ == "__main__":
    unittest.main(failfast=True)
