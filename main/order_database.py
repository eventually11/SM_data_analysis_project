# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:23:20 2024

@author: Administrator
"""
from saas_partner_order_strategy_data_generation import SaasPartnerOrderGenerator
from mysql_conn import SQLExecutor
import time

class OrderDatabase:
    def __init__(self):
        self.df_orders = None
    
    def generate(self):
        generator = SaasPartnerOrderGenerator()
        self.df_orders = generator.generate_orders(10)
        print(self.df_orders)
        return self.df_orders
        
    def write_to_sql_file(self, file_path):
        if self.df_orders is None:
            raise ValueError("No orders to write to the database. Please generate orders first.")
        
        with open(file_path, 'w') as f:
            for _, order in self.df_orders.iterrows():
                insert_query = """
                INSERT INTO sm.saas_partner_order (
                    order_id, tenant, flow, sender, hub, dispatch_pool, vehicle_type, start_time, end_time, title, 
                    route_description, tags, overview, content, `type`, `start`, `end`, service_fee, 
                    start_task_validation, end_task_validation, status_group
                ) VALUES ({}, {}, {}, "{}", "{}", {}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", {}, "{}", "{}", {});
                """.format(
                order['order_id'], order['tenant'], order['flow'], order['sender'], order['hub'], 
                order['dispatch_pool'], order['vehicle_type'], order['start_time'], order['end_time'], 
                order['title'], order['route_description'], order['tags'], order['overview'], 
                order['content'], order['type'], order['start'], order['end'], order['service_fee'],
                order['start_task_validation'], order['end_task_validation'], order['status_group']
                )                
                f.write(insert_query + '\n')  

        print(f"SQL queries written to {file_path}")

    def execute_sql_file(self, file_path):
        executor = SQLExecutor(
            host='localhost',
            user='root',
            password='root',
            queries_file=file_path,
            csv_file_path='query_results_saas_partner_order.csv'
        )
        executor.execute_queries_from_file


if __name__ == "__main__":
    order_db = OrderDatabase()
    df_order = order_db.generate()
    sql_file_path = 'queries_insert_saas_partner_order.sql'
    order_db.write_to_sql_file(sql_file_path)
    order_db.execute_sql_file(sql_file_path)
