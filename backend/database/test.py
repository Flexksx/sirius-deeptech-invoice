from ResponseParser import store_in_db
import json

example_file = "example.json"
data = open(example_file, "r").read()
json_data = json.loads(data)
store_in_db(json_data)

print("Done")
