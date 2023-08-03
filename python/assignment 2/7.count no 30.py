
# 7. Write a Python program that counts the number of elements within a list that are greater than 30.
def count_elements_greater_than_30(lst):
    count = 0
    for element in lst:
        if element > 30:
            count += 1
    return count


if __name__ == "__main__":
    # Example list, you can replace it with any list of integers.
    my_list = [10, 25, 40, 15, 50, 30, 35, 45]

    num_elements_greater_than_30 = count_elements_greater_than_30(my_list)
    print(f"The number of elements greater than 30 is: {num_elements_greater_than_30}")
