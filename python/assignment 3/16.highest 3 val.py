# 16. Write a Python program to find the highest 3 values in a dictionary.
def find_highest_3_values(dictionary):
    # Sort the dictionary items based on their values in descending order
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Get the top 3 values and their corresponding keys
    highest_values = sorted_items[:3]

    # Create a new dictionary with the highest 3 values
    highest_3_dict = dict(highest_values)

    return highest_3_dict

# Example dictionary
example_dict = {
    'a': 10,
    'b': 50,
    'c': 30,
    'd': 70,
    'e': 40
}

highest_3 = find_highest_3_values(example_dict)
print("Highest 3 values in the dictionary:", highest_3)
