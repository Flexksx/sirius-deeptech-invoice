import requests
# class Convertor:
#     def __init__(self) -> None:
#         # '../../database/database.db'
#         self.database_path = os.path.join(
#             os.path.dirname(__file__), '../../database/database.db')

#         self.conn = sqlite3.connect(self.database_path)
#         self.log('Database connected successfully')

#         self.cursor = self.conn.cursor()
#         self.conn.execute('PRAGMA foreign_keys = ON;')
#         self.contract = DBContracts(self.conn)

def get_fixer_rate(from_currency, to_currency, api_key):
    url = f"http://data.fixer.io/api/latest?access_key={api_key}&symbols={to_currency},{from_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            rates = data['rates']
            rate = rates[to_currency] / rates[from_currency]
            return rate
        else:
            print(f"Error from API: {data['error']['info']}")
    else:
        print("Failed to retrieve data from Fixer API.")
    return None

api_key = '____________________'


rate = get_fixer_rate('USD', 'MDL', api_key)

if rate:
    print(f"Exchange rate from USD to MDL: {rate}")
else:
    print("Failed to retrieve the exchange rate.")
