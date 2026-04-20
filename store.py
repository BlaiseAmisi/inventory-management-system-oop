class Store:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        if product.product_id in self.inventory:
            print("Error: Product ID already exists!")
        else:
            self.inventory[product.product_id] = product
            print("Product added successfully!")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty!")
        else:
            print("\nID   | Name       | Price  | Quantity | Total Value")
            print("--------------------------------------------------")
            for product in self.inventory.values():
                print(product.display())

    def update_product_quantity(self, product_id, new_quantity):
        if product_id in self.inventory:
            self.inventory[product_id].update_quantity(new_quantity)
        else:
            print("Error: Product not found!")

    def search_product(self, search_term):
        found = [p for p in self.inventory.values() if p.name.lower() == search_term.lower() or str(p.product_id) == search_term]
        if found:
            for product in found:
                print(f"\nID: {product.product_id} | Name: {product.name} | Price: ${product.price:.2f} | Quantity: {product.quantity}")
        else:
            print("Product not found!")

    def generate_inventory_report(self):
        total_value = sum(product.get_total_value() for product in self.inventory.values())
        print("\n--------------------------------------------------")
        print(f"Total Products: {len(self.inventory)}")
        print(f"Total Inventory Value: ${total_value:.2f}")
        print("--------------------------------------------------")
