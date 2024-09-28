CREATE TABLE terms_invoices_join (
    invoice_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    terms_id INTEGER NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (terms_id) REFERENCES terms(id)
);

CREATE TABLE invoices (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    contract_id INTEGER NOT NULL,
    description TEXT NOT NULL, -- Replaced MULTILINESTRING with TEXT
    invoice_date DATETIME NOT NULL,
    invoice_number TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    invoice_due_date DATETIME NOT NULL,
    payment_terms INTEGER NOT NULL,
    notes TEXT NOT NULL, -- Replaced MULTILINESTRING with TEXT
    data JSON NOT NULL,
    FOREIGN KEY (contract_id) REFERENCES contracts(id)
);

CREATE TABLE products (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    price REAL NOT NULL
);

CREATE TABLE contracts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    created_date TIMESTAMP NOT NULL,
    updated_date TIMESTAMP NOT NULL,
    obligor_id INTEGER NOT NULL,
    obligatee_id INTEGER NOT NULL,
    text TEXT NOT NULL, -- Replaced MULTILINESTRING with TEXT
    face_value INTEGER NOT NULL,
    FOREIGN KEY (obligor_id) REFERENCES clients(id),
    FOREIGN KEY (obligatee_id) REFERENCES clients(id)
);

CREATE TABLE products_invoices_join (
    invoice_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    line_total REAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE invoice_schedules (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    frequency TIME NOT NULL,
    created_date INTEGER NOT NULL,
    updated_date INTEGER NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);

CREATE TABLE clients (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    idno TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    company_type TEXT NOT NULL, -- Replaced ENUM with TEXT
    created_date TIMESTAMP NOT NULL,
    vertical TEXT NOT NULL, -- Replaced ENUM with TEXT
    address TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    tva_code TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    bank_code TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    bank_name TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    iban TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    bank_address TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    fiscal_code TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    person_id INTEGER NOT NULL,
    director_first_name TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    director_last_name TEXT NOT NULL, -- Replaced LINESTRING with TEXT
    country INTEGER NOT NULL,
    email TEXT NOT NULL -- Replaced LINESTRING with TEXT
);

CREATE TABLE terms (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL, -- Replaced ENUM with TEXT
    description TEXT NOT NULL, -- Replaced MULTILINESTRING with TEXT
    data JSON NOT NULL
);
