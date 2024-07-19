"""Utils for CSV database"""

import csv
from typing import List
import os
from inventory_management_system.models import Product

FIELDS = ["index", "name", "description", "price", "quantity", "status"]


def load_from_file(file_path: str):
    """Load data from csv

    Args:
        file_path (str): path to csv file

    Returns:
        _type_: _description_
    """
    products = []
    if os.path.isfile(file_path):
        with open(file_path, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            _ = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                product = Product(
                    index=int(row[0]),
                    name=row[1],
                    description=row[2],
                    price=float(row[3]),
                    quantity=int(row[4]),
                    status=row[5],
                )
                products.append(product)

            # get total number of rows
            print("[+] Database loaded, Total no. of rows: %d" % (csvreader.line_num))
    else:
        print("[-] Database file not found, starting a fresh session.")

    return products


def save_to_file(file_path: str, data: List[Product]):
    mydict = [
        {
            "index": p.index,
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "quantity": p.quantity,
            "status": p.status.value,
        }
        for p in data
    ]
    with open(file_path, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS, lineterminator="\n")

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(mydict)
