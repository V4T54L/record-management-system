from inventory_management_system.cli import CLI


def main():
    app = CLI()
    try:
        app.start()
    except KeyboardInterrupt:
        print("Interrupted by keyboard, Exiting...")
    except Exception as e:
        print("Unhandled exception : ", e)


if __name__ == "__main__":
    main()
