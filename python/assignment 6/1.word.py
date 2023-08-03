# Write a txt file which has a word in each line like:
# Hands
# Legs
# India
# Crow
# Rain
# ...

# Write a python code to read the file and store the words in the list

# Write a function to guess a word randomly from the list.

# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter. 
# Display  letters in the clue word that were guessed correctly. 

# Let say word is EVAPORATE

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# You left with 5 chances to guess.

# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on.


# 1)Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# 2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# 3)When the player wins or loses, let them start a new game.
import random

def read_words_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            words_list = [word.strip() for word in file.readlines()]
        return words_list
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

def guess_random_word(word_list):
    if not word_list:
        return None
    return random.choice(word_list)

def hangman_game(word):
    guessed_letters = set()
    chances = 6
    clue_word = ["_" for _ in word]

    print("Welcome to Hangman!")
    print(" ".join(clue_word))

    while chances > 0 and "_" in clue_word:
        letter = input("Guess your letter (type 'quit' to end the game): ")

        if letter == "QUIT":
            print("Quitting the game.")
            return

        if letter in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(letter)

        if letter in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i] == letter:
                    clue_word[i] = letter
        else:
            chances -= 1
            print("Incorrect guess.")
            print("You have", chances, "chances left to guess.")

        print(" ".join(clue_word))

    if "_" not in clue_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of chances. The word was:", word)

if __name__ == "__main__":
    file_name = "words.txt"
    words_list = read_words_from_file(file_name)

    if words_list:
        while True:
            random_word = guess_random_word(words_list)
            hangman_game(random_word)

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break
    else:
        print("No words to play. Please provide a valid words.txt file.")




words = [
    "Hands",
    "Legs",
    "Ind",
    "Cr",
    "Raining",
    # Add more words here as needed
]

file_name = "words.txt"

with open(file_name, "w") as file:
    for word in words:
        file.write(word + "\n")

print(f"The file '{file_name}' has been created with the words.")
