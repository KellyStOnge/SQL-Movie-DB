# Movie Database Project

## Overview

This project is designed to build and interact with a MySQL database named `moviedbtest`, containing data related to movies. It involves two primary Python scripts:

1. `351HW5_Create.py` - For setting up the database and populating it with data from a provided CSV file.
2. `HW5Q.py` - For running specific queries against the `moviedbtest` database.

The database includes various tables that store detailed information about movies, such as titles, budgets, genres, production companies, etc.

## Prerequisites

Before running the scripts, ensure you have the following installed and configured on your system:

- Python 3.x
- MySQL Server
- MySQL Connector for Python

You can install MySQL Connector for Python using pip:
	'''bash
	pip install mysql-connector-python
	'''

## Database Setup

To set up and populate the `moviedbtest` database, follow these steps:

### Creating and Populating the Database

1. Use the `351HW5_Create.py` script to create the database and its tables, and then populate them with data from a CSV file. Execute the script in your terminal as shown below:

    ```bash
    python3 351HW5_Create.py "path_to_your_csv_file.csv"
    ```

    Replace `"path_to_your_csv_file.csv"` with the actual path to your CSV file.

    **Note:** The CSV file should contain columns that match the database schema, including but not limited to `id`, `title`, `budget`, `original_language`, etc.

### Database Credentials

Ensure you have the following credentials set up for accessing the database:

- **Database Name:** moviedbtest
- **Host:** localhost
- **User:** root
- **Password:** password

After completing these steps, your `moviedbtest` database should be set up with all the necessary tables filled with the data from your CSV file.


## Running Queries

After you have successfully set up the database, you can interact with it by running specific queries through the `HW5Q.py` script. This script allows you to execute predefined queries related to the homework assignment. 

### Usage

To run the script, open your terminal and execute:

```bash
python3 HW5Q.py
'''

Upon running, the script will prompt you to enter the query you wish to execute. You can choose from the following options:

q1 - Executes the first query.
q2 - Executes the second query.
q3 - Executes the third query.
q4 - Executes the fourth query.
q5 - Executes the fifth query.
quit - Exits the program.
Please note that the script is designed to accept only these specific inputs. Any other input will not be recognized.


This version corrects the formatting issues and includes guidelines for contributions and a note on the license, making it a complete and user-friendly README for your project.
