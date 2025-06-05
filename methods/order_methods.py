from json import loads
from allure import step
import requests

from data import ORDER_URL, BASE_URL


class OrderMethods:

    @step('Создаем ордер')
    def create_order(self, params):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', json=params)
        return response.status_code, loads(response.text)


    @step('Получаеи список ордеров')
    def get_list_user_orders(self):
        response = requests.get(f'{BASE_URL}{ORDER_URL}')
        return response.status_code, loads(response.text)