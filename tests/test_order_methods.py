from json import loads
import allure
from data import BAD_REQUEST_STATUS, INVALID_HASH_INGREDIENTS_DATA, SERVER_ERROR_STATUS, UNAUTHORIZED_STATUS, \
    SUCCESS_STATUS
from methods.order_methods import OrderMethods


class TestOrderMethods:

    @allure.title('Тесты на создание ордера с авторизованным пользователем')
    def test_create_order_with_authorization(self, ingredients, user_login):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': ingredients}, user_login)
        assert code == SUCCESS_STATUS and loads(response)['success'] == True


    @allure.title('Тесты на создание ордера без авторизации')
    def test_create_order_without_authorization(self, ingredients):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': ingredients}, token='')
        assert code == SUCCESS_STATUS and loads(response)['success'] == True


    @allure.title('Тесты на создание ордера без ингредиентов')
    def test_create_order_without_ingredients(self):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': []}, token='')
        assert code == BAD_REQUEST_STATUS and loads(response) == {
            "success": False,
            "message": "Ingredient ids must be provided"
        }

    @allure.title('Тесты на создание ордера с невалидным хэшем ингредиентов')
    def test_create_order_with_invalid_ingredients(self):
        order = OrderMethods()
        code, response = order.create_order({'ingredients': INVALID_HASH_INGREDIENTS_DATA}, token='')
        assert code == SERVER_ERROR_STATUS


    @allure.title('Тесты на получение списка ордеров по юзеру без авторизации')
    def test_get_list_user_orders_without_authorization(self):
        order = OrderMethods()
        code, response = order.get_list_user_orders(token='')
        assert code == UNAUTHORIZED_STATUS and response == {
            "success": False,
            "message": "You should be authorised"
        }

    @allure.title('Тесты на получение списка ордеров по юзеру с авторизацией')
    def test_get_list_user_orders_with_authorization(self, user_login):
        order = OrderMethods()
        code, response = order.get_list_user_orders(user_login)
        type_order_field = type(response['orders'])
        assert code == SUCCESS_STATUS and response['success'] == True and type_order_field == list

