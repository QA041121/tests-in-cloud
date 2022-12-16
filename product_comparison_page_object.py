from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from base_page_object import BasePage


class ComparePage(BasePage):

    def get_product_name(self) -> tuple[str, str]:
        elements = self.driver.find_elements(By.XPATH, '//td/a/strong')
        name1 = elements[0].text
        name2 = elements[1].text
        return name1, name2

    def click_remove_button(self) -> None:
        self.driver.find_element(By.CLASS_NAME, 'btn-danger').click()

    def get_products_is_absent_text(self) -> str:
        return self.driver.find_element(By.XPATH, '//div[@id ="content"]/p').text
