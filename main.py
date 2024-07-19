from inventory_management_system.cli import CLI


def main():
    file_path = "./db.csv"
    app = CLI(csv_path=file_path)
    app.start()


if __name__ == "__main__":
    main()
