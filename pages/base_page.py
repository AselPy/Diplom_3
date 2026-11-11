import allure
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_page_locators import BasePageLocators

# Для React DnD обычный drag_and_drop из Selenium не срабатывает, поэтому события перетаскивания отправляются скриптом
DRAG_AND_DROP_SCRIPT = """
const source = arguments[0];
const target = arguments[1];
const dataTransfer = new DataTransfer();
const fire = (element, type) => element.dispatchEvent(
    new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer: dataTransfer})
);
fire(source, 'dragstart');
fire(target, 'dragenter');
fire(target, 'dragover');
fire(target, 'drop');
fire(source, 'dragend');
"""


class BasePage:
    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {url}')
    def open(self, url):
        self.driver.get(url)

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator))

    def wait_all_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_all_elements_located(locator))

    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.invisibility_of_element_located(locator))

    def wait_url_contains(self, part):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.url_contains(part))

    def wait_until(self, condition):
        wait = WebDriverWait(self.driver, self.TIMEOUT, ignored_exceptions=[StaleElementReferenceException])
        return wait.until(condition)

    def is_visible(self, locator):
        return self.wait_visible(locator).is_displayed()

    def click(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            # Пока закрывается модальное окно, его фон перекрывает страницу — тогда кликаем скриптом
            self.driver.execute_script('arguments[0].click();', element)

    def type_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def get_texts(self, locator):
        return [element.text for element in self.wait_all_visible(locator)]

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_visible(source_locator)
        target = self.wait_visible(target_locator)
        self.driver.execute_script(DRAG_AND_DROP_SCRIPT, source, target)

    @allure.step('Нажать «Конструктор» в шапке')
    def click_constructor_link(self):
        self.click(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step('Нажать «Лента заказов» в шапке')
    def click_feed_link(self):
        self.click(BasePageLocators.FEED_LINK)

    @allure.step('Нажать «Личный кабинет» в шапке')
    def click_account_link(self):
        self.click(BasePageLocators.ACCOUNT_LINK)

    @allure.step('Закрыть модальное окно крестиком')
    def close_modal(self):
        self.click(BasePageLocators.OPENED_MODAL_CLOSE_BUTTON)
        self.wait_invisible(BasePageLocators.OPENED_MODAL)

    def is_modal_closed(self):
        return self.wait_invisible(BasePageLocators.OPENED_MODAL)
