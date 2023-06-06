from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPageLocator:
    LOCATOR_VACANCIES = (By.CSS_SELECTOR, ".serp-item__title")
    LOCATOR_NAVI_BAR = (By.CSS_SELECTOR, ".supernova-navi-search-tab")
    LOCATOR_NUMBER_OF_VACANCIES = (By.CSS_SELECTOR, "h1.bloko-header-section-3")


class SearchVacancies(BasePage):
    def list_all_vacancies(self):
        """ Находим все вакансии, выведденые на странице"""

        all_list_vacancies = self.find_elements(SearchPageLocator.LOCATOR_VACANCIES)
        return [x.text for x in all_list_vacancies]


class SearchNaviBar(BasePage):
    def check_navi_bar(self):
        """ Находим элементы навигационного меню"""

        elements_navi_bar = self.find_elements(SearchPageLocator.LOCATOR_NAVI_BAR)
        return [x.text for x in elements_navi_bar]


class SearchNumberVacancies(BasePage):
    def check_number_of_vacancies(self):
        """Находим текст в информационной строке о поиске нашей вакансии"""
        info_number_of_vacancies = self.find_elements(SearchPageLocator.LOCATOR_NUMBER_OF_VACANCIES)
        return [x.text for x in info_number_of_vacancies]
