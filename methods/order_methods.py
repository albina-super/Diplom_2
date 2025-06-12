from json import loads
from allure import step
import requests

from data import ORDER_URL, BASE_URL


class OrderMethods:

    @step('Создаем ордер')
    def create_order(self, params, token):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', json=params, headers={'Authorization': f'{token}'})
        return response.status_code, response.text


    @step('Получаем список ордеров по юзеру')
    def get_list_user_orders(self,token):
        response = requests.get(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': f'{token}'})
        return response.status_code, loads(response.text)