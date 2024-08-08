# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:32:29 2024

@author: Administrator
"""

import pandas as pd
from faker import Faker
import random
from hypothesis.strategies import integers, text, floats, composite, datetimes, timedeltas
from datetime import datetime, timedelta
from hypothesis import given
from open_street_map_API import OpenStreetMapAPI

class SaasTaskDataGenerator:
    """
    A class to generate SaaS partner orders using the hypothesis library and convert the results to a Pandas DataFrame.

    Methods
    -------
    saas_partner_order_strategy()
        Strategy to generate SaaS partner orders.
    
    generate_orders(num_orders)
        Generates a specified number of orders and returns them as a Pandas DataFrame.
    """
    
    def __init__(self):
        self.fake = Faker()
        self.task_id_list = list(range(10000000, 100000000))
        self.order_id_list = list(range(1000000, 10000000))
        random.shuffle(self.order_id_list)  # Shuffle to randomize order
        osm_api = OpenStreetMapAPI()
        query = 'restaurant'  # Search keyword
        latitude = -12.4634  # Latitude of Darwin
        longitude = 130.8456  # Longitude of Darwin
        radius = 1  # Search radius in degrees 
        places = osm_api.get_places(query, latitude, longitude, radius)
        df_restaurants = osm_api.convert_to_dataframe(places)
        self.address_pool = df_restaurants['name'].tolist()

    @composite
    def saas_task_data(draw, self):
        service_fee = round(draw(floats(min_value=0.01, max_value=10000.0)), 2)
        
        min_datetime = datetime(2020, 1, 1)
        max_datetime = datetime(2024, 12, 31)

        start_time = draw(datetimes(min_value=min_datetime, max_value=max_datetime))
        min_duration = timedelta(minutes=2)
        max_duration = timedelta(hours=1)
        end_time = start_time + draw(timedeltas(min_value=min_duration, max_value=max_duration))

        start_address = random.choice(self.address_pool)
        end_address = random.choice(self.address_pool)
        while end_address == start_address:
            end_address = random.choice(self.address_pool)

        return {
            'task_id': self.task_id_list.pop(),
            'tenant': draw(integers(min_value=1, max_value=1000)),
            'order_id': random.choice(self.order_id_list),
            'sender': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'hub': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'zone': draw(integers(min_value=1, max_value=100)),
            'flow': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'task_pool': draw(integers(min_value=1, max_value=1000)),
            'partner': draw(integers(min_value=1, max_value=1000)),
            'title': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'content': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'date': start_time,
            'time_slot': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'type': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'service_time': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'start': start_address,
            'end': end_address,
            'service_fee': service_fee,
            'items': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'start_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'end_task_validation': draw(text(min_size=1, alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')),
            'status_code': draw(integers(min_value=1, max_value=10)),
            'status_group': draw(integers(min_value=1, max_value=10))
        }

    def generate_orders(self, num_orders):
        """
        Generates a specified number of orders and returns them as a Pandas DataFrame.

        Parameters
        ----------
        num_orders : int
            The number of orders to generate.

        Returns
        -------
        DataFrame
            A Pandas DataFrame containing the generated orders.
        """
        orders = []

        @given(self.saas_task_data())
        def collect_order(order):
            orders.append(order)

        for _ in range(num_orders):
            collect_order()

        df = pd.DataFrame(orders)
        return df

# Example usage
if __name__ == "__main__":
    generator = SaasTaskDataGenerator()
    df_orders = generator.generate_orders(10)
    print(df_orders)
