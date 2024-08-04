from faker import Faker
import random
from hypothesis import settings, example
from hypothesis.strategies import integers, text, lists, floats, composite, datetimes, one_of, none
import csv
from datetime import datetime
import json
import mysql.connector
from mysql.connector import Error


fake = Faker()

@composite
def saas_partner_order_strategy(draw):
    service_fee = round(draw(floats(min_value=0.01, max_value=10000.0)), 2)
    
    min_datetime = datetime(2020, 1, 1)
    max_datetime = datetime(2024, 12, 31)

    return {
        'order_id': draw(integers(min_value=1, max_value=10000)),
        'tenant': draw(integers(min_value=1, max_value=1000)),
        'flow': draw(integers(min_value=1, max_value=100)),
        'sender': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'hub': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'dispatch_pool': draw(integers(min_value=1, max_value=100)),
        'vehicle_type': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'start_time': draw(datetimes(min_value=min_datetime, max_value=max_datetime)),
        'end_time': draw(datetimes(min_value=min_datetime, max_value=max_datetime)),
        'title': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'route_description': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'tags': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'overview': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'content': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'type': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'start': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'end': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'service_fee': service_fee,
        'start_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'end_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
        'status_group': draw(integers(min_value=1, max_value=10))
    }

def validate_saas_partner_order(order):
    test_results = []

    def add_result(field, test_type, result):
        test_results.append({"field": field, "test_type": test_type, "result": result})

    if 'order_id' in order:
        try:
            assert isinstance(order['order_id'], int)
            add_result('order_id', 'integer', 'pass')
        except AssertionError:
            add_result('order_id', 'integer', 'fail')
    
    if 'tenant' in order:
        try:
            assert isinstance(order['tenant'], int)
            add_result('tenant', 'integer', 'pass')
        except AssertionError:
            add_result('tenant', 'integer', 'fail')

    if 'flow' in order:
        try:
            assert isinstance(order['flow'], int)
            add_result('flow', 'integer', 'pass')
        except AssertionError:
            add_result('flow', 'integer', 'fail')

    if 'sender' in order:
        try:
            assert isinstance(order['sender'], str)
            add_result('sender', 'string', 'pass')
        except AssertionError:
            add_result('sender', 'string', 'fail')
    
    if 'hub' in order:
        try:
            assert isinstance(order['hub'], str)
            add_result('hub', 'string', 'pass')
        except AssertionError:
            add_result('hub', 'string', 'fail')

    if 'dispatch_pool' in order:
        try:
            assert isinstance(order['dispatch_pool'], int)
            add_result('dispatch_pool', 'integer', 'pass')
        except AssertionError:
            add_result('dispatch_pool', 'integer', 'fail')

    if 'vehicle_type' in order:
        try:
            assert isinstance(order['vehicle_type'], list) and all(isinstance(vt, str) for vt in order['vehicle_type'])
            add_result('vehicle_type', 'list of strings', 'pass')
        except AssertionError:
            add_result('vehicle_type', 'list of strings', 'fail')

    if 'start_time' in order:
        try:
            assert order['start_time'] is None or isinstance(order['start_time'], datetime)
            add_result('start_time', 'datetime or None', 'pass')
        except AssertionError:
            add_result('start_time', 'datetime or None', 'fail')

    if 'end_time' in order:
        try:
            assert order['end_time'] is None or isinstance(order['end_time'], datetime)
            add_result('end_time', 'datetime or None', 'pass')
        except AssertionError:
            add_result('end_time', 'datetime or None', 'fail')

    if 'title' in order:
        try:
            assert isinstance(order['title'], str)
            add_result('title', 'string', 'pass')
        except AssertionError:
            add_result('title', 'string', 'fail')

    if 'route_description' in order:
        try:
            assert isinstance(order['route_description'], str)
            add_result('route_description', 'string', 'pass')
        except AssertionError:
            add_result('route_description', 'string', 'fail')

    if 'tags' in order:
        try:
            assert order['tags'] is None or isinstance(order['tags'], str)
            add_result('tags', 'string or None', 'pass')
        except AssertionError:
            add_result('tags', 'string or None', 'fail')

    if 'overview' in order:
        try:
            assert isinstance(order['overview'], str)
            add_result('overview', 'string', 'pass')
        except AssertionError:
            add_result('overview', 'string', 'fail')

    if 'content' in order:
        try:
            assert isinstance(order['content'], str)
            add_result('content', 'string', 'pass')
        except AssertionError:
            add_result('content', 'string', 'fail')

    if 'type' in order:
        try:
            assert isinstance(order['type'], dict)
            assert isinstance(order['type']['code'], int)
            assert isinstance(order['type']['type_name'], str)
            assert isinstance(order['type']['name'], str)
            add_result('type', 'dictionary with code, type_name, and name', 'pass')
        except AssertionError:
            add_result('type', 'dictionary with code, type_name, and name', 'fail')

    if 'start' in order:
        try:
            assert order['start'] is None or isinstance(order['start'], str)
            add_result('start', 'string or None', 'pass')
        except AssertionError:
            add_result('start', 'string or None', 'fail')

    if 'end' in order:
        try:
            assert order['end'] is None or isinstance(order['end'], str)
            add_result('end', 'string or None', 'pass')
        except AssertionError:
            add_result('end', 'string or None', 'fail')

    if 'service_fee' in order:
        try:
            assert order['service_fee'] is None or isinstance(order['service_fee'], float)
            add_result('service_fee', 'float or None', 'pass')
        except AssertionError:
            add_result('service_fee', 'float or None', 'fail')

    if 'start_task_validation' in order:
        try:
            assert isinstance(order['start_task_validation'], str)
            add_result('start_task_validation', 'string', 'pass')
        except AssertionError:
            add_result('start_task_validation', 'string', 'fail')

    if 'end_task_validation' in order:
        try:
            assert isinstance(order['end_task_validation'], str)
            add_result('end_task_validation', 'string', 'pass')
        except AssertionError:
            add_result('end_task_validation', 'string', 'fail')

    if 'status_group' in order:
        try:
            assert isinstance(order['status_group'], int)
            add_result('status_group', 'integer', 'pass')
        except AssertionError:
            add_result('status_group', 'integer', 'fail')

    return test_results

