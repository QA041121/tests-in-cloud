from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from .base_page_object import BasePage


class CartPage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=checkout/cart'

    def get_product_name(self) -> list[str]:
        elements: list[WebElement] = self.driver.find_elements(By.XPATH, '//tbody/tr/td[2]/a')
        names: list[str] = []
        for name in elements:
            names.append(name.text)
        return names


    def get_total_price(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '(//tbody/tr[4]/td[2])[2]')

    def click_remove_button(self) -> None:
        remove_button = self.driver.find_element(By.XPATH, '//button[@class="btn btn-danger"]')
        remove_button.click()
        WebDriverWait(self.driver, 30).until(EC.staleness_of(remove_button))

    def get_products_is_absent_text(self) -> str:
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="content"]/p'))).text
