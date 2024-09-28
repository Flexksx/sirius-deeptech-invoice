from openai import OpenAI
import os
import dotenv
from datetime import datetime


class PDFDecoder:
    def __init__(self, pdf_path):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        dotenv.load_dotenv(dotenv_path)
        api_key = os.getenv('OPENAI_API_KEY')
        self.openai = OpenAI(api_key=api_key)
        self.log(f'Initialized OpenAI with API key: {api_key}')

    def log(self, message):
        header = '[AI][PDFDecoder]'
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{header} {current_time} {message}')


pdf = PDFDecoder('test.pdf')
