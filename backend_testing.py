import time

import requests
from db_connector import DBConnector
# Testing for Backend env, check Post option using REST API -> Submit a GET request to check  that the user created
# -> Check posted data was stored inside DB (users table)

db_connector = DBConnector()


class BackEndTests:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def check_post(self):
        requests.post(f'http://127.0.0.1:3000/users/{self.user_id}', json={"user_name": self.name})

    def get_user(self):
        res = requests.get(f'http://127.0.0.1:3000/users/{self.user_id}')
        assert res.status_code == 200

    def check_data(self):
        existing_name = db_connector.get_user(self.user_id)
        assert self.name == existing_name

    def clean_user(self):
        res = requests.delete(f'http://127.0.0.1:3000/users/{self.user_id}')
        assert res.status_code == 200


if __name__ == "__main__":
    backend_test = BackEndTests(user_id=3, name='Gilad')
    backend_test.check_post()
    time.sleep(10)
    backend_test.get_user()
    backend_test.check_data()
    backend_test.clean_user()
