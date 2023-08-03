# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 

original_list = ['red', 'black', 'white', 'green', 'orange']

# Lambda function to check if a string contains a specific substring
contains_substring = lambda s, sub: sub in s

# Test cases
substring1 = 'ack'
result1 = list(filter(lambda x: contains_substring(x, substring1), original_list))
print(f"Original list: {original_list}")
print(f"Substring to search: {substring1}")
print(f"Elements of the said list that contain the specific substring: {result1}")

substring2 = 'abc'
result2 = list(filter(lambda x: contains_substring(x, substring2), original_list))
print(f"\nSubstring to search: {substring2}")
print(f"Elements of the said list that contain the specific substring: {result2}")
