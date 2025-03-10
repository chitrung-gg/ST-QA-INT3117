import unittest

def calculate_shipping_fee(x: float, y: float, z: int) -> float:
    if not (0 < x <= 1000) or not (0 < y <= 100) or not (0 < z <= 24): 
        return "Input không hợp lệ"

    x, y = round(x, 2), round(y, 2)
    if x < 10:
        distance_fee = x * 5000
    elif x < 50:
        distance_fee = x * 4500
    else:
        distance_fee = x * 4000
    
    weight_fee = 50000 if y >= 10 else 0
    time_fee = 50000 if z < 12 else 0
    
    return distance_fee + weight_fee + time_fee

class TestShippingFee(unittest.TestCase):
    def test_cases_decision_table(self):
        test_data = [
            (1000.01, 16.12, 22, "Input không hợp lệ"),
            (26, -1.25, 14, "Input không hợp lệ"),
            (38, 2.47, 25, "Input không hợp lệ"),
            (2.65, 6.25, 8, 63250),
            (8.2, 5.81, 16, 41000),
            (0.01, 12.69, 3, 100050),
            (1.23, 23.47, 17, 56150),
            (12.35, 1.26, 5, 105575),
            (15.24, 3.36, 14, 68580),
            (25.16, 15.23, 2, 213220),
            (49.99, 12.03, 18, 274955),
            (52.68, 6.23, 4, 260720),
            (50.01, 2.35, 20, 200040),
            (999.99, 13, 6, 4099960),
            (156.14, 20, 22, 674560),
        ]
        
        for x, y, z, expected in test_data:
            with self.subTest(x=x, y=y, z=z):
                self.assertEqual(calculate_shipping_fee(x, y, z), expected)

    def test_cases_boundary_value(self):
        test_data = [
            (15.25, 5.65, 10, 118625),
            (15.25, 5.65, 1, 118625),
            (15.25, 5.65, 24, 68625),
            (15.25, 5.65, 2, 118625),
            (15.25, 5.65, 23, 68625),
            (15.25, 5.65, 0, "Input không hợp lệ"),
            (15.25, 5.65, 25, "Input không hợp lệ"),
            (15.25, 0.01, 10, 118625),
            (15.25, 100, 10, 168625),
            (15.25, 0.02, 10, 118625),
            (15.25, 99.99, 10, 168625),
            (15.25, 0, 10, "Input không hợp lệ"),
            (15.25, 100.01, 10, "Input không hợp lệ"),
            (0.01, 5.65, 10, 50050),
            (1000, 5.65, 10, 4050000),
            (0.02, 5.65, 10, 50100),
            (999.99, 5.65, 10, 4049960),
            (0, 5.65, 10, "Input không hợp lệ"),
            (1000.01, 5.65, 10, "Input không hợp lệ"),
        ]
        
        for x, y, z, expected in test_data:
            with self.subTest(x=x, y=y, z=z):
                self.assertEqual(calculate_shipping_fee(x, y, z), expected)

if __name__ == "__main__":
    unittest.main()
