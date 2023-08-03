
# 20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
def square_elements(input_list):
    square_list = [num ** 2 for num in input_list]
    return square_list


if __name__ == "__main__":
    # Assuming you have a list of integer elements
    integer_list = [1, 2, 3, 4, 5]

    square_list = square_elements(integer_list)

    print("Original List:", integer_list)
    print("Square List:", square_list)


