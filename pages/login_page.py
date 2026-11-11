import allure

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import LOGIN_PAGE


class LoginPage(BasePage):

    @allure.step('Открыть страницу входа')
    def open_page(self):
        self.open(LOGIN_PAGE)
        self.wait_visible(LoginPageLocators.LOGIN_TITLE)

    @allure.step('Войти под пользователем {email}')
    def login(self, email, password):
        self.open_page()
        self.type_text(LoginPageLocators.EMAIL_INPUT, email)
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_visible(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Нажать «Восстановить пароль»')
    def click_restore_password(self):
        self.click(LoginPageLocators.RESTORE_PASSWORD_LINK)

    def is_login_page_opened(self):
        return self.is_visible(LoginPageLocators.LOGIN_TITLE)
