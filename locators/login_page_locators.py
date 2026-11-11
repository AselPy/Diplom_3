from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
