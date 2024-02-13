import datetime
import pymysql
import os


class DBConnector:

    def __init__(self, host='localhost', port=3306, user='root', passwd='pythoncourse', db='MyDB_AdvancedProject'):
        try:
            self.db = db
            self.host = os.environ.get("database_host") or host
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

    # This function add a new user to the DB
    def add_user(self, user_id, user_name):
        creation_date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (user_name, user_id, creation_date) VALUES (%s, %s, %s)",
                           (user_name, user_id, creation_date))  # Prepared statement
            self.conn.commit()
            num_affected_rows = cursor.rowcount
            if num_affected_rows > 0:
                return 200

    # This function get the User ID and return the Username
    def get_user(self, user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT user_name FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
        return result[0]
    # def select_id(self, user_id):
    #     try:
    #         with self.conn.cursor() as cursor:
    #             cursor.execute("SELECT user_name FROM users WHERE user_id = %s", (user_id,))
    #             result = cursor.fetchone()
    #         return result[0]  # Assuming a single result is expected
    #     except pymysql.Error as e:
    #         print(f"Error selecting user_id: {e}")
    #         raise

    # This function is updating the user in the DB, after PUT REST API method.
    def update_user(self, user_id, new_name):
        with self.conn.cursor() as cursor:  # Use context manager for cursor
            cursor.execute("UPDATE users SET user_name = %s WHERE user_id = %s",
                           (new_name, user_id))  # Prepared statement
        self.conn.commit()

    # This function delete the user from the DB
    def delete_user(self, user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        self.conn.commit()
        return 200

    def __del__(self):
        self.conn.close()  # Close connection when object is destroyed