import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import FORGOT_PASSWORD_PAGE


class ForgotPasswordPage(BasePage):

    @allure.step('Открыть страницу восстановления пароля')
    def open_page(self):
        self.open(FORGOT_PASSWORD_PAGE)
        self.wait_visible(ForgotPasswordPageLocators.RESTORE_BUTTON)

    def is_forgot_password_page_opened(self):
        self.wait_url_contains('/forgot-password')
        return self.is_visible(ForgotPasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Ввести почту {email}')
    def enter_email(self, email):
        self.type_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажать «Восстановить»')
    def click_restore(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Запросить восстановление пароля для {email}')
    def request_password_reset(self, email):
        self.open_page()
        self.enter_email(email)
        self.click_restore()
