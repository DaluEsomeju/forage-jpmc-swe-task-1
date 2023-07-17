import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      output = getDataPoint(quote)
      self.assertEqual(output, (quote['stock'], (quote['top_ask']['price'] + quote['top_bid']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      output = getDataPoint(quote)
      self.assertEqual(output, (quote['stock'], (quote['top_ask']['price'] + quote['top_bid']['price']) / 2))


  """ ------------  more unit tests ------------ """
  def test_getDataPoint_bidEqualAsk(self):
    quote = {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    output = getDataPoint(quote)
    self.assertEqual(output, (quote['stock'], quote['top_ask']['price']))

  def test_getDataPoint_bidAndAskAreZero(self):
    quote = {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    output = getDataPoint(quote)
    self.assertEqual(output, (quote['stock'], 0))

  def test_getRatio_priceBZero(self):
    price_a = 119.2
    price_b = 0
    output = getRatio(price_a, price_b)
    self.assertIsNone(output, "The output should be None when price_b is 0.")

  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 119.2
    output = getRatio(price_a, price_b)
    self.assertEqual(output, 0, "The output should be 0 when price_a is 0.")

  def test_getRatio_priceAandBZero(self):
    price_a = 0
    price_b = 0
    output = getRatio(price_a, price_b)
    self.assertIsNone(output, "The output should be None when both prices are 0.")

  def test_getRatio_positivePrices(self):
    price_a = 121.2
    price_b = 120.48
    output = getRatio(price_a, price_b)
    self.assertEqual(output, price_a/price_b, "The output should be the ratio of price_a to price_b.")
    
    

if __name__ == '__main__':
    unittest.main()
