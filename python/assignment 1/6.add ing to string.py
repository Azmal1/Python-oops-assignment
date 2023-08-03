# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'

def modify_string(input_string):
    if len(input_string) < 3:
        return input_string

    if input_string.endswith('ing'):
        return input_string + 'ly'
    else:
        return input_string + 'ing'

sample_string1 = 'abc'
sample_string2 = 'string'

result1 = modify_string(sample_string1)
result2 = modify_string(sample_string2)

print(result1)
print(result2)
