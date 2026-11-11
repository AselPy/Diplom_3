import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    def is_reset_password_page_opened(self):
        self.wait_url_contains('/reset-password')
        return self.is_visible(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Нажать кнопку показать/скрыть пароль')
    def click_show_password(self):
        self.click(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        return self.is_visible(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
