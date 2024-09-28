import os
import sqlite3
import requests

class Convertor:
    def __init__(self) -> None:
        self.database_path = os.path.join(
            os.path.dirname(__file__), '../database/database.db')

        self.conn = sqlite3.connect(self.database_path)
        self.log('Database connected successfully')

        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON;')

    def log(self, message):
        from datetime import datetime
        currentTime = datetime.now()
        header = "[CONVERTOR]"
        print(f'{header} {currentTime} {message}')

    def get_fixer_rate(self, from_currency, to_currency, api_key):
        url = f"http://data.fixer.io/api/latest?access_key={api_key}&symbols={to_currency},{from_currency}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                rates = data['rates']
                rate = rates[to_currency] / rates[from_currency]
                return rate
            else:
                self.log(f"Error from API: {data['error']['info']}")
        else:
            self.log("Failed to retrieve data from Fixer API.")
        return None

    def get_product_price_by_id(self, product_id):
        """Retrieve the price and currency of a product by its ID from the database."""
        query = "SELECT price, currency FROM products WHERE id = ?"
        self.cursor.execute(query, (product_id,))
        product = self.cursor.fetchone()  # Fetch the price and currency of the product
        return product

    def convert_price_to_mdl(self, product_id, api_key):
        """Convert the price of a specific product to MDL."""
        product = self.get_product_price_by_id(product_id)

        if product:
            price, currency = product
            if currency != 'MDL':  # Only convert if currency is not already MDL
                rate = self.get_fixer_rate(currency, 'MDL', api_key)
                if rate:
                    converted_price = price * rate
                    self.log(f"Price {price} {currency} converted to {converted_price} MDL")
                else:
                    self.log(f"Failed to convert {price} {currency} to MDL")
            else:
                self.log(f"Price {price} MDL does not need conversion.")
        else:
            self.log(f"No product found with ID {product_id}")

# Usage
api_key = '_---------------------------'
product_id = 1  # Example product ID

convertor = Convertor()
convertor.convert_price_to_mdl(product_id, api_key)
