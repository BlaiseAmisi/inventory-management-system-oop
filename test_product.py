import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_total_value(self):
        p = Product(1, "Test", 10.0, 3)
        self.assertEqual(p.get_total_value(), 30.0)

    def test_update_quantity_valid(self):
        p = Product(1, "Test", 5.0, 10)
        p.update_quantity(20)
        self.assertEqual(p.quantity, 20)

    def test_update_quantity_invalid(self):
        p = Product(1, "Test", 5.0, 10)
        p.update_quantity(-5)
        self.assertEqual(p.quantity, 10)  # Should not change

    def test_negative_price_raises(self):
        with self.assertRaises(ValueError):
            Product(2, "Bad", -10.0, 5)
