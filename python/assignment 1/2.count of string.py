# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# 1..def char_count(string2):
#     count={}
#     for char in string2:
#         count[char]=count.get(char, 0)+1
#     return count
# string=input("enter a string:")
# result=char_count(string)
# print(result)



# 2..

def Character_number_count(str):
    character_count = {}
    for i in str:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count
sample_string = input("enter the string:")
res = Character_number_count(sample_string)
print(res)

