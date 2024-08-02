import mysql.connector
from mysql.connector import Error
import time
import csv

def execute_sql_from_file(file_path):
    connection = None
    cursor = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='sm'  # Specify the database if needed
        )

        if connection.is_connected():
            cursor = connection.cursor()
            with open(file_path, 'r') as file:
                sql = file.read()

            # Execute each query in the file
            for query in sql.split(';'):
                query = query.strip()
                if query:
                    start_time = time.time()  # Record the start time
                    try:
                        cursor.execute(query)
                        # Handle different types of queries
                        if query.lower().startswith('select') or query.lower().startswith('show'):
                            # Fetch and print results for SELECT and SHOW queries
                            results = cursor.fetchall()
                            columns = [i[0] for i in cursor.description]
                            print(f"Results for query: {query}")
                            print(columns)
                            for row in results:
                                print(row)
                            
                            # Write results to CSV
                            csv_file_path = 'C:\\Users\\Administrator\\temp2\\2407-Ferry\\query_results.csv'
                            with open(csv_file_path, mode='w', newline='') as csv_file:
                                writer = csv.writer(csv_file)
                                writer.writerow(columns)  # Write column headers
                                writer.writerows(results)  # Write data rows
                            print(f"Results saved to {csv_file_path}")
                        else:
                            # For other queries like CREATE, INSERT, etc.
                            print(f"Query executed successfully: {query}")
                        
                        connection.commit()
                    except Error as e:
                        print(f"Error executing query: {e}")
                    finally:
                        # Handle any remaining results
                        if connection.unread_result:
                            connection.handle_unread_result()
                    
                    end_time = time.time()  # Record the end time
                    execution_time = end_time - start_time
                    print(f"Query execution time: {execution_time:.2f} seconds")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Call the function with the path to your SQL file
execute_sql_from_file('C:\\Users\\Administrator\\temp2\\2407-Ferry\\queries.sql')
