# 4) Write a Python program to find if a given string starts with a given character using Lambda.
starts_with = lambda string, character: string.startswith(character)

# Test cases
string1 = "Hello, World!"
character1 = "H"
result1 = starts_with(string1, character1)
print(f"Does '{string1}' start with '{character1}'? {result1}")  # Output: Does 'Hello, World!' start with 'H'? True

string2 = "Python is great!"
character2 = "p"
result2 = starts_with(string2, character2)
print(f"Does '{string2}' start with '{character2}'? {result2}")  # Output: Does 'Python is great!' start with 'p'? False
