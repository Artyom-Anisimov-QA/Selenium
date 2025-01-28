import logging
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


# _________________.addoption______________________
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--yandex", default=r"C:\Users\admin\Desktop\webdrivers\yandexdriver")
    parser.addoption("--url", default="http://192.168.0.144:8081")
    parser.addoption("--log_level", default="DEBUG")


# _____Fixtures for .addoption/____________________
@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser")
    yandex = request.config.getoption("yandex")
    log_level = request.config.getoption("--log_level")
    driver = None


    # Настройка логирования
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
#    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO)) # Устанавливаем уровень логирования
    logger.setLevel(level=log_level)

    logger.info("===> TEST %s STARTED at %s" % (request.node.name, datetime.datetime.now()))

    # Инициализация браузера
    if browser_name in ["ch", "chrome"]:
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif browser_name in ["ya", "yandex"]:
        options = ChromeOptions()
        options.binary_location = (r"C:\Users\admin\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
        driver = webdriver.Chrome(options=options, service=Service(executable_path=yandex))
        driver.maximize_window()

    # Добавляем свойства к драйверу для логирования
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    def fin():
        driver.quit()
        logger.info("===> TEST %s FINISHED at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    yield driver
