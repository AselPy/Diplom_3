from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//header//p[text()='Конструктор']")
    FEED_LINK = (By.XPATH, "//header//p[text()='Лента Заказов']")
    ACCOUNT_LINK = (By.XPATH, "//header//p[text()='Личный Кабинет']")
    OPENED_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    OPENED_MODAL_CLOSE_BUTTON = (
        By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]"
    )
