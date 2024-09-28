from flask import Flask, jsonify, request, abort
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from backend import SessionLocal 
from database.orm import Contract, Client

app = Flask(__name__)

# Initialize the database session
db_session = SessionLocal()


# GET all contracts
@app.route("/contracts", methods=["GET"])
def get_contracts():
    try:
        contracts = db_session.query(Contract).all()
        return jsonify([contract.__dict__ for contract in contracts]), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# GET a single contract by ID
@app.route("/contracts/<int:contract_id>", methods=["GET"])
def get_contract(contract_id):
    contract = db_session.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        abort(404, description="Contract not found")
    return jsonify(contract.__dict__), 200


# POST (create) a new contract
@app.route("/contracts", methods=["POST"])
def create_contract():
    try:
        data = request.json
        obligor_client_id = data['obligor_client_id']
        obligee_client_id = data['obligee_client_id']

        # Check if obligor and obligee clients exist
        obligor_client = db_session.query(Client).filter(Client.id == obligor_client_id).first()
        obligee_client = db_session.query(Client).filter(Client.id == obligee_client_id).first()

        if not obligor_client or not obligee_client:
            abort(404, description="Obligor or Obligee client not found")

        new_contract = Contract(
            obligor_client_id=obligor_client_id,
            obligee_client_id=obligee_client_id,
            text=data['text'],
            data=data.get('data')
        )
        db_session.add(new_contract)
        db_session.commit()

        return jsonify(new_contract.__dict__), 201
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# PUT (update) an existing contract
@app.route("/contracts/<int:contract_id>", methods=["PUT"])
def update_contract(contract_id):
    contract = db_session.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        abort(404, description="Contract not found")

    try:
        data = request.json

        contract.obligor_client_id = data.get('obligor_client_id', contract.obligor_client_id)
        contract.obligee_client_id = data.get('obligee_client_id', contract.obligee_client_id)
        contract.text = data.get('text', contract.text)
        contract.data = data.get('data', contract.data)
        contract.updated_date = datetime.now()

        db_session.commit()
        return jsonify(contract.__dict__), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# DELETE a contract
@app.route("/contracts/<int:contract_id>", methods=["DELETE"])
def delete_contract(contract_id):
    contract = db_session.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        abort(404, description="Contract not found")

    try:
        db_session.delete(contract)
        db_session.commit()
        return jsonify({"message": f"Contract {contract_id} deleted successfully"}), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


# GET all contracts for a specific client
@app.route("/clients/<int:client_id>/contracts", methods=["GET"])
def get_client_contracts(client_id):
    client = db_session.query(Client).filter(Client.id == client_id).first()
    if not client:
        abort(404, description="Client not found")

    contracts = client.obligor_contracts + client.obligee_contracts  # both types of contracts
    return jsonify([contract.__dict__ for contract in contracts]), 200


if __name__ == "__main__":
    app.run(debug=True)
