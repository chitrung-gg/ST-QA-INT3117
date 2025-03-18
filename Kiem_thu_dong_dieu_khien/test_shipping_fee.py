import unittest
from calculate_shipping_fee import calculate_shipping_fee  # Import hàm từ file khác

class TestShippingFee(unittest.TestCase):
    def test_cases_branch_coverage(self):
        test_data = [
            (1000.01, 16.12, 22, "Invalid Input"),
            (9.75, 12.25, 15, 98750),
            (42.5, 9.25, 20, 191250),
            (100.01, 6.45, 10, 450040)
        ]
        
        for x, y, z, expected in test_data:
            with self.subTest(x=x, y=y, z=z):
                self.assertEqual(calculate_shipping_fee(x, y, z), expected)

if __name__ == "__main__":
    unittest.main()