from openai import OpenAI
import json
import os
import dotenv
from datetime import datetime
import time


class ContractDecoder:
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        dotenv.load_dotenv(dotenv_path)
        api_key = os.getenv('OPENAI_API_KEY')
        self.assistant_id = os.getenv('DECODER_ASSISTANT_ID')
        self.client = OpenAI(api_key=api_key)
        self.log(f'Initialized OpenAI with API key: {api_key}')

    def log(self, message):
        header = '[AI][ContractDecoder]'
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{header} {current_time} {message}')

    def decode_file(self, file_path):
        self.log(f'Started decoding file: {file_path}')
        file = self.__upload_file(file_path)
        message = {
            "role": "user",
            "content": "Extract all data from this contract.",
            "attachments": [
                {
                    "file_id": file.id,
                    "tools": [{"type": "file_search"}]
                }
            ]
        }
        response = self.client.beta.threads.create_and_run(
            assistant_id=self.assistant_id,
            thread={
                "messages": [
                    message
                ]
            }
        )
        run_id = response.id
        thread_id = response.thread_id
        self.log(f'Initiated run with ID: {run_id} on thread: {thread_id}')
        run_status = self.__retrieve_run(run_id, thread_id)
        while run_status != 'completed':
            time.sleep(0.5)
            self.log(f'Run {run_id} status: {run_status}')
            run_status = self.__retrieve_run(run_id, thread_id)
            if run_status == 'failed':
                self.log(f'Run failed SUKA BLYAT')
                return None
        self.log(f'Run completed: {run_status}')
        last_message = self.__get_last_message(thread_id)
        self.log(f'Extracted answer: {last_message}')
        json_answer = json.loads(last_message)
        return json_answer

    def __upload_file(self, file_path):
        self.log(f'Uploading file: {file_path}')
        file = self.client.files.create(
            file=open(file_path, 'rb'), purpose="assistants")
        self.log(f'Uploaded file: {file}')
        return file

    def __retrieve_run(self, run_id, thread_id):
        run_retrieval = self.client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        return run_retrieval.status

    def __get_last_message(self, thread_id):
        thread_messages = self.client.beta.threads.messages.list(
            thread_id=thread_id)
        self.log(f'Fetched thread messages for thread: {thread_id}')
        return thread_messages.data[0].content[0].text.value
