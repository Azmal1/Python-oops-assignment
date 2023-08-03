# 11. Write a Python function to reverses a string if it's length is a multiple of 4. 




def reverse_string_if_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]
    else:
        return input_string

# Example usage:
sample_string1 = "abcd"
sample_string2 = "hello"

result1 = reverse_string_if_multiple_of_4(sample_string1)
result2 = reverse_string_if_multiple_of_4(sample_string2)

print(result1)  # Output: dcba
print(result2)  # Output: hello

