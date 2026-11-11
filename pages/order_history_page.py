import allure

from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    def is_order_history_page_opened(self):
        return self.wait_url_contains('/account/order-history')

    @allure.step('Получить номера заказов из истории')
    def get_order_numbers(self):
        return [int(text.lstrip('#')) for text in self.get_texts(OrderHistoryPageLocators.ORDER_NUMBERS)]
