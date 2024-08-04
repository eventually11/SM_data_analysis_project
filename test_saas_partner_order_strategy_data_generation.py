from datetime import datetime



class OrderValidator:
    def __init__(self, order):
        self.order = order
        self.test_results = []

    def add_result(self, field, test_type, result):
        self.test_results.append({"field": field, "test_type": test_type, "result": result})

    def validate(self):
        if 'order_id' in self.order:
            try:
                assert isinstance(self.order['order_id'], int)
                self.add_result('order_id', 'integer', 'pass')
            except AssertionError:
                self.add_result('order_id', 'integer', 'fail')

        if 'tenant' in self.order:
            try:
                assert isinstance(self.order['tenant'], int)
                self.add_result('tenant', 'integer', 'pass')
            except AssertionError:
                self.add_result('tenant', 'integer', 'fail')

        if 'flow' in self.order:
            try:
                assert isinstance(self.order['flow'], int)
                self.add_result('flow', 'integer', 'pass')
            except AssertionError:
                self.add_result('flow', 'integer', 'fail')

        if 'sender' in self.order:
            try:
                assert isinstance(self.order['sender'], str)
                self.add_result('sender', 'string', 'pass')
            except AssertionError:
                self.add_result('sender', 'string', 'fail')

        if 'hub' in self.order:
            try:
                assert isinstance(self.order['hub'], str)
                self.add_result('hub', 'string', 'pass')
            except AssertionError:
                self.add_result('hub', 'string', 'fail')

        if 'dispatch_pool' in self.order:
            try:
                assert isinstance(self.order['dispatch_pool'], int)
                self.add_result('dispatch_pool', 'integer', 'pass')
            except AssertionError:
                self.add_result('dispatch_pool', 'integer', 'fail')

        if 'vehicle_type' in self.order:
            try:
                assert isinstance(self.order['vehicle_type'], list) and all(isinstance(vt, str) for vt in self.order['vehicle_type'])
                self.add_result('vehicle_type', 'list of strings', 'pass')
            except AssertionError:
                self.add_result('vehicle_type', 'list of strings', 'fail')

        if 'start_time' in self.order:
            try:
                assert self.order['start_time'] is None or isinstance(self.order['start_time'], datetime)
                self.add_result('start_time', 'datetime or None', 'pass')
            except AssertionError:
                self.add_result('start_time', 'datetime or None', 'fail')

        if 'end_time' in self.order:
            try:
                assert self.order['end_time'] is None or isinstance(self.order['end_time'], datetime)
                self.add_result('end_time', 'datetime or None', 'pass')
            except AssertionError:
                self.add_result('end_time', 'datetime or None', 'fail')

        if 'title' in self.order:
            try:
                assert isinstance(self.order['title'], str)
                self.add_result('title', 'string', 'pass')
            except AssertionError:
                self.add_result('title', 'string', 'fail')

        if 'route_description' in self.order:
            try:
                assert isinstance(self.order['route_description'], str)
                self.add_result('route_description', 'string', 'pass')
            except AssertionError:
                self.add_result('route_description', 'string', 'fail')

        if 'tags' in self.order:
            try:
                assert self.order['tags'] is None or isinstance(self.order['tags'], str)
                self.add_result('tags', 'string or None', 'pass')
            except AssertionError:
                self.add_result('tags', 'string or None', 'fail')

        if 'overview' in self.order:
            try:
                assert isinstance(self.order['overview'], str)
                self.add_result('overview', 'string', 'pass')
            except AssertionError:
                self.add_result('overview', 'string', 'fail')

        if 'content' in self.order:
            try:
                assert isinstance(self.order['content'], str)
                self.add_result('content', 'string', 'pass')
            except AssertionError:
                self.add_result('content', 'string', 'fail')

        if 'type' in self.order:
            try:
                assert isinstance(self.order['type'], dict)
                assert isinstance(self.order['type']['code'], int)
                assert isinstance(self.order['type']['type_name'], str)
                assert isinstance(self.order['type']['name'], str)
                self.add_result('type', 'dictionary with code, type_name, and name', 'pass')
            except AssertionError:
                self.add_result('type', 'dictionary with code, type_name, and name', 'fail')

        if 'start' in self.order:
            try:
                assert self.order['start'] is None or isinstance(self.order['start'], str)
                self.add_result('start', 'string or None', 'pass')
            except AssertionError:
                self.add_result('start', 'string or None', 'fail')

        if 'end' in self.order:
            try:
                assert self.order['end'] is None or isinstance(self.order['end'], str)
                self.add_result('end', 'string or None', 'pass')
            except AssertionError:
                self.add_result('end', 'string or None', 'fail')

        if 'service_fee' in self.order:
            try:
                assert self.order['service_fee'] is None or isinstance(self.order['service_fee'], float)
                self.add_result('service_fee', 'float or None', 'pass')
            except AssertionError:
                self.add_result('service_fee', 'float or None', 'fail')

        if 'start_task_validation' in self.order:
            try:
                assert isinstance(self.order['start_task_validation'], str)
                self.add_result('start_task_validation', 'string', 'pass')
            except AssertionError:
                self.add_result('start_task_validation', 'string', 'fail')

        if 'end_task_validation' in self.order:
            try:
                assert isinstance(self.order['end_task_validation'], str)
                self.add_result('end_task_validation', 'string', 'pass')
            except AssertionError:
                self.add_result('end_task_validation', 'string', 'fail')

        if 'status_group' in self.order:
            try:
                assert isinstance(self.order['status_group'], int)
                self.add_result('status_group', 'integer', 'pass')
            except AssertionError:
                self.add_result('status_group', 'integer', 'fail')

        return self.test_results

if __name__ == "__main__":
    order = {
        # Example order data
    }
    validator = OrderValidator(order)
    results = validator.validate()
    print(results)