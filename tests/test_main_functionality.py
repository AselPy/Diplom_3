import allure

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunctionality:

    @allure.title('Клик на «Конструктор» открывает конструктор бургера')
    def test_click_constructor_link_opens_constructor(self, driver):
        FeedPage(driver).open_page()
        main_page = MainPage(driver)

        main_page.click_constructor_link()

        assert main_page.is_constructor_opened()

    @allure.title('Клик на «Лента заказов» открывает ленту заказов')
    def test_click_feed_link_opens_feed(self, driver):
        MainPage(driver).open_page()
        feed_page = FeedPage(driver)

        feed_page.click_feed_link()

        assert feed_page.is_feed_opened()

    @allure.title('Клик на ингредиент открывает окно с деталями ингредиента')
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()

        main_page.click_first_bun()

        assert main_page.is_ingredient_details_visible()

    @allure.title('Окно с деталями ингредиента закрывается кликом по крестику')
    def test_click_close_button_closes_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_first_bun()

        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title('При добавлении ингредиента в заказ его каунтер увеличивается')
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        counter_before = main_page.get_first_sauce_counter()

        main_page.add_first_sauce_to_order()

        assert main_page.get_first_sauce_counter() == counter_before + 1

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_place_order(self, driver, user):
        LoginPage(driver).login(user["email"], user["password"])
        main_page = MainPage(driver)

        main_page.add_first_bun_to_order()
        main_page.click_place_order()

        assert main_page.is_order_placed()
        assert main_page.get_order_number() > 0
