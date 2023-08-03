
# 10) Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']


# Original_list=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 

# sorted_list=sorted(Original_list, key=lambda x:x.items())
# print(Original_list)
# print(sorted_list)


original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

# Lambda function to assign a sort order to the elements
sort_order = lambda x: (isinstance(x, int), x)

sorted_list = sorted(original_list, key=sort_order)

print("Original list:", original_list)
print("Sort the said mixed list of integers and strings:", sorted_list)
