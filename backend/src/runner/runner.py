from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, request, abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from datetime import timedelta, datetime
from database import db_session
from database.models import InvoiceType, InvoiceTypeFrequency,Client, Contract
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

engine = create_engine('sqlite:///home/liviu/GigaHack24/sirius-deeptech-invoice/backend/database.db')
Session = sessionmaker(bind=engine)
session = Session()

for invoice_type in invoice_types:
    name = invoice_type.name
    frequency = invoice_type.frequency
    invoice_count = invoice_type.invoice_count
    starting_date = invoice_type.needed_starting_date
    contract_id = invoice_type.contract_id

    print(f"Name: {name}, Contract ID: {contract_id}")
    
    # Calculate next invoice dates
    dates_to_send = []
    current_date = starting_date

    for _ in range(invoice_count):
        dates_to_send.append(current_date)
        
        if frequency == Frequency.DAILY:
            current_date += timedelta(days=1)
        elif frequency == Frequency.WEEKLY:
            current_date += timedelta(weeks=1)
        elif frequency == Frequency.MONTHLY:
            current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
        elif frequency == Frequency.YEARLY:
            current_date = current_date.replace(year=current_date.year + 1)
        elif frequency == Frequency.ONCE:
            break

    if len(dates_to_send) == invoice_count:
        invoice_type.flag = True 
    
    session.commit()
