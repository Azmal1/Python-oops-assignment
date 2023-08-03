# 13. Write a Python program to remove duplicates from Dictionary.



def remove_duplicates_from_dict(dictionary):
    unique_dict = {}
    for key, value in dictionary.items():
        if key not in unique_dict:
            unique_dict[key] = value
    return unique_dict

# Sample dictionary with duplicates
sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2,'a':1}

# Remove duplicates
result_dict = remove_duplicates_from_dict(sample_dict)

print("Dictionary after removing duplicates:", result_dict)



# d={'a':1,'b':2,'c':4,'a':1}
# print(dict(set(d.items())))