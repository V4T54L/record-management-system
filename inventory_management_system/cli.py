"""CLI app
"""

from inventory_management_system.models import Inventory, Product, InventoryStatus
from inventory_management_system.csv_db import load_from_file, save_to_file


class CLI(object):
    """CLI application"""

    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path
        self.inv_manager = Inventory()
        self.inv_manager.inventory = load_from_file(csv_path)
        self.exit_message = "\nor type 'exit' to exit the application"
        self.choices = [
            self.print_products,
            self.add_product,
            self.update_product,
            self.delete_product,
        ]

    def start(self) -> None:
        """Entry point for the CLI app"""
        inp = ""
        try:
            while True:
                self.print_home()
                inp = input()
                if inp.isnumeric() and 0 < int(inp) <= 4:
                    self.choices[int(inp) - 1]()
                elif inp == "exit":
                    break
                else:
                    print("Invalid input, Please try again.")
                input("\nPress any key to continue...")
        except KeyboardInterrupt:
            print("Interrupted by keyboard, Exiting...")
        except Exception as e:
            print("Unhandled exception : ", e)

        finally:
            print("Saving data...")
            save_to_file(self.csv_path, self.inv_manager.inventory)

        print("\n\n[+] Application terminated successfully")

    def print_home(self):
        """Print home page"""
        text = """Enter your choice:
        1. Print all products
        2. Add Product
        3. Update Product
        4. Delete (Deactivate) product
        """
        print(text + self.exit_message)
        return

    def add_product(self):
        """Handle Add Product"""
        print("ADD PRODUCT: \n\t Please enter product details\n")
        name = input("Name (min. 5 characters) : ")
        description = input("Description (optional) : ")
        price = float(input("Price (>0) : "))
        quantity = int(input("Quantity (>=0) : "))
        status = input("Status (active/inactive) : ")

        product = Product(-1, name, description, price, quantity, status)
        status = self.inv_manager.add_product(product)
        if status == InventoryStatus.SUCCESS:
            print("\n[+] Product added successfully.\n")
        else:
            print(f"\n[-] Failed to add product : {status}.\n")
        return

    def update_product(self):
        """Handle Update Product"""
        print("UPDATE PRODUCT: \n\t Please enter product details\n")
        index_str = ""
        while not index_str:
            index_str = input("Product Index : ")
            if len(index_str) > 0:
                index = int(index_str)
        name = input("Name (min. 5 characters) [optional] : ")
        description = input("Description [optional] : ")
        price_str = input("Price (>0) [optional]: ")
        price = float(price_str) if len(price_str) > 0 else 0

        quantity_str = int(input("Quantity [optional] : "))
        quantity = int(quantity_str) if len(quantity_str) > 0 else -1

        status = input("Status (active/inactive) [optional] : ")

        product = Product(-1, name, description, price, quantity, status)
        status = self.inv_manager.update_product(product)
        if status == InventoryStatus.SUCCESS:
            print("\n[+] Product added successfully.\n")
        else:
            print(f"\n[-] Failed to add product : {status}.\n")
        return

    def delete_product(self):
        """Handle Delete Product"""
        print("DELETE PRODUCT: \n\t Please provide following detail\n")
        index = int(input("Product index : "))
        status = self.inv_manager.delete_product(index)
        if status == InventoryStatus.SUCCESS:
            print("\n[+] Product added successfully.\n")
        else:
            print(f"\n[-] Failed to add product : {status}.\n")
        return

    def print_products(self):
        """Prints products"""
        print("PRINT ALL PRODUCTS:\n")
        print(self.inv_manager.get_products_details())
