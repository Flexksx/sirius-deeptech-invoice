CREATE TABLE IF NOT EXISTS terms_invoices_join (
    invoice_type_id INTEGER NOT NULL,
    terms_id INTEGER NOT NULL,
    FOREIGN KEY (invoice_type_id) REFERENCES invoice_type (id),
    FOREIGN KEY (terms_id) REFERENCES terms (id)
);

CREATE TABLE IF NOT EXISTS invoice_type (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contract_id INTEGER NOT NULL,
    created_date TIMESTAMP NOT NULL,
    notes TEXT NOT NULL,
    data TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (contract_id) REFERENCES contracts (id)
);

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT NOT NULL,
    invoice_date DATETIME NOT NULL,
    invoice_due_date DATETIME NOT NULL,
    invoice_type_id INTEGER NOT NULL,
    FOREIGN KEY (invoice_type_id) REFERENCES invoice_type (id)
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price DECIMAL(8, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS contracts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    created_date TIMESTAMP NOT NULL,
    updated_date TIMESTAMP NOT NULL,
    obligor_client_id INTEGER NOT NULL,
    obligatee_client_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (obligor_client_id) REFERENCES clients (id),
    FOREIGN KEY (obligatee_client_id) REFERENCES clients (id)
);

CREATE TABLE IF NOT EXISTS products_invoices_join (
    invoice_type_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    line_total DECIMAL(8, 2) NOT NULL,
    FOREIGN KEY (invoice_type_id) REFERENCES invoice_type (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

CREATE TABLE IF NOT EXISTS invoice_runners (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    invoice_type_id INTEGER NOT NULL,
    runner_type TEXT NOT NULL,
    FOREIGN KEY (invoice_type_id) REFERENCES invoice_type (id)
);

CREATE TABLE IF NOT EXISTS invoice_runs (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    runner_id INTEGER NOT NULL,
    created_date TIMESTAMP NOT NULL,
    completed_date TIMESTAMP NOT NULL,
    status BOOLEAN NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices (id),
    FOREIGN KEY (runner_id) REFERENCES invoice_runners (id)
);

CREATE TABLE IF NOT EXISTS invoice_runner_schedules (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    runner_id INTEGER NOT NULL,
    frequency TIME NOT NULL,
    start_date DATETIME NOT NULL,
    FOREIGN KEY (runner_id) REFERENCES invoice_runners (id)
);

CREATE TABLE IF NOT EXISTS invoice_runner_one_time (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    runner_id INTEGER NOT NULL,
    start_date DATETIME NOT NULL,
    FOREIGN KEY (runner_id) REFERENCES invoice_runners (id)
);


CREATE TABLE IF NOT EXISTS clients (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    idno TEXT NOT NULL,
    company_type TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL,
    vertical TEXT NOT NULL,
    address TEXT NOT NULL,
    tva_code TEXT NOT NULL,
    bank_code TEXT NOT NULL,
    bank_name TEXT NOT NULL,
    iban TEXT NOT NULL,
    bank_address TEXT NOT NULL,
    fiscal_code TEXT NOT NULL,
    director_first_name TEXT NOT NULL,
    director_last_name TEXT NOT NULL,
    country TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS terms (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    description TEXT NOT NULL,
    data TEXT NOT NULL
);
