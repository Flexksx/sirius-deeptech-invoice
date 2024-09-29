import json
import os

# Load the HTML template as a string
html_template = """<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factură Fiscală</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 40px;
            padding: 20px;
            border: 1px solid #ccc;
            width: 800px;
            background-color: #f8f8f8;
            color: #333;
        }}
        h1, h2, h3 {{
            text-align: center;
            margin-bottom: 10px;
        }}
        h1 {{
            font-size: 24px;
            margin-bottom: 30px;
            color: #333;
        }}
        .invoice-header, .invoice-footer, .invoice-details {{
            margin-bottom: 30px;
            padding: 10px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .invoice-header {{
            text-align: center;
        }}
        .invoice-details {{
            display: flex;
            justify-content: space-between;
        }}
        .invoice-details div {{
            width: 45%;
        }}
        .supplier, .client {{
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 8px;
        }}
        .supplier h2, .client h2 {{
            font-size: 18px;
            color: #4CAF50;
            margin-bottom: 10px;
        }}
        .supplier p, .client p {{
            margin: 5px 0;
        }}
        table {{
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
            background-color: #fff;
        }}
        table th, table td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        table th {{
            background-color: #4CAF50;
            color: #fff;
            font-size: 16px;
        }}
        table td {{
            font-size: 14px;
        }}
        .total {{
            font-weight: bold;
            font-size: 18px;
            text-align: right;
        }}
        .invoice-footer {{
            text-align: right;
        }}
        .contract-details {{
            margin-top: 30px;
            padding: 20px;
            border: 1px solid #ddd;
            background-color: #fff;
            border-radius: 8px;
        }}
        .contract-details pre {{
            background-color: #f1f1f1;
            padding: 10px;
            font-family: monospace;
            white-space: pre-wrap;
            border: 1px solid #ddd;
            border-radius: 5px;
        }}
    </style>
</head>
<body>

    <div class="invoice-header">
        <h1>Fiscal Invoice: {invoice_name}</h1>
        <p>Data: <span id="invoice-date">Created Date: {created_date}</span></p>
    </div>

    <div class="invoice-details">
        <div class="supplier">
            <h2>Obligor:</h2>
            <p><strong>{obligor_company_type}, {obligor_name}</strong></p>
            <p>Adress: {obligor_address}</p>
            {obligor_idno}
            <p>Bank: {obligor_bank_name}</p>
            <p>Bank Code: {obligor_bank_code}</p>
            <p>Bank Address: {obligor_bank_address}</p>
            <p>Country: {obligor_country}</p>
            <p>Created Date: {obligor_created_date}</p>
            <p>Director First Name: {obligor_director_first_name}</p>
            <p>Director Last Name: {obligor_director_last_name}</p>
            {obligor_email}
            {obligor_fiscal_code}
            {obligor_iban}
            {obligor_phone}
            {obligor_tva_code}
        </div>

        <div class="client">
            <h2>Obligee:</h2>
            <p><strong>{obligee_name}</strong></p>
            <p>Adress: {obligee_address}</p>
            <p>Bank Address: {obligee_bank_address}</p>
            <p>Bank Code: {obligee_bank_code}</p>
            <p>Bank Name: {obligee_bank_name}</p>
            <p>Obligee Country: {obligee_country}</p>
            <p>Created Date: {obligee_created_date}</p>
            <p>Director First Name: {obligee_director_first_name}</p>
            <p>Director Last Name: {obligee_director_last_name}</p>
            {obligee_email}
            {obligee_fiscal_code}
            {obligee_iban}
            {obligee_idno}
            {obligee_phone}
            {obligee_tva_code}
        </div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Description</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{product_description}</td>
                <td>{product_price} {product_currency}</td>
                <td>{product_quantity}</td>
                <td>{product_total} {product_currency}</td>
            </tr>
        </tbody>
    </table>

    <div class="invoice-footer">
        <p class="total">Total: {product_total} {product_currency}</p>
        <p>Notes: {invoice_notes}</p>
    </div>

    <div class="contract-details">
        <h2>Contract</h2>
        <p><strong>Name: {contract_name}</strong></p>
        <pre>{contract_text}</pre>
    </div>

</body>
</html>
"""

