class Product:
    def __init__(self, product_id, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            print("Error: Quantity cannot be negative.")
        else:
            self.quantity = new_quantity
            print("Stock updated successfully!")

    def get_total_value(self):
        return self.price * self.quantity

    def display(self):
        return f"{self.product_id}  | {self.name.ljust(10)} | ${self.price:.2f} | {self.quantity} | ${self.get_total_value():.2f}"
