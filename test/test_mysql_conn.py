import unittest
from unittest.mock import patch, MagicMock
import mysql.connector
from mysql_conn import SQLExecutor 


class TestSQLExecutor(unittest.TestCase):
    @patch('mysql.connector.connect')
    def setUp(self, mock_connect):
        # Mock the database connection and cursor
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.is_connected.return_value = True
        mock_connect.return_value = self.mock_connection
        self.mock_connection.cursor.return_value = self.mock_cursor

        # Initialize SQLExecutor
        self.executor = SQLExecutor(
            host='localhost',
            user='root',
            password='root'
        )

    def test_connect(self):
        self.executor.connect()
        print("test_connect passed")

    def test_close(self):
        self.executor.connect()
        self.executor.close()
        print("test_close passed")

if __name__ == '__main__':
    unittest.main()



