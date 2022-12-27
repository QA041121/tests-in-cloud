import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_object.product_page_page_object import ProductPage
from page_object.product_comparison_page_object import ComparePage


class CompareTest(unittest.TestCase):
    driver = None
    product_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.apple_product_page = ProductPage(cls.driver, '42')
        cls.samsung_product_page = ProductPage(cls.driver, '33')
        cls.compare_page = ComparePage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_to_compare(self):
        self.apple_product_page.open()
        self.apple_product_page.click_compare_button()
        alert = self.apple_product_page.get_success_alert()
        self.assertEqual('Success: You have added Apple Cinema 30" to your product comparison!\n×', alert)

        self.samsung_product_page.open()
        self.samsung_product_page.click_compare_button()
        alert = self.samsung_product_page.get_success_alert()
        self.assertEqual('Success: You have added Samsung SyncMaster 941BW to your product comparison!\n×', alert)
        self.samsung_product_page.click_product_comparison_link()
        self.assertEqual(['Apple Cinema 30"', 'Samsung SyncMaster 941BW'], self.compare_page.get_product_name())

    def test_compare(self):
        self.compare_page.click_remove_button()
        self.compare_page.click_remove_button()
        self.assertEqual(
            'You have not chosen any products to compare.', self.compare_page.get_products_is_absent_text()
        )
