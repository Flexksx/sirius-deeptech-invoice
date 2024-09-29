from .ResponseParser import store_in_db
import json
import os


current_dir = os.path.dirname(__file__)
example_file = os.path.join(current_dir, "example.json")
data = open(example_file, "r").read()
json_data = json.loads(data)
store_in_db(json_data)

print("Done")
