# 20. Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]


def extend_list(list1, list2):
    # Concatenate list2 to list1
    new_list = list2 + list1
    return new_list

# Sample data
sample_data1 = [10, 20, 30]
sample_data2 = [40, 50, 60]

output_list = extend_list(sample_data1, sample_data2)
print("Expected output:", output_list)
