# 9. Write a Python program to multiply all the items in a dictionary.
def multiply_items(dict):
    mul=1
    for i in dict.values():
        mul =mul* i
    return mul
sample_dict = {'a': 2, 'b': 3, 'c': 4}
res=multiply_items(sample_dict)
print(res)