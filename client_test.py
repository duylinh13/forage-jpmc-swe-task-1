import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, top_bid_price, top_ask_price, stock_price_based_on_formula = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(top_bid_price, quote['top_bid']['price'])
            self.assertEqual(top_ask_price, quote['top_ask']['price'])
            # Add the expected stock_price_based_on_formula calculation if known
            expected_price = (top_bid_price + top_ask_price) / 2  # Example calculation, replace with the correct formula
            self.assertAlmostEqual(stock_price_based_on_formula, expected_price, places=2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, top_bid_price, top_ask_price, stock_price_based_on_formula = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(top_bid_price, quote['top_bid']['price'])
            self.assertEqual(top_ask_price, quote['top_ask']['price'])
            # Add the expected stock_price_based_on_formula calculation if known
            expected_price = (top_bid_price + top_ask_price) / 2  # Example calculation, replace with the correct formula
            self.assertAlmostEqual(stock_price_based_on_formula, expected_price, places=2)

    def test_getRatio(self):
        # Example data, replace with actual test cases and expected results
        data = [
            (10, 5, 2),  # Example: getRatio(10, 5) should return 2
            (10, 0, float('inf'))  # Example: getRatio(10, 0) should handle division by zero
        ]
        for numerator, denominator, expected_ratio in data:
            self.assertEqual(getRatio(numerator, denominator), expected_ratio)

if __name__ == '__main__':
    unittest.main()
