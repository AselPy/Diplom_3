# Diplom_3 — UI-тесты Stellar Burgers

Автотесты веб-приложения [Stellar Burgers](https://qa-stellarburgers.education-services.ru/) на Selenium с паттерном Page Object Model. Каждый тест запускается в Google Chrome и Mozilla Firefox.

## Что проверяется

- Восстановление пароля
- Личный кабинет
- Основной функционал: конструктор, лента заказов, ингредиенты, оформление заказа
- Раздел «Лента заказов»

## Структура проекта

- `pages/` — Page Object: отдельный класс для каждой страницы.
- `locators/` — локаторы, отдельный файл для каждой страницы.
- `tests/` — тесты, сгруппированные по функциональности.
- `driver_factory.py` — фабрика драйверов (паттерн Factory): создаёт драйвер Chrome или Firefox по имени браузера.
- `conftest.py` — фикстуры: браузер (Chrome и Firefox), тестовый пользователь через API.
- `helpers.py` — запросы к API для подготовки данных.
- `urls.py` — адреса страниц и API.

## Запуск

```bash
py -m pip install -r requirements.txt
py -m pytest --alluredir=allure-results
```

Просмотр отчёта:

```bash
allure serve allure-results
```
