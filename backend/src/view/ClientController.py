from flask import Flask, jsonify, request, abort
from sqlalchemy.exc import SQLAlchemyError
from backend import SessionLocal 
from database.orm import Client, Contract  
from datetime import datetime

app = Flask(__name__)

# Initialize database session
db_session = SessionLocal()


# GET all clients
@app.route("/clients", methods=["GET"])
def get_clients():
    try:
        clients = db_session.query(Client).all()
        return jsonify([client.__dict__ for client in clients]), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# GET a single client by id
@app.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    client = db_session.query(Client).filter(Client.id == client_id).first()
    if not client:
        abort(404, description="Client not found")
    return jsonify(client.__dict__), 200


# POST (create) a new client
@app.route("/clients", methods=["POST"])
def create_client():
    try:
        data = request.json
        new_client = Client(
            name=data['name'],
            idno=data['idno'],
            company_type=data['company_type'],
            vertical=data['vertical'],
            address=data['address'],
            bank_code=data['bank_code'],
            bank_name=data['bank_name'],
            bank_address=data['bank_address'],
            iban=data['iban'],
            tva_code=data['tva_code'],
            fiscal_code=data['fiscal_code'],
            director_first_name=data['director_first_name'],
            director_last_name=data['director_last_name'],
            country=data['country'],
            email=data['email'],
            phone=data['phone'],
            data=data['data']
        )
        db_session.add(new_client)
        db_session.commit()
        return jsonify(new_client.__dict__), 201
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# PUT (update) an existing client
@app.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    client = db_session.query(Client).filter(Client.id == client_id).first()
    if not client:
        abort(404, description="Client not found")

    try:
        data = request.json
        client.name = data.get('name', client.name)
        client.idno = data.get('idno', client.idno)
        client.company_type = data.get('company_type', client.company_type)
        client.vertical = data.get('vertical', client.vertical)
        client.address = data.get('address', client.address)
        client.bank_code = data.get('bank_code', client.bank_code)
        client.bank_name = data.get('bank_name', client.bank_name)
        client.bank_address = data.get('bank_address', client.bank_address)
        client.iban = data.get('iban', client.iban)
        client.tva_code = data.get('tva_code', client.tva_code)
        client.fiscal_code = data.get('fiscal_code', client.fiscal_code)
        client.director_first_name = data.get('director_first_name', client.director_first_name)
        client.director_last_name = data.get('director_last_name', client.director_last_name)
        client.country = data.get('country', client.country)
        client.email = data.get('email', client.email)
        client.phone = data.get('phone', client.phone)
        client.data = data.get('data', client.data)
        client.updated_date = datetime.now()

        db_session.commit()
        return jsonify(client.__dict__), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# DELETE a client
@app.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    client = db_session.query(Client).filter(Client.id == client_id).first()
    if not client:
        abort(404, description="Client not found")
    
    try:
        db_session.delete(client)
        db_session.commit()
        return jsonify({"message": f"Client {client_id} deleted successfully"}), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# GET all contracts for a specific client (obligor)
@app.route("/clients/<int:client_id>/contracts", methods=["GET"])
def get_client_contracts(client_id):
    client = db_session.query(Client).filter(Client.id == client_id).first()
    if not client:
        abort(404, description="Client not found")

    contracts = client.obligor_contracts + client.obligee_contracts  # both types of contracts
    return jsonify([contract.__dict__ for contract in contracts]), 200


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
