'''4: Write a Python program to sort a list of dictionaries using Lambda.
 Original list of dictionaries :
 [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
 Sorting the List of dictionaries :
 [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]'''


data = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
                                                            'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Original List")
print(data, "\n")

print("Sorting the List of dictionaries :")
data.sort(key=lambda x: x['color'])
print(data)
