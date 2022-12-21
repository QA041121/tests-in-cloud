import unittest
from page_object.product_page_page_object import ProductPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ProductPageTest(unittest.TestCase):
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

    def test_product_name(self):
        product_name = self.product_page.get_name()
        self.assertEqual('Apple Cinema 30"', product_name)

    def test_product_brand(self):
        product_brand = self.product_page.get_brand()
        self.assertEqual('Apple', product_brand)

    def test_product_code(self):
        product_code = self.product_page.get_product_code()
        self.assertEqual('Product 15', product_code)

    def test_product_price(self):
        product_price = self.product_page.get_price()
        self.assertEqual('$110.00', product_price)

    def test_description(self):
        product_description = self.product_page.get_description()
        self.assertIn(
            'The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution.',
            product_description
        )
