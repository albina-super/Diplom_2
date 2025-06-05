from helpers import data_for_user
from methods.user_methods import UserMethods

class TestUserMethods:

    def test_register_user_success(self):
        user = UserMethods()
        data = data_for_user()
        code, response = user.register_user(data)
        print(response, '789')
        res_data = {
            "success": True,
            "user": {
                "email": data['email'],
                "name": data['name']
            }
        }
        assert code == 200 and  res_data.keys() in response.keys()


    def test_register_exists_user(self):
        pass

    def test_register_user_without_one_field(self):
        pass


    def test_login_user_success(self):
        pass


    def test_login_with_invalid_data(self):
        pass


    def test_login_update_user_with_authorization(self):
        pass

    def test_login_update_user_without_authorization(self):
        pass

