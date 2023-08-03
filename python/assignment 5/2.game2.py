import random


def random_number():
    digits=list(range(10))
    random.shuffle(digits)
    return ''.join(str(d) for d in digits[:4])


def count_cows_bulls(secret_number,guess):
    cows, bulls=0, 0
    for i in range(4):
        if guess[i]==secret_number[i]:
            cows += 1
        elif guess[i] in secret_number:
            bulls += 1
    return cows, bulls

def valid_guess(guess):
    if not guess.isdigit() or len(guess)!=4 or len(set(guess))!=4 :
        return False
    return True

def play_cow_bulls():
    secret_number=random_number()
    attempts=0
    print("welcome to cow and bulls game")

    while True:
        guess=input("enter the 4 digit number(numbers should not be repeated):")
        if not valid_guess(guess):
            print("Invalid input. Please enter a 4-digit number with unique digits.")
            continue
        attempts += 1
        cows, bulls = count_cows_bulls(secret_number,guess)
        if cows==4:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        else:
            print(f"cow{cows},bulls{bulls}")
if __name__=="__main__":
    play_cow_bulls()
    