import requests
from db_connector import DBConnector

db_connector = DBConnector()


class BackEndTests:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def test_create_user(self):
        requests.post(f'http://127.0.0.1:5000/users/{self.user_id}', json={"user_name": self.name})

    def test_get_user(self):
        res = requests.get(f'http://127.0.0.1:5000/users/{self.user_id}')
        assert res.status_code == 200

    def test_put_user(self):
        res = requests.put(f'http://127.0.0.1:5000/users/{self.user_id}')
        assert res.status_code == 200

    def test_clean_user(self):
        res = requests.delete(f'http://127.0.0.1:5000/users/{self.user_id}')
        assert res.status_code == 200
        # db_connector.delete_user(self.user_id)


if __name__ == "__main__":
    backend_test = BackEndTests(user_id=8, name='Gilad')
    backend_test.test_create_user()
    backend_test.test_get_user()
    backend_test.test_put_user()
    backend_test.test_clean_user()
