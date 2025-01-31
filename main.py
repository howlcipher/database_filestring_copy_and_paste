from modules.app import App

def main():
    """
    Main function to run the application.
    """
    config_path = 'config.json'
    app = App(config_path)
    app.run()

if __name__ == "__main__":
    main()
