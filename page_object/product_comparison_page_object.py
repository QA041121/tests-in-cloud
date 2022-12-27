from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from .base_page_object import BasePage


class ComparePage(BasePage):

    def get_product_name(self) -> list[str]:
        elements = self.driver.find_elements(By.XPATH, '//td/a/strong')
        names: list[str] = []
        for name in elements:
            names.append(name.text)
        return names

    def click_remove_button(self) -> None:
        button = WebDriverWait(self.driver, 10).until(
            visibility_of_element_located((By.CLASS_NAME, 'btn-danger'))
        )
        button.click()

    def get_products_is_absent_text(self) -> str:
        return self.driver.find_element(By.XPATH, '//div[@id ="content"]/p').text
