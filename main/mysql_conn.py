import mysql.connector
from mysql.connector import Error
import csv

class SQLExecutor:
    def __init__(self, host, user, password, queries_file, csv_file_path):
        self.host = host
        self.user = user
        self.password = password
        self.queries_file = queries_file
        self.csv_file_path = csv_file_path
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("MySQL connection is established")
        except Error as e:
            print(f"Error: {e}")

    def execute_query(self, query):
        try:
            if self.connection.is_connected():
                print(f"Executing query: {query}")
                self.cursor.execute(query)
                if query.strip().lower().startswith('select'):
                    results = self.cursor.fetchall()
                    if results:
                        columns = [i[0] for i in self.cursor.description]
                        with open(self.csv_file_path, mode='w', newline='') as csv_file:
                            writer = csv.writer(csv_file)
                            writer.writerow(columns)  # Write column headers
                            writer.writerows(results)  # Write data rows
                        print(f"Results saved to {self.csv_file_path}")
                    else:
                        print("No results to save")
                else:
                    self.connection.commit()
                    print("Query executed successfully")
        except Error as e:
            print(f"Error: {e}")

    def execute_queries_from_file(self):
        try:
            self.connect()
            if self.connection.is_connected():
                with open(self.queries_file, 'r') as file:
                    queries = file.read().strip().split(';')
                    for query in queries:
                        if query.strip():  # Skip empty queries
                            self.execute_query(query.strip() + ';')
        except FileNotFoundError:
            print(f"File not found: {self.queries_file}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

# Usage
if __name__ == '__main__':
    executor = SQLExecutor(
        host='localhost',
        user='root',
        password='root',
        queries_file='queries.sql',  # Ensure this is the path to your queries file
        csv_file_path='query_results_saas_partner_order.csv'   # Ensure this is the path for the output CSV file
    )
    
    executor.execute_queries_from_file()
