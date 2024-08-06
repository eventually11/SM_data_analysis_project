# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:10:43 2024

@author: Administrator
"""

# Test if the distance and duration are correctly returned and are greater than 0

import unittest
from OSRM_route_calculator import OSRMRouteCalculator

class TestOSRMRouteCalculator(unittest.TestCase):
    def setUp(self):
        self.start_lat = 39.9087
        self.start_lng = 116.3975
        self.end_lat = 39.9163
        self.end_lng = 116.3971
        self.calculator = OSRMRouteCalculator(self.start_lat, self.start_lng, self.end_lat, self.end_lng)

    def test_get_route_info(self):
        distance, duration = self.calculator.get_route_info()
        self.assertIsNotNone(distance, "Distance should not be None")
        self.assertIsNotNone(duration, "Duration should not be None")
        self.assertGreater(distance, 0, "Distance should be greater than 0")
        self.assertGreater(duration, 0, "Duration should be greater than 0")

if __name__ == "__main__":
    unittest.main()
