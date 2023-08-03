# 15. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
#1... from collections import Counter

# def combine_and_add_values(d1, d2):
#     counter1 = Counter(d1)
#     counter2 = Counter(d2)
#     combined_counter = counter1 + counter2
#     return combined_counter

# # Sample dictionaries
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}

# # Combine and add values for common keys
# result_counter = combine_and_add_values(d1, d2)

# print("Sample output:", result_counter)


def combine_and_add_values(d1, d2):
    combined_dict = {}

    # Combine d1 into the result dictionary
    for key, value in d1.items():
        combined_dict[key] = value

    # Add values from d2 to the result dictionary
    for key, value in d2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value

    return combined_dict

# Sample dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine and add values for common keys
result_dict = combine_and_add_values(d1, d2)

print("Sample output:", result_dict)
