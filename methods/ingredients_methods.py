from json import loads
from allure import step
import requests

from data import BASE_URL, INGREDIENTS_URL


class IngredientsMethod:

    @step('Получаем список ингредиентов')
    def get_ingredients(self):
        response = requests.get(f'{BASE_URL}{INGREDIENTS_URL}')
        return response.status_code, loads(response.text)