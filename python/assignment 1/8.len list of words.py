# 8. Write a Python function that takes a list of words and returns the length of the longest one. 
def find_longest_word_length(word_list):
    longest_length = 0

    for word in word_list:
        word_length = len(word)
        if word_length > longest_length:
            longest_length = word_length

    return longest_length

# Example usage:
words_list = ['apple', 'banana', 'grapefruit', 'orange', 'kiwi']
result = find_longest_word_length(words_list)
print("The length of the longest word:", result)
  