from dataclasses import dataclass
from decimal import Decimal
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from .base_page_object import BasePage


@dataclass
class Product:
    name: str
    price: str


def extract_decimal_price(text: str) -> str:
    split_by_lines: List[str] = text.split("\n")
    first_price_lines = split_by_lines[0].split(' ')
    first_price = first_price_lines[0]
    return first_price


class SearchPage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/search'

    def get_search_field(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'input-lg')

    def input_search_query(self, keyword: str) -> None:
        self.get_search_field().send_keys(keyword)

    def clear_search_field(self) -> None:
        self.get_search_field().clear()

    def click_search_button(self) -> None:
        button = self.driver.find_element(By.CLASS_NAME, "btn-default")
        button.click()

    def get_search_criteria_field(self) -> WebElement:
        return self.driver.find_element(By.ID, "input-search")

    def input_search_criteria_field(self, keyword: str) -> None:
        self.get_search_criteria_field().send_keys(keyword)

    def clear_search_criteria_field(self) -> None:
        self.get_search_criteria_field().clear()

    def click_search_criteria_button(self) -> None:
        search_button = self.driver.find_element(By.ID, "button-search")
        search_button.click()

    # def toggle_search_in_subcategories_checkbox(self) -> None:

    def toggle_search_in_description_checkbox(self) -> None:
        """search in product descriptions checkbox"""
        checkbox = self.driver.find_element(By.ID, "description")
        checkbox.click()

    def get_text_absent_result(self) -> str:
        return self.driver.find_element(By.XPATH, '(//p)[3]').text

    # TODO:
    # См. лекцию про извлечение структурированных данных
    # def get_products(self) -> list[Product]:
    # all_product_cards = self.driver.find_elements(By.CLASS_NAME, "product_layout")
    # products: list[Product] = []
    # for product_card in all_products_cards:
    #     name = product_card.find_element(By.TAG, "h4").text
    #     descr = product_card.find_element(By.TAG, "p").text
    #     price = ...
    #     products.append(Product(name, descr, price))
    # return products

    def get_products(self) -> list[Product]:
        all_product_cards = self.driver.find_elements(By.CLASS_NAME, "product-layout")
        products: list[Product] = []
        for product_card in all_product_cards:
            name = product_card.find_element(By.TAG_NAME, "h4").text
            price = extract_decimal_price(product_card.find_element(By.CLASS_NAME, 'price').text)
            products.append(Product(name, price))
        return products
