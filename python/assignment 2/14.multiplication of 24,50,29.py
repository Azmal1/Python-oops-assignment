# 14. Print multiplication table of 24, 50 and 29 using loop.
def print_multiplication_table(number):
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


if __name__ == "__main__":
    numbers = [24, 50, 29]

    for number in numbers:
        print_multiplication_table(number)
        print()  # Add a newline for clarity between different tables
