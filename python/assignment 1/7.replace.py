
# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def replace_poor_with_good(input_string):
    not_index = input_string.find('not')
    poor_index = input_string.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return input_string[:not_index] + 'good' + input_string[poor_index+ 4:]
    else:
        return input_string

sample_string1 = 'The lyrics is not that poor!'
sample_string2 = 'The lyrics is poor!'

result1 = replace_poor_with_good(sample_string1)
result2 = replace_poor_with_good(sample_string2)

print(result1)
print(result2)