file_path = os.path.join(os.path.dirname(__file__), 'a.json')
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract data for replacement
invoice_data = data['invoice_type']
obligor_data = invoice_data['obligor']
obligee_data = invoice_data['obligee']
contract_data = invoice_data['contract']
product_data = invoice_data['products'][0]  # Assuming a single product

# Prepare the values for replacement
html_output = html_template.format(
    invoice_name=invoice_data['name'],
    created_date=invoice_data['created_date'],
    obligor_company_type=obligor_data['company_type'],
    obligor_name=obligor_data['name'],
    obligor_address=obligor_data['address'],
    obligor_idno=f'<p>IDNO: {obligor_data["idno"]}</p>' if obligor_data['idno'] else '',
    obligor_bank_name=obligor_data['bank_name'] if obligor_data['bank_name'] else '',
    obligor_bank_code=obligor_data['bank_code'],
    obligor_bank_address=obligor_data['bank_address'],
    obligor_country=obligor_data['country'],
    obligor_created_date=obligor_data['created_date'],
    obligor_director_first_name=obligor_data['director_first_name'],
    obligor_director_last_name=obligor_data['director_last_name'],
    obligor_email=f'<p>Email: {obligor_data["email"]}</p>' if obligor_data.get('email') else '',
    obligor_fiscal_code=f'<p>Fiscal Code: {obligor_data["fiscal_code"]}</p>' if obligor_data.get('fiscal_code') else '',
    obligor_iban=f'<p>IBAN: {obligor_data["iban"]}</p>' if obligor_data.get('iban') else '',
    obligor_phone=f'<p>Phone: {obligor_data["phone"]}</p>' if obligor_data.get('phone') else '',
    obligor_tva_code=f'<p>TVA Code: {obligor_data["tva_code"]}</p>' if obligor_data.get('tva_code') else '',
    
    obligee_name=obligee_data['name'],
    obligee_address=obligee_data['address'],
    obligee_bank_address=obligee_data['bank_address'],
    obligee_bank_code=obligee_data['bank_code'],
    obligee_bank_name=obligee_data['bank_name'] if obligee_data.get('bank_name') else '',
    obligee_country=obligee_data['country'],
    obligee_created_date=obligee_data['created_date'],
    obligee_director_first_name=obligee_data['director_first_name'],
    obligee_director_last_name=obligee_data['director_last_name'],
    obligee_email=f'<p>Email: {obligee_data["email"]}</p>' if obligee_data.get('email') else '',
    obligee_fiscal_code=f'<p>Fiscal Code: {obligee_data["fiscal_code"]}</p>' if obligee_data.get('fiscal_code') else '',
    obligee_iban=f'<p>IBAN: {obligee_data["iban"]}</p>' if obligee_data.get('iban') else '',
    obligee_idno=f'<p>IDNO: {obligee_data["idno"]}</p>' if obligee_data.get('idno') else '',
    obligee_phone=f'<p>Phone: {obligee_data["phone"]}</p>' if obligee_data.get('phone') else '',
    obligee_tva_code=f'<p>TVA Code: {obligee_data["tva_code"]}</p>' if obligee_data.get('tva_code') else '',
    
    product_description=product_data['description'],
    product_price=product_data['price'],
    product_quantity=product_data['quantity'],
    product_total=product_data['price'] * product_data['quantity'],
    product_currency=product_data['currency'],
    invoice_notes=invoice_data['notes'],
    
    contract_name=contract_data['name'],
    contract_text=contract_data['text']
)

# Save the output HTML to a file
with open('invoice2.html', 'w', encoding='utf-8') as output_file:
    output_file.write(html_output)

print("Invoice generated successfully!")
