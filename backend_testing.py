import requests
from db_connector import DBConnector

db_connector = DBConnector()


class BackEndTests:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def check_post(self):
        requests.post(f'http://127.0.0.1:5000/users/{self.user_id}', json={"user_name": self.name})

    def get_user(self):
        res = requests.get(f'http://127.0.0.1:5000/users/{self.user_id}')
        assert res.status_code == 200

    def check_data(self):
        existing_name = db_connector.select_id(self.user_id)
        assert self.name == existing_name

    def clean_user(self):
        res = requests.delete(f'http://127.0.0.1:5000/users/{self.user_id}')
        assert res.status_code == 200
        # db_connector.delete_user(self.user_id)


if __name__ == "__main__":
    backend_test = BackEndTests(user_id=8, name='Gilad')
    backend_test.check_post()
    backend_test.get_user()
    backend_test.check_data()
    backend_test.clean_user()