def insert_order_into_db(order):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='sm'
        )
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO saas_partner_order (
            order_id, tenant, flow, sender, hub, dispatch_pool, vehicle_type, start_time, end_time, title, 
            route_description, tags, overview, content, type, start, end, service_fee, 
            start_task_validation, end_task_validation, status_group
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        vehicle_type_str = json.dumps(order['vehicle_type'])
        type_dict_str = json.dumps(order['type'])

        data_tuple = (
            order['order_id'], order['tenant'], order['flow'], order['sender'], order['hub'], order['dispatch_pool'], vehicle_type_str,
            order['start_time'], order['end_time'], order['title'], order['route_description'], order['tags'], order['overview'],
            order['content'], type_dict_str, order['start'], order['end'], order['service_fee'],
            order['start_task_validation'], order['end_task_validation'], order['status_group']
        )

        if order['service_fee'] is not None and (order['service_fee'] < 0.0 or order['service_fee'] > 10000.0):
            raise ValueError("service_fee out of range")

        cursor.execute(insert_query, data_tuple)
        connection.commit()

    except mysql.connector.Error as error:
        print(f"Failed to insert record into MySQL table: {error}")
    except ValueError as ve:
        print(f"Validation error: {ve}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    results = []
    strategy = saas_partner_order_strategy()
    for _ in range(10):
        example = strategy.example()
        test_results = validate_saas_partner_order(example)
        results.extend(test_results)
        # Insert the generated order into MySQL database
        insert_order_into_db(example)

    with open(r"C:\Users\Administrator\temp2\2407-Ferry\test_report.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["field", "test_type", "result"])
        for result in results:
            writer.writerow([result["field"], result["test_type"], result["result"]])

    print("Test report generated in 'C:\\Users\\Administrator\\temp2\\2407-Ferry\\test_report.csv'")
