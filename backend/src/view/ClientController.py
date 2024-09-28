from flask import Flask, jsonify, request, abort
from sqlalchemy.exc import SQLAlchemyError
import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from database.models import Client, Contract
from database import db_session
from datetime import datetime

app = Flask(__name__)

@app.route("/clients", methods=["GET"])
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


@app.route("/clients/<int:client_id>", methods=["GET"])
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


@app.route("/clients", methods=["POST"])
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


@app.route("/clients/<int:client_id>", methods=["PUT"])
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
        client.director_first_name = data.get("director_first_name", client.director_first_name)
        client.director_last_name = data.get("director_last_name", client.director_last_name)
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


@app.route("/clients/<int:client_id>", methods=["DELETE"])
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


#TODO:
@app.route("/clients/<int:client_id>/contracts", methods=["GET"])
def get_client_contracts(client_id):
    try:
        # Retrieve the client by ID
        client = db_session.query(Client).get(client_id)

        # Check if the client exists
        if not client:
            abort(404, description="Client not found")
        
        # Get all contracts associated with the client
        contracts = client.obligor_contracts + client.obligee_contracts

        # Return the contracts as JSON
        return jsonify([contract.__dict__ for contract in contracts]), 200

    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))



# POST (add) a new contract for a specific client
@app.route("/clients/<int:client_id>/contracts", methods=["POST"])
def add_contract_to_client(client_id):
    client = db_session.query(Client).filter(Client.id == client_id).first()
    if not client:
        abort(404, description="Client not found")

    try:
        data = request.json
        new_contract = Contract(
            obligor_client_id=client_id,
            obligee_client_id=data.get('obligee_client_id'),
            text=data['text'],
            face_value=data['face_value'],
            created_date=datetime.now()
        )
        db_session.add(new_contract)
        db_session.commit()
        return jsonify(new_contract.__dict__), 201
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


if __name__ == "__main__":
    app.run(debug=True)
