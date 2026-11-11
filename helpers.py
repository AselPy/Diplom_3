import random
import string

import allure
import requests

from urls import API_REGISTER_USER, API_USER, API_INGREDIENTS, API_ORDERS


def generate_random_string(length=10):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def generate_user_data():
    return {
        "email": f'{generate_random_string()}@yandex.ru',
        "password": generate_random_string(),
        "name": generate_random_string()
    }


@allure.step('Создать пользователя через API')
def create_user(user_data):
    return requests.post(API_REGISTER_USER, json=user_data).json().get("accessToken")


@allure.step('Удалить пользователя через API')
def delete_user(token):
    requests.delete(API_USER, headers={"Authorization": token})


@allure.step('Создать заказ через API')
def create_order(token):
    ingredients = requests.get(API_INGREDIENTS).json()["data"]
    bun_id = next(item["_id"] for item in ingredients if item["type"] == "bun")
    response = requests.post(API_ORDERS, json={"ingredients": [bun_id]}, headers={"Authorization": token})
    return response.json()["order"]["number"]
