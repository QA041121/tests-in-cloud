import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_object.product_page_page_object import ProductPage
from page_object.shopping_cart_page_object import CartPage


class ShoppingCartTest(unittest.TestCase):
    driver = None
    product_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.hp_product_page = ProductPage(cls.driver, '47')
        cls.samsung_product_page = ProductPage(cls.driver, '33')
        cls.cart_page = CartPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_to_cart(self):
        self.samsung_product_page.open()
        self.samsung_product_page.clear_quantity_field()
        self.samsung_product_page.set_quantity("2")
        self.samsung_product_page.click_add_to_cart_button()
        self.assertEqual('Success: You have added Samsung SyncMaster 941BW to your shopping cart!\n×',
                         self.samsung_product_page.get_success_alert())

        self.hp_product_page.open()
        self.hp_product_page.click_add_to_cart_button()
        self.assertEqual('Success: You have added HP LP3065 to your shopping cart!\n×',
                         self.hp_product_page.get_success_alert())

    def test_delete_from_cart(self):
        self.cart_page.open()
        self.assertEqual(('Samsung SyncMaster 941BW', 'HP LP3065'), self.cart_page.get_product_name())
        self.cart_page.click_remove_button()
        self.cart_page.click_remove_button()
        self.assertEqual('Your shopping cart is empty!',
                         self.cart_page.get_products_is_absent_text())

