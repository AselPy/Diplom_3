from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    FIRST_BUN = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul[1]/a[1]")
    FIRST_SAUCE = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul[1]/a[1]")
    FIRST_SAUCE_COUNTER = (
        By.XPATH, "//h2[text()='Соусы']/following-sibling::ul[1]/a[1]//p[contains(@class, 'counter_counter__num')]"
    )
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_NUMBER = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")
    ORDER_ID_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")
