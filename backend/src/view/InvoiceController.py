from flask import send_file
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from database import db_session
import io
from database.models import DueInvoice
from flask import Flask, jsonify, request, abort, Blueprint, send_file
from sqlalchemy.exc import SQLAlchemyError
from pyppeteer import launch
import asyncio
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

invoices_blueprint = Blueprint('invoices_blueprint', __name__)


def generate_pdf(html):
    pdf_file_path = './invoice.pdf'  # Specify your desired file path
    pdf_file_path = os.path.join(os.path.dirname(__file__), pdf_file_path)
    browser = launch()
    page = browser.newPage()
    page.setContent(html)
    page.pdf({'path': pdf_file_path})  # Save PDF to the specified path
    browser.close()
    return pdf_file_path


@invoices_blueprint.route("/invoices", methods=["GET"])
def get_invoices():
    try:
        invoices = db_session.query(DueInvoice).all()
        invoice_list = []
        for invoice in invoices:
            print(invoice)
            invoice_dict = invoice.__dict__.copy()
            invoice_dict.pop('_sa_instance_state', None)
            if invoice_dict.get('created_date') == '':
                invoice_dict['created_date'] = None
            if invoice_dict.get('due_date') == '':
                invoice_dict['due_date'] = None
            invoice_dict['due_period'] = str(invoice_dict['due_period'])
            invoice_list.append(invoice_dict)

        return jsonify(invoice_list), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@invoices_blueprint.route("/invoices/<int:invoice_id>", methods=["GET"])
def get_invoice_by_id(invoice_id):
    try:
        invoice = db_session.query(DueInvoice).get(invoice_id)
        if invoice is None:
            abort(404, description="Invoice not found")

        invoice_dict = invoice.__dict__.copy()
        # Remove SQLAlchemy internal state
        invoice_dict.pop('_sa_instance_state', None)
        invoice_dict['due_period'] = str(invoice_dict['due_period'])

        return jsonify(invoice_dict), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@invoices_blueprint.route("/invoices/<int:invoice_id>/html", methods=["GET"])
def get_invoice_html_by_id(invoice_id):
    try:
        invoice = db_session.query(DueInvoice).get(invoice_id)
        if invoice is None:
            abort(404, description="Invoice not found")

        invoice_dict = invoice.__dict__.copy()
        # Remove SQLAlchemy internal state
        invoice_dict.pop('_sa_instance_state', None)
        invoice_dict['due_period'] = str(invoice_dict['due_period'])
        result = {"html": invoice_dict['html']}
        return jsonify(result), 200
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))


@invoices_blueprint.route("/invoices/<int:invoice_id>/pdf", methods=["GET"])
def get_invoice_pdf_by_id(invoice_id):
    try:
        invoice = db_session.query(DueInvoice).get(invoice_id)
        if invoice is None:
            abort(404, description="Invoice not found")

        invoice_dict = invoice.__dict__.copy()
        invoice_dict.pop('_sa_instance_state', None)
        invoice_dict['due_period'] = str(invoice_dict['due_period'])
        invoice_html = invoice_dict['html']

        # Generate PDF synchronously using ThreadPoolExecutor
        pdf_file_path = generate_pdf(invoice_html)

        # Check if the PDF file was generated successfully
        if not os.path.exists(pdf_file_path):
            abort(500, description="PDF generation failed")

        # Send the PDF as a response
        return send_file(pdf_file_path, as_attachment=True, download_name='invoice.pdf', mimetype='application/pdf')

    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))
    except Exception as e:
        abort(500, description=str(e))


@invoices_blueprint.route("/invoices", methods=["POST"])
def create_invoice():
    try:
        data = request.json
        required_fields = ['invoice_type_id', 'due_date']
        if not all(field in data for field in required_fields):
            abort(400, description="Missing required fields")

        invoice_type_id = data.get('invoice_type_id')
        if invoice_type_id is None:
            abort(400, description="invoice_type_id is required")

        due_date = data.get('due_date')
        if due_date is None:
            abort(400, description="due_date is required")
        else:
            due_date = datetime.strptime(due_date, '%d-%m-%Y')

        created_date = data.get('created_date')

        if created_date is None:
            created_date = datetime.now()
        else:
            created_date = datetime.strptime(created_date, '%d-%m-%Y')

        invoice_number = data.get('invoice_number')
        description = data.get('description')
        other_data = data.get('data')

        # Create a new Invoice instance
        new_invoice = DueInvoice(
            invoice_type_id=invoice_type_id,
            invoice_number=invoice_number,
            created_date=created_date,
            due_date=due_date,
            description=description,
            data=other_data
        )
        db_session.add(new_invoice)
        db_session.commit()
        invoice_dict = new_invoice.__dict__.copy()
        invoice_dict.pop('_sa_instance_state', None)
        return jsonify(invoice_dict), 201
    except SQLAlchemyError as e:
        db_session.rollback()
        abort(500, description=str(e))
