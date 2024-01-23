import unittest
from backend_testing import BackEndTests
from frontend_testing import FrontEndTests


class CombinedTests(unittest.TestCase):
    user_id = 7
    name = 'dad'
    """Combines backend and frontend tests for comprehensive coverage."""
    backend = BackEndTests(user_id, name)

    def test_backend_functionality(self):
        """Tests backend operations for posting, retrieving users, and data integrity."""
        self.backend.check_post()
        self.backend.get_user()
        self.backend.check_data()

    def test_frontend_display(self):
        """Tests frontend display of usernames."""
        frontend = FrontEndTests(self.user_id)
        frontend.check_name()

    @classmethod
    def tearDownClass(cls):
        """Performs cleanup after each test."""
        cls.backend.clean_user()


if __name__ == "__main__":
    unittest.main()
