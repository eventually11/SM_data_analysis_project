import json
import mysql.connector
from mysql.connector import Error
from saas_partner_order_strategy_data_generation import saas_partner_order_strategy
from hypothesis import given
import pandas as pd

class OrderDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")
            self.connection = None
            self.cursor = None

    def insert_order(self, order):
        if self.connection is None or self.cursor is None:
            print("Not connected to the database.")
            return

        try:
            insert_query = """
            INSERT INTO saas_partner_order (
                order_id, tenant, flow, sender, hub, dispatch_pool, vehicle_type, start_time, end_time, title, 
                route_description, tags, overview, content, type, start, end, service_fee, 
                start_task_validation, end_task_validation, status_group
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            vehicle_type_str = json.dumps(order['vehicle_type'])
            type_dict_str = json.dumps(order['type'])

            values = (
                order['order_id'], order['tenant'], order['flow'], order['sender'], order['hub'], 
                order['dispatch_pool'], vehicle_type_str, order['start_time'], order['end_time'], 
                order['title'], order['route_description'], order['tags'], order['overview'], 
                order['content'], type_dict_str, order['start'], order['end'], order['service_fee'],
                order['start_task_validation'], order['end_task_validation'], order['status_group']
            )
            self.cursor.execute(insert_query, values)
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

def create_dataframe_from_order(order):
    df = pd.DataFrame([order])
    return df

df_order = None

@given(saas_partner_order_strategy())
def print_and_insert_order(order):
    global df_order
    df_order = create_dataframe_from_order(order)
    print(df_order)

    db = OrderDatabase(host='localhost', user='root', password='root', database='sm')
    db.connect()
    db.insert_order(order)
    db.close()

# Example usage
if __name__ == "__main__":
    print_and_insert_order()
    # 打印全局变量 df_order，以便在外部可以看到它
    print("Generated DataFrame:")
    print(df_order)
