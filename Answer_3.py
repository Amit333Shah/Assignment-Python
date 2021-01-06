'''3: Write a Python program to convert the Python dictionary object (sort by key) to
JSON data. Print the object members with indent level 4.
'''

import json

data = {'6': '4', '2': '5', '8': '7', '1': '3'}
parsed = json.dumps(data, sort_keys=True, indent=4)
print(parsed)