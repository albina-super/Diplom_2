import random

import pytest

from data import MY_USER_DATA
from methods.ingredients_methods import IngredientsMethod
from methods.user_methods import UserMethods


@pytest.fixture
def user():
    user = UserMethods()
    code, response = user.register_user(MY_USER_DATA)
    yield response
    status, response_login = user.login_user(MY_USER_DATA)
    user.delete_user(response_login['accessToken'])


@pytest.fixture
def user_login():
    user = UserMethods()
    _response = user.register_user(MY_USER_DATA)
    code, response = user.login_user(MY_USER_DATA)
    yield response['accessToken']
    user.delete_user(response['accessToken'])


@pytest.fixture
def ingredients():
    ingredients = IngredientsMethod()
    code, response = ingredients.get_ingredients()
    all_ids = [item["_id"] for item in response["data"][1:3]]
    return all_ids