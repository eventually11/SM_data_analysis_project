from faker import Faker
import random
from hypothesis.strategies import integers, text, lists, floats, composite, datetimes
from datetime import datetime

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
if __name__ == "__main__":
    from hypothesis import given

    @given(saas_partner_order_strategy())
    def print_saas_partner_order(order):
        print(order)

    print_saas_partner_order()