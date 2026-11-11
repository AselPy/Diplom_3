from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    ACTIVE_PASSWORD_FIELD = (
        By.XPATH, "//input[@name='Введите новый пароль']/parent::div[contains(@class, 'input_status_active')]"
    )
