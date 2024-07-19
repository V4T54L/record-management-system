from inventory_management_system.cli import CLI
from inventory_management_system.csv_db import save_to_file


def main():
    file_path = "./db.csv"
    app = CLI(csv_path=file_path)
    app.start()


if __name__ == "__main__":
    main()
