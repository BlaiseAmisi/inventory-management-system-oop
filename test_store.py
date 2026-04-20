import unittest
from product import Product
from store import Store

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.product = Product(1, "Phone", 500.0, 5)

    def test_add_product(self):
        self.store.add_product(self.product)
        self.assertIn(1, self.store.inventory)

    def test_update_product_quantity(self):
        self.store.add_product(self.product)
        self.store.update_product_quantity(1, 10)
        self.assertEqual(self.store.inventory[1].quantity, 10)

    def test_search_product_found(self):
        self.store.add_product(self.product)
        results = [p for p in self.store.inventory.values() if p.name.lower() == "phone"]
        self.assertEqual(len(results), 1)

    def test_inventory_value_report(self):
        self.store.add_product(Product(1, "Item1", 10.0, 2))
        self.store.add_product(Product(2, "Item2", 20.0, 1))
        total_value = sum(p.get_total_value() for p in self.store.inventory.values())
        self.assertEqual(total_value, 40.0)
