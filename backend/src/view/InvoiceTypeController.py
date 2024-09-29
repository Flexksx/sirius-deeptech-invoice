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
    obligor_client = Client.query.get(contract_associated.obligor_client_id)
    obligee_client = Client.query.get(contract_associated.obligee_client_id)
    response = {

    }
    return jsonify(invoice_type)


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
