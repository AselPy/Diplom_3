import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    def is_profile_page_opened(self):
        self.wait_url_contains('/account/profile')
        return self.is_visible(ProfilePageLocators.PROFILE_LINK)

    @allure.step('Нажать «История заказов»')
    def click_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Нажать «Выход»')
    def click_logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
