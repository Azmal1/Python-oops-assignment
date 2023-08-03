# 20. Write a Python program to remove all consecutive duplicates of a given string.
# x = input("enter the string:")
# y = set(x)
# res= ''.join(y)
# print(res)


# def duplicate_string(x):
#  word = x.split()
#  res = set(word)
#  return ' '.join(res)
# str = input("enter the string:")
# result = duplicate_string(str)
# print(result) 

# def duplicate_string(x): ---------------------> to remove the single worded string
#     result_str = " "
#     prev_char = None
#     for char in x:
#         if char != prev_char:
#             result_str += char
#         prev_char = char
#     return result_str
# input_str = input("enter the string:")
# res = duplicate_string(input_str)
# print(res)            

def duplicate_string(input_str):
 words = input_str.split()
 result_words = [words[0]]
 for word in words[1:]:
  if word != result_words[-1]:
   result_words.append(word)
 return ' '.join(result_words)
input_str = input("Enter the sentence: ")
result = duplicate_string(input_str)
print(result)

