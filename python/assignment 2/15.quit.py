
# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

def get_integer_input():
    while True:
        user_input = input("Enter an integer (press 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            num = int(user_input)
            yield num
        except ValueError:
            print("Invalid input. Please enter an integer or press 'q' to quit.")


def main():
    total_sum = 0
    product = 1
    num_count = 0

    for num in get_integer_input():
        total_sum += num
        product *= num
        num_count += 1

    if num_count == 0:
        print("No numbers were entered.")
    else:
        average = total_sum / num_count
        print(f"Average: {average}")
        print(f"Product: {product}")


if __name__ == "__main__":
    main()
