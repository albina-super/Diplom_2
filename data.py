BASE_URL = ' https://stellarburgers.nomoreparties.site/api/'
REGISTER_USER_URL = 'auth/register'
LOGIN_USER_URL = 'auth/login'
USER_URL = 'auth/user'
ORDER_URL = 'orders'
INGREDIENTS_URL = 'ingredients'



MY_USER_DATA = {
    "email": "my_user555@test.com",
    "password": "test123",
    "name": "my_user"
}

DATA_WITHOUT_LOGIN = {
    "email": "",
    "password": "test123",
    "name": "my_user2"
}

DATA_WITHOUT_PASSWORD = {
    "email": "my_user553@test.com",
    "password": "",
    "name": "my_user3"
}

DATA_WITHOUT_USERNAME = {
    "email": "my_user554@test.com",
    "password": "test123",
    "name": ""
}



INVALID_PASS_FOR_LOGIN = {
    "email": "my_user555@test.com",
    "password": "test12"
}

INVALID_EMAIL_FOR_LOGIN = {
    "email": "my_user552@test.com",
    "password": "test123"
}


UPDATE_EMAIL_DATA = {
    "email": "test_email123@test.com",
}

UPDATE_NAME_DATA = {
    "name": "Test_My_user",
}

INVALID_HASH_INGREDIENTS_DATA = ['qwerty12345', 'asdfsddhghg87878']

SUCCESS_STATUS = 200
FORBIDDEN_STATUS = 403
UNAUTHORIZED_STATUS = 401
BAD_REQUEST_STATUS = 400
SERVER_ERROR_STATUS = 500