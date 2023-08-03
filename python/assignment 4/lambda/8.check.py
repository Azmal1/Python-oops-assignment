
# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 
# string_contains=lambda x:bool(x.upper()) or bool(x.lower()),lambda x: len(x)>=10
# string="PaceWisd0m"
# res=string_contains(string)
# print(res)


check_valid_string = lambda s: all(func(s) for func in [str.isupper, str.islower, str.isdigit, lambda x: len(x) >= 10])

input_string = "PaceWisd0m"
if check_valid_string(input_string):
    print("Valid string")
else:
    print("Invalid string")
