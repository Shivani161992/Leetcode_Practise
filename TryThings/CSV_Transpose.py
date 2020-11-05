
def change_key(input_data, required_key):
    for k, v in input_data.items():
        if isinstance(v, dict):
            change_key(v, required_key)
        if k == required_key:
            value= input_data[k]
            input_data[k] = '*' * len(value)
            return
import json
with open('/Users/shivani/Downloads/Example_Raw.txt') as json_file:
    input_data = json.load(json_file)
    scrub_keys = ['name', 'phone', 'address', 'card_number']
    for key in scrub_keys:
        change_key(input_data, key)







