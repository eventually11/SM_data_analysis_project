import mysql.connector
from mysql.connector import Error
import time
import csv
import os

class SQLExecutor:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        # Get the current script's directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.current_dir, 'queries.sql')
        self.csv_file_path = os.path.join(self.current_dir, 'query_results.csv')
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

    def execute_sql_from_file(self):
        try:
            self.connect()
            if self.connection.is_connected():
                with open(self.file_path, 'r') as file:
                    sql = file.read()

                # Execute each query in the file
                for query in sql.split(';'):
                    query = query.strip()
                    if query:
                        start_time = time.time()  # Record the start time
                        try:
                            self.cursor.execute(query)
                            # Handle different types of queries
                            if query.lower().startswith('select') or query.lower().startswith('show'):
                                # Fetch and print results for SELECT and SHOW queries
                                results = self.cursor.fetchall()
                                columns = [i[0] for i in self.cursor.description]
                                print(f"Results for query: {query}")
                                print(columns)
                                for row in results:
                                    print(row)
                                
                                # Write results to CSV
                                with open(self.csv_file_path, mode='w', newline='') as csv_file:
                                    writer = csv.writer(csv_file)
                                    writer.writerow(columns)  # Write column headers
                                    writer.writerows(results)  # Write data rows
                                print(f"Results saved to {self.csv_file_path}")
                            else:
                                # For other queries like CREATE, INSERT, etc.
                                print(f"Query executed successfully: {query}")
                            
                            self.connection.commit()
                        except Error as e:
                            print(f"Error executing query: {e}")
                        finally:
                            # Handle any remaining results
                            if self.connection.unread_result:
                                self.connection.handle_unread_result()
                        
                        end_time = time.time()  # Record the end time
                        execution_time = end_time - start_time
                        print(f"Query execution time: {execution_time:.2f} seconds")

        except Error as e:
            print(f"Error: {e}")
        finally:
            self.close()

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

# Usage
if __name__ == '__main__':
    executor = SQLExecutor(
        host='localhost',
        user='root',
        password='root'
    )
    executor.execute_sql_from_file()
