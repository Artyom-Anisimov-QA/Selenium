import allure
from selenium.common import TimeoutException, InvalidSelectorException, NoSuchElementException, \
    StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException, NoAlertPresentException, \
    NoSuchWindowException, NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    # Описание локаторов
    PRICE_MACBOOK_US_DOLLAR = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
    PRICE_IPHONE_US_DOLLAR = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    PRICE_APPLE_CINEMA_US_DOLLAR = (By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/div/div/span[1]')
    PRICE_CANON_EOS_5D_US_DOLLAR = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[2]/div/div/span[1]')
    POUND_STERLING = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a')
    PRICE_MACBOOK_POUND_STERLING = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
    PRICE_IPHONE_POUND_STERLING = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div/div/span[1]')
    PRICE_APPLE_CINEMA_POUND_STERLING = (By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[2]/div/div/span[1]')
    PRICE_CANON_EOS_5D_POUND_STERLING = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[2]/div/div/span[1]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search"]/button')
    REMOVE_BUTTON = (By.XPATH, '//*[@class="fa-solid fa-circle-xmark"]/parent::*')
    BASKET_BUTTON = (By.XPATH, '//*[@id="header-cart"]/div/button/i')
    EMPTY_MODAL_WINDOW = (By.XPATH, '//*[@id="header-cart"]/div/ul/li')
    POPUP_WINDOW = (By.XPATH, '//*[@id="alert"]/div')
    MODAL_WINDOW = (By.XPATH, '//*[@id="header-cart"]/div/ul')

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__


    # Метод ищет элементы на странице
    @allure.step("Finding element: {args}")
    def find(self, *args):
        self.logger.debug("%s: Finding element: %s" % (self.class_name, args))
        try:
            element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*args))
            self.logger.info("%s: Successfully found element: %s" % (self.class_name, args))
            return element
        except InvalidSelectorException as ise:
            self.logger.critical("%s: Invalid selector used: %s. Error: %s" % (self.class_name, args, str(ise)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Invalid selector used",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoSuchElementException as nsee:
            self.logger.error("%s: No such element found: %s. Error: %s" % (self.class_name, args, str(nsee)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No such element found",
                attachment_type=allure.attachment_type.PNG)
            return None
        except StaleElementReferenceException as sere:
            self.logger.error("%s: Stale element reference: %s. Error: %s" % (self.class_name, args, str(sere)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Stale element reference",
                attachment_type=allure.attachment_type.PNG)
            return None
        except TimeoutException as te:
            self.logger.error("%s: Element not found within timeout: %s. Error: %s" % (self.class_name, args, str(te)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Element not found within timeout",
                attachment_type=allure.attachment_type.PNG)
            return None
        except ElementNotVisibleException as enve:
            self.logger.error("%s: Element not visible: %s. Error: %s" % (self.class_name, args, str(enve)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Element not visible",
                attachment_type=allure.attachment_type.PNG)
            return None
        except ElementNotSelectableException as ense:
            self.logger.error("%s: Element not selectable: %s. Error: %s" % (self.class_name, args, str(ense)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Element not selectable",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoAlertPresentException as nap:
            self.logger.error("%s: No alert present when expected. Error: %s" % (self.class_name, str(nap)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No alert present when expected",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoSuchWindowException as nswe:
            self.logger.error("%s: No such window found. Error: %s" % (self.class_name, str(nswe)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No such window found",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoSuchFrameException as nsfe:
            self.logger.error("%s: No such frame found. Error: %s" % (self.class_name, str(nsfe)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No such frame found",
                attachment_type=allure.attachment_type.PNG)
            return None


    # Метод ищет кликабельные элементы на странице
    @allure.step("Finding clickable element element: {args}")
    def find_clickable(self, *args):
        self.logger.debug("%s: Finding clickable element: %s" % (self.class_name, args))
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(*args))
            self.logger.info("%s: Successfully found clickable element: %s" % (self.class_name, args))
            return element
        except InvalidSelectorException as ise:
            self.logger.critical("%s: Invalid selector used: %s. Error: %s" % (self.class_name, args, str(ise)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Invalid selector used",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoSuchElementException as nsee:
            self.logger.error("%s: No such сlickable element found: %s. Error: %s" % (self.class_name, args, str(nsee)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No such сlickable element found",
                attachment_type=allure.attachment_type.PNG)
            return None
        except StaleElementReferenceException as sere:
            self.logger.error("%s: Stale сlickable element reference: %s. Error: %s" % (self.class_name, args, str(sere)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Stale сlickable element reference",
                attachment_type=allure.attachment_type.PNG)
            return None
        except TimeoutException as te:
            self.logger.error("%s: Clickable element not found: %s. Error: %s" % (self.class_name, args, str(te)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Clickable element not found",
                attachment_type=allure.attachment_type.PNG)
            return None
        except ElementNotVisibleException as enve:
            self.logger.error("%s: Clickable element not visible: %s. Error: %s" % (self.class_name, args, str(enve)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Clickable element not visible",
                attachment_type=allure.attachment_type.PNG)
            return None
        except ElementNotSelectableException as ense:
            self.logger.error("%s: Clickable element not selectable: %s. Error: %s" % (self.class_name, args, str(ense)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Clickable element not selectable",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoAlertPresentException as nap:
            self.logger.error("%s: No alert present when expected. Error: %s" % (self.class_name, str(nap)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No alert present when expected",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoSuchWindowException as nswe:
            self.logger.error("%s: No such window found. Error: %s" % (self.class_name, str(nswe)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No such window found",
                attachment_type=allure.attachment_type.PNG)
            return None
        except NoSuchFrameException as nsfe:
            self.logger.error("%s: No such frame found. Error: %s" % (self.class_name, str(nsfe)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="No such frame found",
                attachment_type=allure.attachment_type.PNG)
            return None


    # Клик по элементу с использованием ActionChains
    @allure.step("Clicking custom element: {element}")
    def custom_click(self, element):
        if element is not None:
            self.logger.debug("%s: Clicking custom element: %s" % (self.class_name, str(element)))
            ActionChains(self.browser).move_to_element(element).pause(0.5).click().perform()
            self.logger.info("%s: Successfully clicked on element: %s" % (self.class_name, str(element)))
        else:
            self.logger.error("%s: Cannot click on None element." % self.class_name)
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Cannot click on None element",
                attachment_type=allure.attachment_type.PNG)


    # Ищет кнопку 'Корзина' на странице
    @allure.step("Finding button Сart_shopping")
    def get_button_cart_shopping(self):
        self.logger.debug("%s: Finding button Сart_shopping." % self.class_name)
        button = self.find(self.BASKET_BUTTON)
        button.click()
        if button is not None:
            self.logger.info("%s: Found Сart_shopping." % self.class_name)
#        return button


    # Метод ищет модальное окно
    @allure.step("Finding modal window")
    def get_modal_window(self):
        self.logger.debug("%s: Finding modal window." % self.class_name)
        try:
            modal_window = self.browser.find(By.NAME, "Your shopping cart is empty!")
            self.logger.info("%s: Successfully found modal window." % self.class_name)
            return modal_window
        except Exception as e:
            self.logger.error("%s: Error finding modal window. Error: %s" % (self.class_name, str(e)))
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="Error finding modal window",
                attachment_type=allure.attachment_type.PNG)
            return None


    # Метод ожидает исчезновения всплывающего окна
    @allure.step("Waiting for disappearance of popup window")
    def get_popup_window_down(self):
        self.logger.debug("%s: Waiting for disappearance of popup window." % self.class_name)
        old_element = self.find(self.POPUP_WINDOW)
        if old_element is not None:
            try:
                WebDriverWait(self.browser, 10).until(EC.staleness_of(old_element))
                self.logger.info("%s: Popup window has disappeared." % self.class_name)
            except TimeoutException:
                self.logger.error("%s: Popup window did not disappear in time." % self.class_name)
                allure.attach(
                    self.browser.get_screenshot_as_png(),
                    name="Popup window did not disappear in time",
                    attachment_type=allure.attachment_type.PNG)