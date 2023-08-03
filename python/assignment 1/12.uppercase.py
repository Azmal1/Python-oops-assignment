# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert_to_uppercase(input_string):
    uppercase_count = sum(1 for char in input_string[:4] if char.isupper())

    if uppercase_count >= 2:
        return input_string.upper()
    else:
        return input_string

# Example usage:
sample_string1 = "HeLlo, World!"
sample_string2 = "UPPERCASE"

result1 = convert_to_uppercase(sample_string1)
result2 = convert_to_uppercase(sample_string2)

print(result1)  # Output: HELLO, WORLD!
print(result2)  # Output: UPPERCASE
