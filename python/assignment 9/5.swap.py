
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

def swap(string1,string2):
    modified_string1=string2[:2]+string1[2:]
    modified_string2=string1[:2]+string2[2:]
    return modified_string1,modified_string2



string1='abc'
string2='xyz'
res=swap(string1,string2)
print(res)