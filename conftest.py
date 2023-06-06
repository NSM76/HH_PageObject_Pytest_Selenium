import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    #1й способ запуска браузера в режиме без пользовательского интерфейса
    options.add_argument("--headless")

    # 2й способ запуска браузера в режиме без пользовательского интерфейса
    # options.headless = True

    driver = webdriver.Chrome(executable_path="./chromedriver_win32", options=options)
    # driver.set_window_size(1400, 1000)
    driver.maximize_window()

    yield driver

    driver.quit()
