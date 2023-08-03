
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

def swap_first_two_chars(str1, str2):
    modified_str1 = str2[:2] + str1[2:]
    modified_str2 = str1[:2] + str2[2:]
    result = f"{modified_str1} {modified_str2}"
    return result

sample_str1 = 'abc'
sample_str2 = 'xyz'
result = swap_first_two_chars(sample_str1, sample_str2)
print(result)
