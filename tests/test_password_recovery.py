import allure

from helpers import generate_user_data
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:

    @allure.title('Кнопка «Восстановить пароль» ведёт на страницу восстановления пароля')
    def test_click_restore_password_opens_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()

        login_page.click_restore_password()

        assert ForgotPasswordPage(driver).is_forgot_password_page_opened()

    @allure.title('После ввода почты и клика «Восстановить» открывается страница сброса пароля')
    def test_enter_email_and_click_restore_opens_reset_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page()

        forgot_password_page.enter_email(generate_user_data()["email"])
        forgot_password_page.click_restore()

        assert ResetPasswordPage(driver).is_reset_password_page_opened()

    @allure.title('Клик по кнопке показать/скрыть пароль подсвечивает поле пароля')
    def test_click_show_password_makes_password_field_active(self, driver):
        ForgotPasswordPage(driver).request_password_reset(generate_user_data()["email"])
        reset_password_page = ResetPasswordPage(driver)

        reset_password_page.click_show_password()

        assert reset_password_page.is_password_field_active()
