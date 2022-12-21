import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_object.product_page_page_object import ProductPage


class AddReviewTest(unittest.TestCase):
    driver = None
    product_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.product_page = ProductPage(cls.driver, '42')
        cls.product_page.open()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_submit_empty_form(self):
        self.product_page.click_review_tab()
        self.product_page.click_continue_button()
        self.assertEqual('Warning: Please select a review rating!', self.product_page.wait_warning_alert().text)

    def test_submit_form_with_insufficient_characters(self):
        self.product_page.click_review_tab()
        self.product_page.set_rating(4)
        self.product_page.fill_name_field('John')
        self.product_page.fill_review_field('test 24 characters limit')
        self.product_page.click_continue_button()
        self.product_page.wait_alert_disappear()
        self.assertEqual(
            'Warning: Review Text must be between 25 and 1000 characters!', self.product_page.wait_warning_alert().text
        )

    def test_submit_correct_form(self):
        self.product_page.click_review_tab()
        self.product_page.fill_name_field('John')
        self.product_page.fill_review_field('type more than 25 characters limit')
        self.product_page.set_rating(4)
        self.product_page.click_continue_button()
        self.assertEqual(
            'Thank you for your review. It has been submitted to the webmaster for approval.',
            self.product_page.get_success_alert()
        )
