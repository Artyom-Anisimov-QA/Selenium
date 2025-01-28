import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

# _________________.addoption______________________
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--yandex", default=r"C:\Users\admin\Desktop\webdrivers\yandexdriver")
    parser.addoption("--url", default="http://192.168.0.144:8081")


# _____Fixtures for .addoption/____________________
@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    yandex = pytestconfig.getoption("yandex")
    driver = None

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

    yield driver
    driver.quit()