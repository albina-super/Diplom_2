from json import loads
import requests
from allure import step
from data import REGISTER_USER_URL, BASE_URL, LOGIN_USER_URL, USER_URL


class UserMethods:

    @step('Регистрируем юзера')
    def register_user(self, params):
        response = requests.post(f'{BASE_URL}{REGISTER_USER_URL}', json=params)
        return response.status_code, loads(response.text)


    @step('Логин пользвателя')
    def login_user(self, params):
        response = requests.post(f'{BASE_URL}{LOGIN_USER_URL}', json=params)
        return response.status_code, loads(response.text)


    @step('обновляем данные пользователя')
    def update_user(self, params, token):
        response = requests.patch(f'{BASE_URL}{USER_URL}', json=params, headers={'Authorization': f'{token}'})
        return response.status_code, loads(response.text)


    @step('Удаляем юзера')
    def delete_user(self, token):
        response = requests.delete(f'{BASE_URL}{USER_URL}', headers={'Authorization': f'{token}'})
        return response.status_code, loads(response.text)


