# 7. Write a Python script to merge two Python dictionaries.

def merge_dict(*dict):
    merged_dict=dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
res=merge_dict(dict1,dict2)
print(res)

