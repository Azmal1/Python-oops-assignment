
#  3) Write a Python program to sort a list of dictionaries using Lambda. 

original_list_of_dicts = [
    {'name': 'John', 'age': 25, 'score': 90},
    {'name': 'Alice', 'age': 30, 'score': 85},
    {'name': 'Bob', 'age': 22, 'score': 95},
    {'name': 'Eve', 'age': 28, 'score': 88}
]

# Sort the list of dictionaries based on the 'name' key
sorted_list_by_name = sorted(original_list_of_dicts, key=lambda x: x['name'])

# Sort the list of dictionaries based on the 'age' key
sorted_list_by_age = sorted(original_list_of_dicts, key=lambda x: x['age'])

# Sort the list of dictionaries based on the 'score' key
sorted_list_by_score = sorted(original_list_of_dicts, key=lambda x: x['score'])

print("Original list of dictionaries:")
print(original_list_of_dicts)

print("\nSorting the list of dictionaries by name:")
print(sorted_list_by_name)

print("\nSorting the list of dictionaries by age:")
print(sorted_list_by_age)

print("\nSorting the list of dictionaries by score:")
print(sorted_list_by_score)

#  3) Write a Python program to sort a list of dictionaries using Lambda. 
# Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
# Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}] 

original_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
                 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Sorting the list of dictionaries based on the 'make' key
sorted_list = sorted(original_list, key=lambda x: x['make'])

print("Original list of dictionaries:", original_list)
print("Sorting the List of dictionaries:", sorted_list)
