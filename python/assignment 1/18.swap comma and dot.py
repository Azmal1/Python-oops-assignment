# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"




# def replace(str1):
#     maketrans = str1.maketrans
#     res = str1.translate(maketrans(',.','.,',''))
#     return res.replace('.','.')
# string = input("enter the string:")
# print(replace(string))

def replace_str(x):
    arr = []
    for i in x:
        if i == ".":
            arr.append(",")
        elif i == ",":
            arr.append(".")
            continue
        elif i == " ":
            continue
        else:
            arr.append(i)
    y = "".join(arr)
    return arr

input_str = input("enter the string:")
print(replace_str(input_str))

