from datetime import datetime
from database import db_session
from database.models import Client, Contract
from flask import Flask, jsonify, request, abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

contracts_blueprint = Blueprint('contracts_blueprint', __name__)


@contracts_blueprint.route("/contracts", methods=["GET"])
def get_contracts():
    try:
        contracts = db_session.query(Contract).all()
        contract_list = []
        for contract in contracts:
            contract_dict = contract.__dict__.copy()
            # Remove the internal SQLAlchemy state
            contract_dict.pop('_sa_instance_state', None)
            contract_list.append(contract_dict)
        return jsonify(contract_list), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@contracts_blueprint.route("/contracts/<int:contract_id>", methods=["GET"])
def get_contract_by_id(contract_id):
    try:
        contract = db_session.query(Contract).get(contract_id)
        if contract is None:
            abort(404, description="Contract not found")

        contract_dict = contract.__dict__.copy()
        # Remove SQLAlchemy internal state
        contract_dict.pop('_sa_instance_state', None)

        return jsonify(contract_dict), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@contracts_blueprint.route("/contracts", methods=["POST"])
def create_contract():
    try:
        data = request.json

        # Validate the required fields
        required_fields = ['created_date', 'updated_date',
                           'obligor_client_id', 'obligee_client_id', 'text', 'data']
        if not all(field in data for field in required_fields):
            abort(400, description="Missing required fields")

        # Create a new Contract instance
        new_contract = Contract(
            created_date=datetime.strptime(data['created_date'], '%Y-%m-%d'),
            updated_date=datetime.strptime(data['updated_date'], '%Y-%m-%d'),
            obligor_client_id=data['obligor_client_id'],
            obligee_client_id=data['obligee_client_id'],
            text=data['text'],
            data=data['data']  # Assuming this is a JSON field
        )

        # Add to the session and commit
        db_session.add(new_contract)
        db_session.commit()

        # Prepare the response
        contract_dict = new_contract.__dict__.copy()
        # Remove SQLAlchemy internal state
        contract_dict.pop('_sa_instance_state', None)

        return jsonify({"message": "Contract created successfully", "contract": contract_dict}), 201
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@contracts_blueprint.route('/contracts/<int:contract_id>', methods=['PUT'])
def update_contract(contract_id):
    try:
        # Retrieve the contract by ID
        contract = db_session.query(Contract).filter_by(id=contract_id).first()

        if not contract:
            abort(404, description="Contract not found")

        # Get the JSON data from the request
        contract_data = request.get_json()

        # Update the contract fields
        if 'created_date' in contract_data:
            contract.created_date = datetime.strptime(
                contract_data['created_date'], '%Y-%m-%d')
        if 'updated_date' in contract_data:
            contract.updated_date = datetime.strptime(
                contract_data['updated_date'], '%Y-%m-%d')
        if 'obligor_client_id' in contract_data:
            contract.obligor_client_id = contract_data['obligor_client_id']
        if 'obligee_client_id' in contract_data:
            contract.obligee_client_id = contract_data['obligee_client_id']
        if 'text' in contract_data:
            contract.text = contract_data['text']
        if 'data' in contract_data:
            contract.data = contract_data['data']

        # Commit the changes to the database
        db_session.commit()

        # Manually create a dict of the contract object to return
        updated_contract = {
            "id": contract.id,
            "created_date": contract.created_date.strftime('%Y-%m-%d'),
            "updated_date": contract.updated_date.strftime('%Y-%m-%d'),
            "obligor_client_id": contract.obligor_client_id,
            "obligee_client_id": contract.obligee_client_id,
            "text": contract.text,
            "data": contract.data
        }

        # Return a success message with the updated contract
        return jsonify({"message": "Contract updated successfully", "contract": updated_contract}), 200

    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@contracts_blueprint.route("/contracts/<int:id>", methods=["DELETE"])
def delete_contract(id):
    try:
        # Fetch the contract by ID
        contract = db_session.query(Contract).filter(Contract.id == id).first()

        # If the contract doesn't exist, return 404
        if contract is None:
            return jsonify({"message": "Contract not found"}), 404

        # Delete the contract
        db_session.delete(contract)
        db_session.commit()

        # Return a success message
        return jsonify({"message": f"Contract with id {id} has been deleted"}), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@contracts_blueprint.route('/clients/<int:client_id>/contracts', methods=['GET'])
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
