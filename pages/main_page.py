import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import MAIN_PAGE

# Пока сервер не вернул номер заказа, в модальном окне показывается заглушка
ORDER_NUMBER_PLACEHOLDER = '9999'


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_page(self):
        self.open(MAIN_PAGE)
        self.wait_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    def is_constructor_opened(self):
        return self.is_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Кликнуть на ингредиент')
    def click_first_bun(self):
        self.click(MainPageLocators.FIRST_BUN)

    def is_ingredient_details_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step('Получить значение каунтера соуса')
    def get_first_sauce_counter(self):
        return int(self.get_text(MainPageLocators.FIRST_SAUCE_COUNTER))

    @allure.step('Добавить соус в заказ')
    def add_first_sauce_to_order(self):
        self.drag_and_drop(MainPageLocators.FIRST_SAUCE, MainPageLocators.BURGER_CONSTRUCTOR)

    @allure.step('Добавить булку в заказ')
    def add_first_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.FIRST_BUN, MainPageLocators.BURGER_CONSTRUCTOR)

    @allure.step('Нажать «Оформить заказ»')
    def click_place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Получить номер оформленного заказа')
    def get_order_number(self):
        self.wait_until(
            lambda driver: self.get_text(MainPageLocators.ORDER_NUMBER) not in ('', ORDER_NUMBER_PLACEHOLDER)
        )
        return int(self.get_text(MainPageLocators.ORDER_NUMBER))

    @allure.step('Оформить заказ с булкой')
    def place_order(self):
        self.add_first_bun_to_order()
        self.click_place_order()
        order_number = self.get_order_number()
        self.close_modal()
        return order_number

    def is_order_placed(self):
        return self.is_visible(MainPageLocators.ORDER_ID_TEXT)
