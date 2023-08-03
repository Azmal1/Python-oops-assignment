# 11. Write a Python program to sort a dictionary by key.
def sort_dict_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

# Sample dictionary
sample_dict = {3: 'apple', 1: 'orange', 2: 'banana'}

# Sort the dictionary by key
sorted_dict = sort_dict_by_key(sample_dict)

print("Dictionary sorted by key:", sorted_dict)
