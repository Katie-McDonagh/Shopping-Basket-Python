import unittest
@dataclass
class Basket(object):
  items: List

  def total(pass):
    pass

class ShoppingBasketTest(unittest.TestCase):
  def test_empty_basket_total(self):
    basket = Basket([])
    self.assertEqual(basket.total(), 0)


if __name__ == '__main__'
  pass