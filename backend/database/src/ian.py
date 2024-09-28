import sqlite3
import json
from DBcontracts import DBContracts
# Assuming DBContracts class is already defined above

def insert_data_from_json(db_path, json_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Create an instance of DBContracts
    db_contracts = DBContracts(conn)

    # Load data from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    for contract in data:
        db_contracts.insert(contract)
    
    # Close the connection
    conn.close()

# Usage
db_path = '/home/liviu/GigaHack24/sirius-deeptech-invoice/backend/database/src/database.db'  # Update with your database path
json_file = '/home/liviu/GigaHack24/sirius-deeptech-invoice/backend/database/src/data.json'  # Update with your JSON file path
insert_data_from_json(db_path, json_file)
