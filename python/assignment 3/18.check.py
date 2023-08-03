# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
def all_dicts_empty(input_list):
    for dictionary in input_list:
        if dictionary:
            return False
    return True

# Sample lists
sample_list1 = [{}, {}, {}]
sample_list2 = [{1, 2}, {}, {}]

result1 = all_dicts_empty(sample_list1)
result2 = all_dicts_empty(sample_list2)

print("Return value for sample_list1:", result1)
print("Return value for sample_list2:", result2)


