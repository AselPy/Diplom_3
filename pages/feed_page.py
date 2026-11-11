import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
from urls import FEED_PAGE


class FeedPage(BasePage):

    @allure.step('Открыть ленту заказов')
    def open_page(self):
        self.open(FEED_PAGE)
        self.wait_visible(FeedPageLocators.FIRST_ORDER)

    def is_feed_opened(self):
        return self.is_visible(FeedPageLocators.FEED_TITLE)

    @allure.step('Кликнуть на заказ в ленте')
    def click_first_order(self):
        self.click(FeedPageLocators.FIRST_ORDER)

    def is_order_details_visible(self):
        return self.is_visible(FeedPageLocators.ORDER_DETAILS_MODAL)

    @allure.step('Получить номера заказов в ленте')
    def get_order_numbers(self):
        return [int(text.lstrip('#')) for text in self.get_texts(FeedPageLocators.ORDER_NUMBERS)]

    @allure.step('Получить счётчик «Выполнено за всё время»')
    def get_completed_all_time(self):
        return int(self.get_text(FeedPageLocators.COMPLETED_ALL_TIME_COUNTER))

    @allure.step('Получить счётчик «Выполнено за сегодня»')
    def get_completed_today(self):
        return int(self.get_text(FeedPageLocators.COMPLETED_TODAY_COUNTER))

    @allure.step('Дождаться, когда счётчик «Выполнено за всё время» станет больше {old_value}')
    def wait_completed_all_time_greater_than(self, old_value):
        self.wait_until(lambda driver: self.get_completed_all_time() > old_value)
        return self.get_completed_all_time()

    @allure.step('Дождаться, когда счётчик «Выполнено за сегодня» станет больше {old_value}')
    def wait_completed_today_greater_than(self, old_value):
        self.wait_until(lambda driver: self.get_completed_today() > old_value)
        return self.get_completed_today()

    @allure.step('Дождаться заказа {order_number} в разделе «В работе»')
    def wait_order_in_progress(self, order_number):
        self.wait_until(lambda driver: order_number in self.get_orders_in_progress())
        return self.get_orders_in_progress()

    def get_orders_in_progress(self):
        texts = [element.text for element in self.driver.find_elements(*FeedPageLocators.ORDERS_IN_PROGRESS)]
        return [int(text) for text in texts if text.isdigit()]
