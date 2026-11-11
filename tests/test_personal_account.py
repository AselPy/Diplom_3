import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage


class TestPersonalAccount:

    @allure.title('Клик на «Личный кабинет» открывает профиль пользователя')
    def test_click_account_link_opens_profile_page(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])

        MainPage(driver).click_account_link()

        assert ProfilePage(driver).is_profile_page_opened()

    @allure.title('Клик на «История заказов» открывает историю заказов')
    def test_click_order_history_opens_order_history_page(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])
        MainPage(driver).click_account_link()
        profile_page = ProfilePage(driver)

        profile_page.click_order_history()

        assert OrderHistoryPage(driver).is_order_history_page_opened()

    @allure.title('Клик на «Выход» выводит пользователя из аккаунта')
    def test_click_logout_opens_login_page(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])
        MainPage(driver).click_account_link()
        profile_page = ProfilePage(driver)

        profile_page.click_logout()

        assert LoginPage(driver).is_login_page_opened()
