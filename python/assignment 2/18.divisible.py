
# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
def is_divisible(num, divisor):
    return num % divisor == 0


if __name__ == "__main__":
    # Assuming you have already obtained the even_numbers and odd_numbers lists
    even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100] # Replace ... with the rest of the even numbers
    odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]   # Replace ... with the rest of the odd numbers

    div_by_4 = [num for num in even_numbers if is_divisible(num, 4)]
    div_by_6 = [num for num in even_numbers if is_divisible(num, 6)]
    div_by_8 = [num for num in even_numbers if is_divisible(num, 8)]
    div_by_10 = [num for num in even_numbers if is_divisible(num, 10)]
    div_by_3 = [num for num in odd_numbers if is_divisible(num, 3)]
    div_by_5 = [num for num in odd_numbers if is_divisible(num, 5)]
    div_by_7 = [num for num in odd_numbers if is_divisible(num, 7)]
    div_by_9 = [num for num in odd_numbers if is_divisible(num, 9)]

    print("Numbers divisible by 4:", div_by_4)
    print("Numbers divisible by 6:", div_by_6)
    print("Numbers divisible by 8:", div_by_8)
    print("Numbers divisible by 10:", div_by_10)
    print("Numbers divisible by 3:", div_by_3)
    print("Numbers divisible by 5:", div_by_5)
    print("Numbers divisible by 7:", div_by_7)
    print("Numbers divisible by 9:", div_by_9)

