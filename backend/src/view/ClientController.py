from datetime import datetime
from database import db_session
from database.models import Client, Contract
from flask import Flask, jsonify, request, abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

clients_blueprint = Blueprint('clients_blueprint', __name__)


@clients_blueprint.route("/clients", methods=["GET"])
def get_clients():
    try:
        clients = db_session.query(Client).all()
        # Use list comprehension to filter out SQLAlchemy's internal attributes
        return jsonify([{
            key: value for key, value in client.__dict__.items()
            if not key.startswith('_')  # Exclude internal attributes
        } for client in clients]), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@clients_blueprint.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    try:
        # Query for the client by ID
        client = db_session.query(Client).get(client_id)
        if not client:
            abort(404, description="Client not found")

        # Serialize the client object (you can use __dict__ filtering or Marshmallow as shown previously)
        return jsonify({
            key: value for key, value in client.__dict__.items()
            if not key.startswith('_')  # Exclude internal attributes
        }), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@clients_blueprint.route("/clients", methods=["POST"])
def create_client():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate the input data (you can add more validations as needed)
        if not data or not isinstance(data, dict):
            abort(400, description="Invalid input data")

        # Create a new Client instance
        new_client = Client(
            name=data.get("name"),
            idno=data.get("idno"),
            company_type=data.get("company_type"),
            vertical=data.get("vertical"),
            address=data.get("address"),
            bank_code=data.get("bank_code"),
            bank_name=data.get("bank_name"),
            bank_address=data.get("bank_address"),
            iban=data.get("iban"),
            tva_code=data.get("tva_code"),
            fiscal_code=data.get("fiscal_code"),
            director_first_name=data.get("director_first_name"),
            director_last_name=data.get("director_last_name"),
            country=data.get("country"),
            email=data.get("email"),
            phone=data.get("phone"),
            data=data.get("data", {})
        )
        # Check if the client already exists by name
        existing_client = db_session.query(Client).filter(
            Client.name == new_client.name).first()

        if existing_client:
            # Update the existing client's missing fields with the new data
            existing_client.idno = existing_client.idno or new_client.idno
            existing_client.company_type = existing_client.company_type or new_client.company_type
            existing_client.vertical = existing_client.vertical or new_client.vertical
            existing_client.address = existing_client.address or new_client.address
            existing_client.bank_code = existing_client.bank_code or new_client.bank_code
            existing_client.bank_name = existing_client.bank_name or new_client.bank_name
            existing_client.bank_address = existing_client.bank_address or new_client.bank_address
            existing_client.iban = existing_client.iban or new_client.iban
            existing_client.tva_code = existing_client.tva_code or new_client.tva_code
            existing_client.fiscal_code = existing_client.fiscal_code or new_client.fiscal_code
            existing_client.director_first_name = existing_client.director_first_name or new_client.director_first_name
            existing_client.director_last_name = existing_client.director_last_name or new_client.director_last_name
            existing_client.country = existing_client.country or new_client.country
            existing_client.email = existing_client.email or new_client.email
            existing_client.phone = existing_client.phone or new_client.phone
            # Merge data dictionaries
            existing_client.data = {**new_client.data, **existing_client.data}

            # Commit the changes to the existing client
            db_session.commit()

            # Return the updated client as JSON with a 200 OK status
            return jsonify({
                "id": existing_client.id,
                "name": existing_client.name,
                "idno": existing_client.idno,
                "company_type": existing_client.company_type,
                "vertical": existing_client.vertical,
                "address": existing_client.address,
                "bank_code": existing_client.bank_code,
                "bank_name": existing_client.bank_name,
                "bank_address": existing_client.bank_address,
                "iban": existing_client.iban,
                "tva_code": existing_client.tva_code,
                "fiscal_code": existing_client.fiscal_code,
                "director_first_name": existing_client.director_first_name,
                "director_last_name": existing_client.director_last_name,
                "country": existing_client.country,
                "email": existing_client.email,
                "phone": existing_client.phone,
                "data": existing_client.data
            }), 200
        # Add the new client to the session and commit
        db_session.add(new_client)
        db_session.commit()

        # Return the created client as JSON with a 201 Created status
        return jsonify({
            "id": new_client.id,
            "name": new_client.name,
            "idno": new_client.idno,
            "company_type": new_client.company_type,
            "vertical": new_client.vertical,
            "address": new_client.address,
            "bank_code": new_client.bank_code,
            "bank_name": new_client.bank_name,
            "bank_address": new_client.bank_address,
            "iban": new_client.iban,
            "tva_code": new_client.tva_code,
            "fiscal_code": new_client.fiscal_code,
            "director_first_name": new_client.director_first_name,
            "director_last_name": new_client.director_last_name,
            "country": new_client.country,
            "email": new_client.email,
            "phone": new_client.phone,
            "data": new_client.data
        }), 201

    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@clients_blueprint.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate the input data
        if not data or not isinstance(data, dict):
            abort(400, description="Invalid input data")

        # Retrieve the client by ID
        client = db_session.query(Client).get(client_id)

        # Check if the client exists
        if not client:
            abort(404, description="Client not found")

        # Update the client fields with the new data
        client.name = data.get("name", client.name)
        client.idno = data.get("idno", client.idno)
        client.company_type = data.get("company_type", client.company_type)
        client.vertical = data.get("vertical", client.vertical)
        client.address = data.get("address", client.address)
        client.bank_code = data.get("bank_code", client.bank_code)
        client.bank_name = data.get("bank_name", client.bank_name)
        client.bank_address = data.get("bank_address", client.bank_address)
        client.iban = data.get("iban", client.iban)
        client.tva_code = data.get("tva_code", client.tva_code)
        client.fiscal_code = data.get("fiscal_code", client.fiscal_code)
        client.director_first_name = data.get(
            "director_first_name", client.director_first_name)
        client.director_last_name = data.get(
            "director_last_name", client.director_last_name)
        client.country = data.get("country", client.country)
        client.email = data.get("email", client.email)
        client.phone = data.get("phone", client.phone)
        client.data = data.get("data", client.data)

        # Commit the changes to the database
        db_session.commit()

        # Return a success message along with the updated client data
        return jsonify({
            "message": "Client updated successfully.",
            "client": {
                "id": client.id,
                "name": client.name,
                "idno": client.idno,
                "company_type": client.company_type,
                "vertical": client.vertical,
                "address": client.address,
                "bank_code": client.bank_code,
                "bank_name": client.bank_name,
                "bank_address": client.bank_address,
                "iban": client.iban,
                "tva_code": client.tva_code,
                "fiscal_code": client.fiscal_code,
                "director_first_name": client.director_first_name,
                "director_last_name": client.director_last_name,
                "country": client.country,
                "email": client.email,
                "phone": client.phone,
                "data": client.data
            }
        }), 200

    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@clients_blueprint.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    try:
        # Retrieve the client by ID
        client = db_session.query(Client).get(client_id)

        # Check if the client exists
        if not client:
            abort(404, description="Client not found")

        # Delete the client from the session
        db_session.delete(client)
        db_session.commit()

        # Return a success message
        return jsonify({"message": "Client deleted successfully."}), 200

    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@clients_blueprint.route('/clients/<int:client_id>/contracts', methods=['GET'])
def get_client_contracts(client_id):
    try:
        # Retrieve all contracts for the specified client (as obligor or obligee)
        contracts = db_session.query(Contract).filter(
            (Contract.obligor_client_id == client_id) |
            (Contract.obligee_client_id == client_id)
        ).all()

        if not contracts:
            return jsonify({"message": "No contracts found for this client."}), 404

        # Create a list of contracts to return
        contract_list = []
        for contract in contracts:
            contract_list.append({
                "id": contract.id,
                "created_date": contract.created_date.strftime('%Y-%m-%d %H:%M:%S') if contract.created_date else None,
                "updated_date": contract.updated_date.strftime('%Y-%m-%d %H:%M:%S') if contract.updated_date else None,
                "obligor_client_id": contract.obligor_client_id,
                "obligee_client_id": contract.obligee_client_id,
                "text": contract.text,
                "data": contract.data
            })

        return jsonify(contract_list), 200

    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))
