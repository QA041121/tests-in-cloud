import unittest

from search_page_object import SearchPage
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
        self.search_page.search_in_search_field('apple')
        self.search_page.click_search_button()
        result_name = self.search_page.get_name()
        result_price = self.search_page.get_price()
        self.assertEqual('Apple Cinema 30"', result_name)
        self.assertEqual('$110.00', result_price)

    def test_search_sony(self):
        self.search_page.clear_search_field()
        self.search_page.search_in_search_field('sony')
        self.search_page.click_search_button()
        result_name = self.search_page.get_name()
        result_price = self.search_page.get_price_sony()
        self.assertEqual('Sony VAIO', result_name)
        self.assertEqual('$1,202.00', result_price)

    def test_search_nokia(self):
        self.search_page.clear_search_field()
        self.search_page.search_in_search_field('nokia')
        self.search_page.click_search_button()
        result = self.search_page.get_text_absent_result()
        self.assertEqual('There is no product that matches the search criteria.', result)

    def test_search_criteria(self):
        self.search_page.clear_search_criteria_field()
        self.search_page.search_in_search_criteria_field('stunning')
        self.search_page.check_checkbox()
        self.search_page.click_search_criteria_button()
        self.assertEqual('HP LP3065', self.search_page.get_result_hp())
        self.assertEqual('iMac', self.search_page.get_result_mac())



