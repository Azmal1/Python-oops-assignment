# 8.  Write a Python program to sum all the items in a dictionary.
# def sum_dict_items(dictionary):
#     total_sum = sum(dictionary.values())
#     return total_sum

# # Sample dictionary
# sample_dict = {'a': 10, 'b': 20, 'c': 30}

# # Calculate the sum of all items
# result_sum = sum_dict_items(sample_dict)

# print("Sum of all items in the dictionary:", result_sum)


def sum_item(dictionary):
    totl_sum=sum(dictionary.values())
    return totl_sum
sample_dict = {'a': 10, 'b': 20, 'c': 30}
res=sum_item(sample_dict)
print(res)  