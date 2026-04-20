from product import Product
from store import Store

def main():
    store = Store()

    # Preloaded sample products
    store.add_product(Product(101, "Laptop", 800, 5))
    store.add_product(Product(102, "Mouse", 25, 20))
    store.add_product(Product(103, "Keyboard", 50, 10))

    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add New Product")
        print("3. Update Product Quantity")
        print("4. Search Product")
        print("5. Generate Inventory Report")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            store.view_inventory()
        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                store.add_product(Product(product_id, name, price, quantity))
            except ValueError:
                print("Invalid input! Please enter valid numbers for ID, price, and quantity.")
        elif choice == "3":
            try:
                product_id = int(input("Enter Product ID: "))
                new_quantity = int(input("Enter New Quantity: "))
                store.update_product_quantity(product_id, new_quantity)
            except ValueError:
                print("Invalid input! Please enter a valid number for quantity.")
        elif choice == "4":
            search_term = input("Enter Product Name or ID: ")
            store.search_product(search_term)
        elif choice == "5":
            store.generate_inventory_report()
        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
# This is a simple inventory management system that allows users to manage products in a store.
# It includes functionalities to view, add, update, search products, and generate an inventory report.
