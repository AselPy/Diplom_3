import allure

from helpers import create_order
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage


class TestOrderFeed:

    @allure.title('Клик на заказ в ленте открывает окно с деталями заказа')
    def test_click_order_opens_details_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_page()

        feed_page.click_first_order()

        assert feed_page.is_order_details_visible()

    @allure.title('Заказы пользователя из «Истории заказов» отображаются в ленте заказов')
    def test_user_orders_from_history_displayed_in_feed(self, driver, user):
        create_order(user["token"])
        LoginPage(driver).login(user["email"], user["password"])
        MainPage(driver).click_account_link()
        ProfilePage(driver).click_order_history()
        history_orders = OrderHistoryPage(driver).get_order_numbers()
        feed_page = FeedPage(driver)

        feed_page.open_page()

        assert set(history_orders).issubset(feed_page.get_order_numbers())

    @allure.title('При создании заказа счётчик «Выполнено за всё время» увеличивается')
    def test_new_order_increases_completed_all_time_counter(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])
        feed_page = FeedPage(driver)
        feed_page.open_page()
        counter_before = feed_page.get_completed_all_time()
        feed_page.click_constructor_link()

        MainPage(driver).place_order()
        feed_page.open_page()

        assert feed_page.wait_completed_all_time_greater_than(counter_before) > counter_before

    @allure.title('При создании заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_new_order_increases_completed_today_counter(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])
        feed_page = FeedPage(driver)
        feed_page.open_page()
        counter_before = feed_page.get_completed_today()
        feed_page.click_constructor_link()

        MainPage(driver).place_order()
        feed_page.open_page()

        assert feed_page.wait_completed_today_greater_than(counter_before) > counter_before

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_new_order_number_appears_in_progress(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])

        order_number = MainPage(driver).place_order()
        feed_page = FeedPage(driver)
        feed_page.open_page()

        assert order_number in feed_page.wait_order_in_progress(order_number)
