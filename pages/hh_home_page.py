from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePageLocator:
    LOCATOR_HOME_PAGE_FIELD_SEACH = (By.ID, "a11y-search-input")
    LOCATOR_HOME_PAGE_FIND_BUTTON = (By.XPATH, "//span[contains(text(),'Найти работу')]")


class SearchHelper(BasePage):

    def enter_vacancy(self, vacancy):
        """ Ввод вакансии в поисковую строку"""

        search_field = self.find_element(HomePageLocator.LOCATOR_HOME_PAGE_FIELD_SEACH)
        search_field.click()
        search_field.send_keys(vacancy)
        return search_field

    def click_on_find_button(self):
        """Нажимаем на кнопку "Найти работу" """

        return self.find_element(HomePageLocator.LOCATOR_HOME_PAGE_FIND_BUTTON, time=1).click()
