# 13. Take 10 integers from keyboard using loop and print their average value on the screen.
def main():
    total_sum = 0
    num_integers = 10

    for i in range(num_integers):
        num = int(input(f"Enter integer {i + 1}: "))
        total_sum += num

    average = total_sum / num_integers
    print(f"The average value is: {average}")


if __name__ == "__main__":
    main()
