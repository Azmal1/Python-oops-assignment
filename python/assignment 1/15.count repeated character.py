
# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2


# def Character_number_count(str):
#     character_count = {}
#     for i in str:
#         if i in character_count:
#             character_count[i] += 1
#         else:
#             character_count[i] = 1
#     return character_count
# sample_string = input("enter the string:")
# res = Character_number_count(sample_string)
# print(res)



def repeatedCh_count(x):
 character_count = {}
 for i in x:
    if i in character_count:
        character_count[i] += 1
 else:
    character_count[i] = 1
 return character_count
input_str = input("enter the string:")
res = repeatedCh_count(input_str) 

sorted_res = sorted(res.items(), key=lambda item:item[1] , reverse = True)

for char , count in sorted_res:
 if count > 1:
     print(f'{char} {count}')

