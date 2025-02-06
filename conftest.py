import logging
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# _________________.addoption______________________
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--yandex", default=r"C:\Users\admin\Desktop\webdrivers\yandexdriver")
    parser.addoption("--url", default="http://192.168.0.144:8081")
    parser.addoption("--log_level", default="DEBUG")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")


# _____Fixtures for .addoption/____________________
@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("browser")
    yandex = request.config.getoption("yandex")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    mobile = request.config.getoption("--mobile")

#    executor_url = f"http://{executor}:4444/wd/hub"
#    driver = None

    # Настройка логирования
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
#    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO)) # Устанавливаем уровень логирования
    logger.setLevel(level=log_level)
    logger.info("===> TEST %s STARTED at %s" % (request.node.name, datetime.datetime.now()))


    if executor == "local":
        #Локальный запуск
        # Инициализация браузера
        if browser in ["ch", "chrome"]:
            options = ChromeOptions()
            driver = webdriver.Chrome()
            driver.maximize_window()
        elif browser in ["ff", "firefox"]:
            options = FirefoxOptions()
            driver = webdriver.Firefox()
            driver.maximize_window()
        elif browser in ["ya", "yandex"]:
            options = ChromeOptions()
            options.binary_location = (r"C:\Users\admin\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
            driver = webdriver.Chrome(options=options, service=Service(executable_path=yandex))
            driver.maximize_window()

    else:
        #Удалённый запуск через Selenoid
        executor_url = f"http://{executor}:4444/wd/hub"
        # Инициализация браузера
        if browser in ["ch", "chrome"]:
            options = ChromeOptions()
            driver = webdriver.Chrome()
            driver.maximize_window()
        elif browser in ["ff", "firefox"]:
            options = FirefoxOptions()
            driver = webdriver.Firefox()
            driver.maximize_window()
        elif browser in ["ya", "yandex"]:
            options = ChromeOptions()
            options.binary_location = (r"C:\Users\admin\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
            driver = webdriver.Chrome(options=options, service=Service(executable_path=yandex))
            driver.maximize_window()

        caps = {
            "browserName": browser,
            #"browserVersion": version,
            # "selenoid:options": {
            #     "enableVNC": vnc,
            #     "name": request.node.name,
            #     "screenResolution": "1280x2000",
            #     "enableVideo": video,
            #     "enableLog": logs,
            #     "timeZone": "Europe/Moscow",
            #     "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
            #    "sessionTimeout": "30m"
            # },
            # "acceptInsecureCerts": True, # игнорировать ошибки сертификатов
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    # Добавляем свойства к драйверу для логирования
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    def fin():
        driver.quit()
        logger.info("===> TEST %s FINISHED at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    yield driver
