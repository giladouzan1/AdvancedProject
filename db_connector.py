import datetime
import pymysql


class DBConnector:

    def __init__(self, host='host.docker.internal', port=3306, user='root', passwd='pythoncourse', db='MyDB_AdvancedProject'):
        try:
            self.db = db
            self.host = host
            self.port = port
            self.user = user
            self.passwd = passwd
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db)
            with self.conn.cursor() as cursor:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INT PRIMARY KEY,
                    user_name VARCHAR(50) NOT NULL,
                    creation_date VARCHAR(50) NOT NULL
                );
            """)
                self.conn.commit()

        except pymysql.Error as e:
            print(f"Error during database connection: {e}")
            raise  # Raising the exception to notify the calling code about the error

    # This function check if a user exist in the DB and return True or the error
    def user_exists(self, user_id):
        try:
             query = "SELECT * FROM users WHERE user_id = %s"
             self.cursor.execute(query, (user_id,))
             return bool(self.cursor.fetchone())
        except pymysql.Error as e:
            print(f"Error checking if user exists: {e}")
            raise

    # This function add a new user to the DB
    def add_user(self, user_id, user_name):
        try:
            creation_date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
            query = "INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s,%s)"
            print(creation_date)
            self.cursor.execute(query, (user_id, user_name, creation_date))
            self.conn.commit()
        except pymysql.Error as e:
            print(f"Error adding user: {e}")
            raise

    # This function get the User ID and return the Username
    def get_user(self, user_id):
        try:
            query = "SELECT user_name FROM users WHERE user_id = %s"
            self.cursor.execute(query, (user_id,))
            return self.cursor.fetchone()

        except pymysql.Error as e:
            print(f"Error getting user: {e}")
            raise

    def select_id(self, user_id):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT user_name FROM users WHERE user_id = %s", (user_id,))
                result = cursor.fetchone()
            return result[0]  # Assuming a single result is expected
        except pymysql.Error as e:
            print(f"Error selecting user_id: {e}")
            raise

    # This function is updating the user in the DB, after PUT REST API method.
    def update_user(self, user_id, user_name):
        try:
            if self.user_exists(user_id):
                query = "UPDATE users SET user_name = %s WHERE user_id = %s"
                self.cursor.execute(query, (user_name, user_id))
                self.conn.commit()
                return True
            else:
                return False
        except pymysql.Error as e:
            print(f"Error updating user: {e}")
            raise

    # This function delete the user from the DB
    def delete_user(self, user_id):
        try:
            if self.user_exists(user_id):
                query = "DELETE FROM users WHERE user_id = %s"
                self.cursor.execute(query, (user_id,))
                self.conn.commit()
                return True
            else:
                return False
        except pymysql.Error as e:
            print(f"Error deleting user: {e}")
            raise
