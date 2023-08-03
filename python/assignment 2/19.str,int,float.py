# 19. From a list containing ints, strings and floats, make three lists to store them separately
def separate_data_types(data_list):
    int_list = []
    str_list = []
    float_list = []

    for item in data_list:
        if isinstance(item, int):
            int_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)
        elif isinstance(item, float):
            float_list.append(item)

    return int_list, str_list, float_list


if __name__ == "__main__":
    # Assuming you have a list with a mix of integers, strings, and floats
    data_list = [10, "Hello", 3.14, "World", 20, 2.718, "Python", 5]

    int_list, str_list, float_list = separate_data_types(data_list)

    print("Integers:", int_list)
    print("Strings:", str_list)
    print("Floats:", float_list)
