import requests

from data import BASE_URL, INGREDIENTS_URL


class IngredientsMethod:

    def get_ingredients(self):
        response = requests.get(f'{BASE_URL}{INGREDIENTS_URL}')
        return response.json()