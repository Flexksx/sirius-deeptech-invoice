from flask import Flask
from src.view.ClientController import clients_blueprint
from src.view.ContractController import contracts_blueprint
from src.view.InvoiceTypeController import invoice_type_blueprint
from src.view.InvoiceController import invoices_blueprint

# from ai.AIController import ai_blueprint
app = Flask(__name__)

# Register blueprints
app.register_blueprint(clients_blueprint)
app.register_blueprint(contracts_blueprint)
app.register_blueprint(invoice_type_blueprint)
app.register_blueprint(invoices_blueprint)
# app.register_blueprint(ai_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
