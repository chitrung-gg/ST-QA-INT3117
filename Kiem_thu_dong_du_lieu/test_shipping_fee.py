import unittest
from calculate_shipping_fee import calculate_shipping_fee

class TestShippingFee(unittest.TestCase):
    def test_cases_branch_coverage(self):
        test_data = [
            (-15.42, 10, 12, "Invalid Input"),
            (100.5, 100.01, 12, "Invalid Input"),
            (52.36, 10, -1, "Invalid Input"),
            (9.08, 12.4, 11, 145400),
            (6.43, 15, 4, 132150),
            (40.05, 8.75, 18, 180225),
            (25, 5.13, 20, 112500),
            (125.25, 6.12, 9, 551000),
            (68.42, 3.12, 6, 323680)
        ]
        
        for x, y, z, expected in test_data:
            with self.subTest(x=x, y=y, z=z):
                self.assertEqual(calculate_shipping_fee(x, y, z), expected)

if __name__ == "__main__":
    unittest.main()
