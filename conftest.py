import pytest

from driver_factory import WebDriverFactory
from helpers import generate_user_data, create_user, delete_user


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    """Браузер для теста: каждый тест запускается в Chrome и в Firefox."""
    browser = WebDriverFactory.get_driver(request.param)

    yield browser

    browser.quit()


@pytest.fixture
def user():
    """Тестовый пользователь, созданный через API: данные и accessToken. Удаляется после теста."""
    user_data = generate_user_data()
    token = create_user(user_data)

    yield {"email": user_data["email"], "password": user_data["password"], "token": token}

    if token:
        delete_user(token)
