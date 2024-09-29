import os
import sys
import json
from flask import Blueprint, request, jsonify, abort
from datetime import datetime
from database import db_session
from models import *
# sys.path.append(os.path.abspath(
#     os.path.join(os.path.dirname(__file__), '../..')))


def store_in_db(ai_response: dict = None):
    if ai_response is None:
        return jsonify({"message": "No data to store in database"})

    data = ai_response.get("data")
    for contract_data in data:
        process_contract(contract_data.get("contract"))


def process_contract(contract_data: dict):
    contract_name = contract_data.get("name")
    contract_created_date_str = contract_data.get("created_date")
    contract_text = contract_data.get("text")
    obligee_data = contract_data.get("obligee")
    obligor_data = contract_data.get("obligor")
    other_data = contract_data.get("other_data")

    # Convert created_date string in dd-mm-yyyy format to datetime
    if contract_created_date_str:
        contract_created_date = datetime.strptime(
            contract_created_date_str, '%d-%m-%Y')
    else:
        contract_created_date = datetime.now()

    contract_obligee = process_client(obligee_data)
    contract_obligor = process_client(obligor_data)

    needed_invoice_types = contract_data.get("needed_invoices")

    # Create Contract instance with correct datetime object
    contract = Contract(
        name=contract_name,
        created_date=contract_created_date,
        obligor_client_id=contract_obligor.id,
        obligee_client_id=contract_obligee.id,
        text=contract_text,
        data=other_data
    )
    db_session.add(contract)
    db_session.commit()
    for invoice_data in needed_invoice_types:
        process_invoice_types(invoice_data, contract_id=contract.id)


def process_invoice_types(invoices_data: dict, contract_id: int):
    description = invoices_data.get("description")
    name = invoices_data.get("name")
    frequency = invoices_data.get("frequency")
    invoices_count = invoices_data.get("invoices_count")
    needed_starting_date = invoices_data.get("starting_date")
    if needed_starting_date:
        needed_starting_date = datetime.strptime(
            needed_starting_date, '%d-%m-%Y')
    else:
        needed_starting_date = datetime.now()

    notes = invoices_data.get("notes")
    terms = invoices_data.get("terms")
    products = invoices_data.get("products")
    other_data = invoices_data.get("data")
    if not other_data:
        other_data = None
    else:
        other_data = json.dumps(other_data)
    invoice_type = InvoiceType(name=name, contract_id=contract_id, notes=notes, data=other_data,
                               description=description, frequency=frequency, invoices_count=invoices_count, needed_starting_date=needed_starting_date)

    db_session.add(invoice_type)
    db_session.commit()
    invoice_type_id = invoice_type.id

    for term_data in terms:
        process_term(term_data, invoice_type_id)

    for product_data in products:
        process_product(product_data, invoice_type_id)


def process_term(term_data: dict, invoice_type_id: int):
    description = term_data.get("description")
    name = term_data.get("name")
    value = term_data.get("value")
    term = Terms(name, description, value, invoice_type_id)
    db_session.add(term)
    db_session.commit()


def process_product(product_data: dict, invoice_type_id: int):
    currency = product_data.get("currency")
    description = product_data.get("description")
    name = product_data.get("name")
    price = product_data.get("price")
    quantity = product_data.get("quantity")
    unit = product_data.get("unit")
    product = Product(
        name=name,
        description=description,
        price=price,
        unit=unit,
        currency=currency,
        quantity=quantity,
        invoice_type_id=invoice_type_id
    )
    db_session.add(product)
    db_session.commit()


def process_client(client_data: dict):
    idno = client_data.get("idno")
    print(idno)
    name = client_data.get("name")
    existing_client = db_session.query(Client).filter(
        Client.name == name).first()
    print(existing_client)
    if existing_client:
        return existing_client
    address = client_data.get("address")
    bank_address = client_data.get("bank_address")
    bank_code = client_data.get("bank_code")
    company_type = client_data.get("company_type")
    country = client_data.get("country")
    director_first_name = client_data.get("director_first_name")
    director_last_name = client_data.get("director_last_name")
    email = client_data.get("email")
    fiscal_code = client_data.get("fiscal_code")
    iban = client_data.get("iban")
    other_data = client_data.get("other_data")
    if not other_data:
        other_data = None
    else:
        other_data = json.dumps(other_data)

    phone = client_data.get("phone")
    tva_code = client_data.get("tva_code")
    vertical = client_data.get("vertical")
    client = Client(name=name, idno=idno, company_type=company_type, vertical=vertical, address=address, bank_code=bank_code, bank_name=None,
                    bank_address=bank_address, iban=iban, tva_code=tva_code, fiscal_code=fiscal_code, director_first_name=director_first_name, director_last_name=director_last_name, country=country, email=email, phone=phone, data=other_data)
    db_session.add(client)
    db_session.commit()
    return client
