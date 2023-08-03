
# 17. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

def match_key_values(dict1, dict2):
    matching_keys = set(dict1.keys()) & set(dict2.keys())
    result = {}

    for key in matching_keys:
        if dict1[key] == dict2[key]:
            result[key] = dict1[key]

    return result

# Sample dictionaries
dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

matched_values = match_key_values(dict1, dict2)

if matched_values:
    for key, value in matched_values.items():
        print(f"{key}: {value} is present in both x and y")
else:
    print("No matching key values found.")
