from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    FIRST_ORDER = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]//a[contains(@class, 'OrderHistory_link')])[1]")
    ORDER_NUMBERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]//div[contains(@class, 'OrderHistory_textBox')]/p[1]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_orderBox')]")
    COMPLETED_ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COMPLETED_TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Список под заголовком «В работе» на странице имеет класс OrderFeed_orderListReady
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
