# 13. Write a Python program to check whether a string starts with specified characters.
# def starts_with_specified_characters(string, specified_characters):
#     return string.startswith(specified_characters)

# if __name__ == "__main__":
#     user_input = input("Enter a string: ")
#     characters_to_check = input("Enter specified characters: ")

#     if starts_with_specified_characters(user_input, characters_to_check):
#         print("The string starts with specified characters.")
#     else:
#         print("The string does not start with specified characters.")




def string_character(str2,starting_char2):
    if str2[0]==starting_char2[0]:
        print("The string starts with specified characters.")
    else:
          print("The string does not start with specified characters.")



str1=input("enter the string:")
starting_char=input("enter the starting character")
result=string_character(str1,starting_char)
print(result)