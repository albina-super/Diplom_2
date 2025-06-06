import allure
import pytest

from helpers import data_for_user
from methods.user_methods import UserMethods
from data import MY_USER_DATA, DATA_WITHOUT_LOGIN, DATA_WITHOUT_PASSWORD, DATA_WITHOUT_USERNAME, SUCCESS_STATUS, \
    FORBIDDEN_STATUS, UNAUTHORIZED_STATUS, INVALID_PASS_FOR_LOGIN, INVALID_EMAIL_FOR_LOGIN, UPDATE_EMAIL_DATA, \
    UPDATE_NAME_DATA


class TestUserMethods:

    @allure.title('Тесты на успешную регистрацию пользователя')
    def test_register_user_success(self):
        user = UserMethods()
        data = data_for_user()
        code, response = user.register_user(data)
        res_data = {
            "user": {
                "email": data['email'],
                "name": data['name']
            }
        }

        assert code == SUCCESS_STATUS and  res_data['user'].items() == response['user'].items() and "accessToken" in response and "refreshToken" in response


    @allure.title('Тесты на регистрацию существующего пользователя')
    def test_register_exists_user(self, user):
        user_test = UserMethods()
        code, response = user_test.register_user(MY_USER_DATA)
        assert code == 403 and response == {
            "success": False,
            "message": "User already exists"
            }


    @pytest.mark.parametrize(
        'data',
        [
            DATA_WITHOUT_LOGIN,
            DATA_WITHOUT_PASSWORD,
            DATA_WITHOUT_USERNAME
        ]
    )
    def test_register_user_without_one_field(self, data):
        allure.dynamic.title('Тестируем регистрацию  без одного обязательного поля')
        user = UserMethods()
        code, response = user.register_user(data)
        assert code == FORBIDDEN_STATUS and response == {
            "success": False,
            "message": "Email, password and name are required fields"
        }


    @allure.title('Тесты на успешный логин')
    def test_login_user_success(self, user):
        user = UserMethods()
        code, response = user.login_user(MY_USER_DATA)
        assert code == SUCCESS_STATUS and 'accessToken' in response and 'refreshToken' in response


    @pytest.mark.parametrize(
        'data',
        [
            INVALID_PASS_FOR_LOGIN,
            INVALID_EMAIL_FOR_LOGIN
        ]
    )
    def test_login_with_invalid_data(self, user, data):
        allure.dynamic.title('Тестируем логин без одного обязательного поля')
        user_test = UserMethods()
        code, response = user_test.login_user(data)
        assert code == UNAUTHORIZED_STATUS and response == {
            "success": False,
            "message": "email or password are incorrect"
        }


    @pytest.mark.parametrize(
        'data', [
           UPDATE_EMAIL_DATA,
           UPDATE_NAME_DATA
       ]
    )
    def test_update_user_with_authorization(self, data, user_login):
        allure.dynamic.title('Тестируем редактирование юзера с авторизацией')
        user_test = UserMethods()
        code, response = user_test.update_user(data, user_login)
        key = list(data.keys())[0]
        assert code == SUCCESS_STATUS and response['user'][key] == data[key]


    @pytest.mark.parametrize(
        'data', [
            UPDATE_EMAIL_DATA,
            UPDATE_NAME_DATA
        ]
    )
    def test_update_user_without_authorization(self, user, data):
        allure.dynamic.title('Тестируем редактирование юзера без авторизации')
        user_test = UserMethods()
        code, response = user_test.update_user(data, token='')
        assert code == UNAUTHORIZED_STATUS and response == {
            "success": False,
            "message": "You should be authorised"
        }

