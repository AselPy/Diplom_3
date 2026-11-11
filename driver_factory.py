from selenium import webdriver


class WebDriverFactory:
    """Фабрика драйверов: создаёт драйвер нужного браузера по его имени."""

    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080

    @classmethod
    def get_driver(cls, browser_name):
        if browser_name == 'chrome':
            driver = webdriver.Chrome(options=cls._get_chrome_options())
        elif browser_name == 'firefox':
            driver = webdriver.Firefox()
        else:
            raise ValueError(f'Браузер «{browser_name}» не поддерживается. Доступны: chrome, firefox')
        driver.set_window_size(cls.WINDOW_WIDTH, cls.WINDOW_HEIGHT)
        return driver

    @staticmethod
    def _get_chrome_options():
        options = webdriver.ChromeOptions()
        # Отключаем окно Chrome «Смените пароль», которое появляется после входа с простым паролем
        options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False,
            'profile.password_manager_leak_detection': False
        })
        return options
