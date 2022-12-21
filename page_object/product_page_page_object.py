from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from .base_page_object import BasePage


class ProductPage(BasePage):

    def __init__(self, driver: WebDriver, product_id: str):
        super().__init__(driver)
        self.product_id = product_id

    def get_url(self) -> str:
        return f'http://54.183.112.233/index.php?route=product/product&product_id={self.product_id}'

    def get_name(self) -> str:
        return self.driver.find_element(By.TAG_NAME, 'h1').text

    def get_brand(self) -> str:
        return self.driver.find_element(By.XPATH, '(//ul[@class = "list-unstyled"])[8]/li/a').text

    def get_product_code(self) -> str:
        product_code_line = self.driver.find_element(By.XPATH, '//li[contains(text(),"Product Code:")]').text
        return product_code_line.split("Product Code: ")[1]

    def get_price(self) -> str:
        return self.driver.find_element(By.XPATH, '(//ul[@class = "list-unstyled"])[9]/li/h2').text

    def get_description(self) -> str:
        return self.driver.find_element(By.XPATH, '(//font[@face="Helvetica"])[1]').text

    def click_review_tab(self) -> None:
        self.driver.find_element(By.XPATH, '//a[contains(text(), "Reviews")]').click()

    def click_continue_button(self) -> None:
        self.driver.find_element(By.ID, 'button-review').click()

    def wait_warning_alert(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger')))

    def wait_alert_disappear(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(EC.staleness_of(self.wait_warning_alert()))

    def get_success_alert(self) -> str:
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'alert-success'))
        ).text

    def set_rating(self, value: int) -> None:
        self.driver.find_element(By.XPATH, f'//input[@value = "{value}"]').click()

    def clear_name_field(self) -> None:
        raise NotImplementedError()

    def clear_review_field(self) -> None:
        raise NotImplementedError()

    def fill_name_field(self, name: str) -> None:
        name_field = self.driver.find_element(By.ID, 'input-name')
        name_field.send_keys(name)

    def fill_review_field(self, review: str) -> None:
        name_field = self.driver.find_element(By.ID, 'input-review')
        name_field.send_keys(review)

    def click_compare_button(self) -> None:
        self.driver.find_element(By.XPATH, '//button[contains(@onclick,"compare.add")]').click()

    def click_product_comparison_link(self) -> None:
        self.driver.find_element(By.XPATH, '//a[text()="product comparison"]').click()

    def get_quantity_field(self) -> WebElement:
        return self.driver.find_element(By.NAME, 'quantity')

    def clear_quantity_field(self) -> None:
        self.get_quantity_field().clear()

    def set_quantity(self, quantity: str) -> None:
        self.get_quantity_field().send_keys(quantity)

    def click_add_to_cart_button(self) -> None:
        self.driver.find_element(By.ID, 'button-cart').click()
