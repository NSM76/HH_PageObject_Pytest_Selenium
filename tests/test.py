import pytest

from pages.hh_home_page import SearchHelper
from pages.hh_seach_page import SearchVacancies, SearchNaviBar, SearchNumberVacancies


def test_hh(browser):
    # наша искомая вакансия
    vacancy = "Тестировщик автоматизатор"

    # экземпляр класса поиска текста информационной строки о результате поиска вакансий
    hh_search_number_of_vacancies = SearchNumberVacancies(browser)

    # экземпляр класса поиска элементов навигационного меню
    hh_search_navi_bar = SearchNaviBar(browser)

    # экземпляр класса поиска вакансий
    hh_search_page = SearchVacancies(browser)

    # экземпляр класса ввода данных в строку поиска
    hh_home_page = SearchHelper(browser)

    # открываем главную страницу сайта
    hh_home_page.go_to_site()

    # вводим в строку поиска нашу вакансию
    hh_home_page.enter_vacancy(vacancy)

    # кликаем на кнопку "Найти работу"
    hh_home_page.click_on_find_button()

    # Список найденных вакансий
    vacancies = hh_search_page.list_all_vacancies()
    print("\nНайденные вакансии:\n", '\n'.join(vacancies))

    # Список элементов навигационного меню
    elements = hh_search_navi_bar.check_navi_bar()

    # Текст с количеством найденных вакансий по запросу найшей вакансии(vacancy)
    text_info = hh_search_number_of_vacancies.check_number_of_vacancies()[0]
    # разбиваем строку с текстом на слова по пробелам и делаем из них список
    list_el_text_info = text_info.split()

    # проверка, что мы находимся на странице с найденными вакансиями
    assert "Вакансии" and "Резюме" and "Компании" in elements

    # проверка, что список найденных вакансий не пустой
    assert len(vacancies) > 0

    # проверка, что в информационной строке количество вакансий совпадает с количеством найденных
    assert int(list_el_text_info[0]) == len(vacancies)

    # проверка, что в информационной строке присутсвует название нашей вакансии
    assert vacancy in text_info
