"""Declaration for Product, Inventory and required enums"""

from typing import List
from inventory_management_system.enums import (
    ProductStatus,
    InventoryStatus,
    ValidationStatus,
)


class Product(object):
    """Product class"""

    def __init__(
        self,
        index: int,
        name: str,
        description: str,
        price: int,
        quantity: int,
        status: str,
    ) -> None:
        self.index = index
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.status_msg = status
        if status == "inactive":
            self.status = ProductStatus.INACTIVE
        else:
            self.status = (
                ProductStatus.AVAILABLE
                if self.quantity > 0
                else ProductStatus.UNAVAILABLE
            )

    def validate(self):
        """Validate product details

        Returns:
            validation_status : Validation status of the product
        """

        if self.price <= 0:
            # "Invalid price"
            return ValidationStatus.FAILURE

        if self.quantity < 0:
            # "invalid quantity"
            return ValidationStatus.FAILURE

        # At least 5 characters for name
        if len(self.name) < 5:
            # "invalid name"
            return ValidationStatus.FAILURE

        return ValidationStatus.SUCCESS

    def __str__(self) -> str:
        return f"""
        Index : {self.index}
        Name : {self.name}
        Description : {self.description}
        Price : {self.price}
        Quantity : {self.quantity}
        Status : {self.status}"""


class Inventory(object):
    def __init__(self) -> None:
        self.inventory: List[Product] = []

    def add_product(self, product: Product) -> str:
        """Add a product to the inventory

        Args:
            product (Product): A product object that needs to be
            added to the inventory

        Returns:
            validation_status : Status of updation of product
        """
        product.index = len(self.inventory)
        if product.validate() != ValidationStatus.SUCCESS:
            return InventoryStatus.INVALID_DATA

        self.inventory.append(product)
        return InventoryStatus.SUCCESS

    def update_product(self, product: Product):
        """Update a product in the inventory

        Args:
            product (Product): Partial (or complete) product information

        Returns:
            validation_status : Status of updation of product
        """
        if product.index < 0 or product.index > len(product):
            return InventoryStatus.INVALID_DATA

        db_product = self.inventory[product.index]

        if len(product.name) > 0:
            db_product.name = product.name

        if len(product.description) > 0:
            db_product.description = product.description

        # Input -1 as quantity if not provided
        if len(product.quantity) != -1:
            db_product.quantity = product.quantity

        if len(product.status) > 0:
            db_product.status_msg = product.status_msg
            if product.status_msg == "inactive":
                db_product.status = ProductStatus.INACTIVE
            else:
                db_product.status = (
                    ProductStatus.AVAILABLE
                    if db_product.quantity > 0
                    else ProductStatus.UNAVAILABLE
                )

        self.inventory[product.index] = db_product

        return InventoryStatus.SUCCESS

    def delete_product(self, index: int):
        """Delete/Deactivate a product from inventory

        Args:
            index (int): Index of the product to deactivate

        Returns:
            validation_status : Status of updation of product
        """
        if index < 0 or index > len(Product):
            return InventoryStatus.INVALID_DATA

        self.inventory[index].status = ProductStatus.INACTIVE
        return InventoryStatus.SUCCESS

    def get_active_products(self) -> str:
        """Get details of all products

        Returns:
            inventory_details(str): Concatenated details of all
            products in the inventory
        """
        return "\n===================\n".join(map(str, self.inventory))
