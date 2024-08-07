import json
import mysql.connector
from datetime import datetime
from hypothesis import given, settings, HealthCheck
from hypothesis.strategies import integers, text, composite
import csv

@composite
def saas_partner_order_type_strategy(draw):
    return {
        'code': draw(integers(min_value=1000, max_value=9999)),  # Test code: integer, range 1000-9999
        'type_name': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),  # Test type_name: string
        'name': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))  # Test name: string
    }

def validate_saas_partner_order_type(order_type):
    test_results = {}

    def add_result(field, test_type, result):
        test_results[field] = {"test_type": test_type, "result": result}

    try:
        assert isinstance(order_type['code'], int) and 1000 <= order_type['code'] <= 9999
        add_result('code', 'integer in range 1000-9999', 'pass')
    except AssertionError:
        add_result('code', 'integer in range 1000-9999', 'fail')

    try:
        assert isinstance(order_type['type_name'], str) and len(order_type['type_name']) >= 1
        add_result('type_name', 'non-empty string', 'pass')
    except AssertionError:
        add_result('type_name', 'non-empty string', 'fail')

    try:
        assert isinstance(order_type['name'], str) and len(order_type['name']) >= 1
        add_result('name', 'non-empty string', 'pass')
    except AssertionError:
        add_result('name', 'non-empty string', 'fail')

    return test_results

def insert_into_mysql(order_type):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='sm'
        )
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO saas_partner_order_type (code, type_name, languages)
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (order_type['code'], order_type['type_name'], order_type['name']))
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as error:
        print(f"Failed to insert data into MySQL table: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

@settings(suppress_health_check=[HealthCheck.return_value])
@given(saas_partner_order_type_strategy())
def test_insert_into_mysql(order_type):
    validate_results = validate_saas_partner_order_type(order_type)
    for result in validate_results.values():
        if result['result'] == 'fail':
            print(f"Validation failed for field: {result['field']}, test type: {result['test_type']}")
            return
    print(f"Generated order_type: {order_type}")
    insert_into_mysql(order_type)

if __name__ == "__main__":
    generated_data = []
    unique_validation_results = {}

    for _ in range(10):  # Generate and insert 10 examples
        example = saas_partner_order_type_strategy().example()
        validate_results = validate_saas_partner_order_type(example)
        for result in validate_results.values():
            if result['result'] == 'fail':
                print(f"Validation failed for field: {result['field']}, test type: {result['test_type']}")
                continue
        insert_into_mysql(example)
        generated_data.append((example, validate_results))
        
        for field, result in validate_results.items():
            unique_validation_results[field] = result

    print("Generated data:")
    for data in generated_data:
        print(data[0])

    # Save the unique validation results to CSV
    csv_file_path = 'C:\\Users\\Administrator\\temp2\\2407-Ferry\\saas_partner_order_type_testreport.csv'
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['field', 'test_type', 'result'])  # Write column headers
        for field, result in unique_validation_results.items():
            writer.writerow([field, result['test_type'], result['result']])  # Write unique validation results rows
    print(f"Validation results saved to {csv_file_path}")
