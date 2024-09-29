import os
import sys
from flask import Blueprint, request, jsonify, abort
from datetime import datetime
from database import db_session
from database.models import *
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

invoice_type_blueprint = Blueprint('invoice_type', __name__)


@invoice_type_blueprint.route('/invoice_type', methods=['GET'])
def get_invoice_types():
    try:
        invoice_types = db_session.query(InvoiceType).all()
        answer = [
            {
                "id": invoice_type.id,
                "name": invoice_type.name,
                "frequency": str(invoice_type.frequency),
                "contract_id": invoice_type.contract_id
            } for invoice_type in invoice_types
        ]
        return jsonify(answer), 200
    except Exception as e:
        db_session.rollback()
        return jsonify({"message": str(e)}), 500


@invoice_type_blueprint.route('/invoice_type/<int:id>', methods=['GET'])
def get_invoice_type(id):
    invoice_type = InvoiceType.query.get(id)
    contract_associated = Contract.query.get(invoice_type.contract_id)
    contract_json = contract_associated.__dict__.copy()
    contract_json.pop('_sa_instance_state', None)

    obligor_client = Client.query.get(contract_associated.obligor_client_id)
    obligor_client_json = obligor_client.__dict__.copy()
    obligor_client_json.pop('_sa_instance_state', None)

    obligee_client = Client.query.get(contract_associated.obligee_client_id)
    obligee_client_json = obligee_client.__dict__.copy()
    obligee_client_json.pop('_sa_instance_state', None)

    invoice_products = Product.query.filter_by(
        invoice_type_id=invoice_type.id).all()
    products = []
    for product in invoice_products:
        product_json = product.__dict__.copy()
        product_json.pop('_sa_instance_state', None)
        product_json['unit'] = str(product_json['unit'])
        products.append(product_json)

    due_invoices = DueInvoice.query.filter_by(
        invoice_type_id=invoice_type.id).all()
    due_invoices_list = []
    for due_invoice in due_invoices:
        due_invoice_json = due_invoice.__dict__.copy()
        due_invoice_json.pop('_sa_instance_state', None)
        due_invoices_list.append(due_invoice_json)
    response = {
        "invoice_type": {
            "id": invoice_type.id,
            "name": invoice_type.name,
            "notes": invoice_type.notes,
            "created_date": invoice_type.created_date,
            "description": invoice_type.description,
            "frequency": str(invoice_type.frequency),
            "invoices_count": invoice_type.invoices_count,
            "needed_starting_date": invoice_type.needed_starting_date,
            "products": products,
            "contract": contract_json,
            "obligor": obligor_client_json,
            "obligee": obligee_client_json,
            "due_invoices": due_invoices_list
        }
    }
    return jsonify(response)


@invoice_type_blueprint.route('/invoice_type', methods=['POST'])
def create_invoice_type():
    data = request.json
    new_invoice_type = InvoiceType(
        name=data.get("name"),
        contract_id=data.get("contract_id"),
        notes=data.get("notes"),
        data=data.get("data"),
        description=data.get("description"),
        frequency=data.get("frequency"),
        invoices_count=data.get("invoices_count"),
        needed_starting_date=data.get("needed_starting_date")
    )
    db_session.add(new_invoice_type)
    db_session.commit()
    return jsonify({"message": "Invoice type created", "invoice_type": {"name": new_invoice_type.name, "id": new_invoice_type.id, "contract_id": new_invoice_type.contract_id}})
