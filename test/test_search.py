import unittest

from page_object.search_page_object import SearchPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SearchPageTest(unittest.TestCase):
    driver = None
    search_page = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.search_page = SearchPage(cls.driver)
        cls.search_page.open()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_search_apple(self):
        self.search_page.input_search_query('apple')
        self.search_page.click_search_button()
        result_name = self.search_page.get_name()
        result_price = self.search_page.get_price()
        self.assertEqual('Apple Cinema 30"', result_name)
        self.assertEqual('$110.00', result_price)

    def test_search_sony(self):
        self.search_page.clear_search_field()
        self.search_page.input_search_query('sony')
        self.search_page.click_search_button()
        result_name = self.search_page.get_name()
        result_price = self.search_page.get_price()
        self.assertEqual('Sony VAIO', result_name)
        self.assertEqual('$1,202.00', result_price)

    def test_search_nokia(self):
        self.search_page.clear_search_field()
        self.search_page.input_search_query('nokia')
        self.search_page.click_search_button()
        result = self.search_page.get_text_absent_result()
        self.assertEqual('There is no product that matches the search criteria.', result)

    def test_search_criteria(self):
        self.search_page.clear_search_criteria_field()
        self.search_page.input_search_criteria_field('stunning')
        self.search_page.toggle_search_in_description_checkbox()
        self.search_page.click_search_criteria_button()
        self.assertEqual('HP LP3065', self.search_page.get_result_hp())
        self.assertEqual('iMac', self.search_page.get_result_mac())

        # self.assertEqual("HP", products[0].name)
        # self.assertEqual("iMac", products[1].name)

        # self.assertEqual(
        #    ["HP", "iMac"],
        #    [products[0].name, products[1].name]
        # )
