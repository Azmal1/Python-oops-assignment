# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

Sample_String = 'restart'
first_string=Sample_String[0]
modified_string=first_string+Sample_String[1:].replace(first_string,'$')
print(modified_string)



