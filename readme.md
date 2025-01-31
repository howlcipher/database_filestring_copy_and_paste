# Database_Filestring_Copy_and_paste

## Installation

1. **Clone the repository:**

    git clone https://github.com/your_username/your_repository.git
    cd your_repository

## Install dependencies:

    pip install -r requirements.txt
This installs all required dependencies listed in requirements.txt.

## Setup configuration:

Modify config.json file with your specific configurations.

## Usage
Run the application:

    python main.py

## Build
    pyinstaller main.spec

Expected output:

Files are copied from a file string with in a query to a desired location.

## Configuration
config.json: This file contains configuration settings such as database connection details (database, server, username, password) and other application-specific settings.

Example config.json structure:

    {
        "database": {
            "server": "your_server_name",
            "database": "your_database_name",
            "query": "SELECT * FROM your_table;"
            "file_column": "file_path"
        },
        "destination_directory": "output"
    }

Adjust the configuration according to your specific setup.