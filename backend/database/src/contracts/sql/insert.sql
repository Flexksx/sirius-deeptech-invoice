-- Insert into clients table
INSERT INTO clients (
    id, name, idno, company_type, created_date, vertical, address, tva_code, 
    bank_code, bank_name, iban, bank_address, fiscal_code, director_first_name, 
    director_last_name, country, email
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

-- Insert into contracts table
INSERT INTO contracts (
    id, created_date, updated_date, obligor_client_id, obligatee_client_id, text, data
) VALUES (?, ?, ?, ?, ?, ?, ?);

-- Insert into terms table
INSERT INTO terms (
    id, type, description, data
) VALUES (?, ?, ?, ?);

-- Insert into invoice_type table
INSERT INTO invoice_type (
    id, name, contract_id, created_date, notes, data, description
) VALUES (?, ?, ?, ?, ?, ?, ?);

-- Insert into invoices table
INSERT INTO invoices (
    id, invoice_number, invoice_date, invoice_due_date, invoice_type_id
) VALUES (?, ?, ?, ?, ?);

-- Insert into products table
INSERT INTO products (
    id, name, price
) VALUES (?, ?, ?);

-- Insert into products_invoices_join table
INSERT INTO products_invoices_join (
    invoice_type_id, product_id, quantity, line_total
) VALUES (?, ?, ?, ?);

-- Insert into invoice_runners table
INSERT INTO invoice_runners (
    id, invoice_type_id, runner_type
) VALUES (?, ?, ?);

-- Insert into invoice_runs table
INSERT INTO invoice_runs (
    id, invoice_id, runner_id, created_date, completed_date, status
) VALUES (?, ?, ?, ?, ?, ?);

-- Insert into invoice_runner_schedules table
INSERT INTO invoice_runner_schedules (
    id, runner_id, frequency, start_date
) VALUES (?, ?, ?, ?);

-- Insert into invoice_runner_one_time table
INSERT INTO invoice_runner_one_time (
    id, runner_id, start_date
) VALUES (?, ?, ?);

-- Insert into terms_invoices_join table
INSERT INTO terms_invoices_join (
    invoice_type_id, terms_id
) VALUES (?, ?);
