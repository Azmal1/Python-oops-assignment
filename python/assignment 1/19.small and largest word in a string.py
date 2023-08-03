# 19. Write a Python program to find smallest and largest word in a given string.
def find_smallest_and_largest_word(input_string):
    words = input_string.split()
    
    # Initialize variables to store the smallest and largest words
    smallest_word = None
    largest_word = None

    for word in words:
        # Remove any punctuation or special characters from the word
        cleaned_word = ''.join(char for char in word if char.isalnum())

        # Update smallest_word and largest_word
        if smallest_word is None or len(cleaned_word) < len(smallest_word):
            smallest_word = cleaned_word

        if largest_word is None or len(cleaned_word) > len(largest_word):
            largest_word = cleaned_word

    return smallest_word, largest_word

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    smallest, largest = find_smallest_and_largest_word(input_string)
    print(f"Smallest word: {smallest}")
    print(f"Largest word: {largest}")
