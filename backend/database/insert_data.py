import sqlite3
import json

# Load data from 'data.json' file
with open('data.json', 'r') as f:
    data = json.load(f)

# Create a connection to the SQLite database
conn = sqlite3.connect('invoices.db')
cursor = conn.cursor()

# Insert data into tables
def insert_data():
    # Insert clients
    for client in data['clients']:
        cursor.execute('''
            INSERT INTO clients (id, name, idno, company_type, created_date, vertical, address, tva_code, bank_code, bank_name, iban, bank_address, fiscal_code, director_first_name, director_last_name, country, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', tuple(client.values()))

    # Insert contracts
    for contract in data['contracts']:
        cursor.execute('''
            INSERT INTO contracts (id, created_date, updated_date, obligor_client_id, obligatee_client_id, text, data)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            contract['id'], contract['created_date'], contract['updated_date'],
            contract['obligor_client_id'], contract['obligatee_client_id'],
            contract['text'], json.dumps(contract['data'])  # Convert data to JSON string
        ))

    # Insert terms
    for term in data['terms']:
        cursor.execute('''
            INSERT INTO terms (id, type, description, data)
            VALUES (?, ?, ?, ?)
        ''', (
            term['id'], term['type'], term['description'], json.dumps(term['data'])  # Convert data to JSON string
        ))

    # Insert invoice_type
    for invoice_type in data['invoice_type']:
        cursor.execute('''
            INSERT INTO invoice_type (id, name, contract_id, created_date, notes, data, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            invoice_type['id'], invoice_type['name'], invoice_type['contract_id'],
            invoice_type['created_date'], invoice_type['notes'],
            json.dumps(invoice_type['data']),  # Convert data to JSON string
            invoice_type['description']
        ))

    # Insert invoices
    for invoice in data['invoices']:
        cursor.execute('''
            INSERT INTO invoices (id, invoice_number, invoice_date, invoice_due_date, invoice_type_id)
            VALUES (?, ?, ?, ?, ?)
        ''', tuple(invoice.values()))

    # Insert products
    for product in data['products']:
        cursor.execute('''
            INSERT INTO products (id, name, price)
            VALUES (?, ?, ?)
        ''', tuple(product.values()))

    # Insert products_invoices_join
    for products_invoice in data['products_invoices_join']:
        cursor.execute('''
            INSERT INTO products_invoices_join (invoice_type_id, product_id, quantity, line_total)
            VALUES (?, ?, ?, ?)
        ''', tuple(products_invoice.values()))

    # Insert invoice_runners
    for runner in data['invoice_runners']:
        cursor.execute('''
            INSERT INTO invoice_runners (id, invoice_type_id, runner_type)
            VALUES (?, ?, ?)
        ''', tuple(runner.values()))

    # Insert invoice_runs
    for run in data['invoice_runs']:
        cursor.execute('''
            INSERT INTO invoice_runs (id, invoice_id, runner_id, created_date, completed_date, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', tuple(run.values()))

    # Insert invoice_runner_schedules
    for schedule in data['invoice_runner_schedules']:
        cursor.execute('''
            INSERT INTO invoice_runner_schedules (id, runner_id, frequency, start_date)
            VALUES (?, ?, ?, ?)
        ''', tuple(schedule.values()))

    # Insert invoice_runner_one_time
    for one_time in data['invoice_runner_one_time']:
        cursor.execute('''
            INSERT INTO invoice_runner_one_time (id, runner_id, start_date)
            VALUES (?, ?, ?)
        ''', tuple(one_time.values()))

    # Insert terms_invoices_join
    for terms_invoice in data['terms_invoices_join']:
        cursor.execute('''
            INSERT INTO terms_invoices_join (invoice_type_id, terms_id)
            VALUES (?, ?)
        ''', tuple(terms_invoice.values()))

# Call the insert function
insert_data()

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully.")
