# 10. Write a Python program to remove a key from a dictionary. 
def remove_key(dict,key_to_re):
    if key_to_remove in dict:
        del dict[key_to_re]
    else:
        print("key not present")
sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove="d"
remove_key(sample_dict,key_to_remove)
print(sample_dict)




# def remove_key_from_dict(dictionary, key_to_remove):
#     if key_to_remove in dictionary:
#         del dictionary[key_to_remove]

# # Sample dictionary
# sample_dict = {'a': 1, 'b': 2, 'c': 3}

# # Key to remove
# key_to_remove = 'b'

# # Remove the key from the dictionary
# remove_key_from_dict(sample_dict, key_to_remove)

# print("Dictionary after removing the key:", sample_dict)
