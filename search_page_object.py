from dataclasses import dataclass
from decimal import Decimal
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from base_page_object import BasePage


def extract_decimal_price(text: str) -> str:
    split_by_lines: list[str] = text.split("\n")
    first_price_lines = split_by_lines[0].split(' ')
    first_price = first_price_lines[0]
    return first_price


class SearchPage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/search'

    def get_search_field(self)-> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'input-lg')

    def search_in_search_field(self, keyword: str) -> None:
        self.get_search_field().send_keys(keyword)

    def clear_search_field(self) -> None:
        self.get_search_field().clear()

    def click_search_button(self) -> None:
        button = self.driver.find_element(By.CLASS_NAME, "btn-default")
        button.click()

    def get_search_criteria_field(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-search")

    def search_in_search_criteria_field(self, keyword: str) -> None:
        self.get_search_criteria_field().send_keys(keyword)

    def clear_search_criteria_field(self) -> None:
        self.get_search_criteria_field().clear()

    def click_search_criteria_button(self) -> None:
        search_button = self.driver.find_element(By.ID, "button-search")
        search_button.click()

    def check_checkbox(self) -> None:
        # search in product descriptions checkbox
        checkbox = self.driver.find_element(By.ID, "description")
        checkbox.click()

    def get_name(self) -> str:
        return self.driver.find_element(By.XPATH, '//h4/a').text

    def get_price(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, 'price-new').text

    def get_price_sony(self) -> str:
        price = self.driver.find_element(By.CLASS_NAME, 'price').text
        return extract_decimal_price(price)

    def get_text_absent_result(self) -> str:
        return self.driver.find_element(By.XPATH, '(//p)[3]').text

    def get_result_hp(self) -> str:
        return self.driver.find_element(By.XPATH, '(//h4)[1]/a').text

    def get_result_mac(self) -> str:
        return self.driver.find_element(By.XPATH, '(//h4)[2]/a').text
