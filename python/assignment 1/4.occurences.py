# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'





def replace_occurrences(input_string):
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    return modified_string

sample_string = 'restart'
result = replace_occurrences(sample_string)
print(result)








