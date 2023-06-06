from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.base_url = "https://hh.ru"
        self.driver = driver

    def go_to_site(self):
        """ Открываем главную страницу сайта"""

        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """ Находим один элемент по локатору"""

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"{locator} not found")

    def find_elements(self, locator, time=10):
        """Находим все элементы , имеющие данный локатор"""

        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"{locator} not found")
