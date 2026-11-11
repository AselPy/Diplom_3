from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDER_NUMBERS = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]//div[contains(@class, 'OrderHistory_textBox')]/p[1]")
