# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# i=int(input("enter the mark:"))

# if i<20:
#     print("F")
# elif i>=25 and i<45:
#     print("E")
# elif i>=45 and i<50:
#     print("D")
# elif i>=50 and i<60:
#     print("C")
# elif i>=60 and i<80:
#     print("B")
# else:
#     print("A")

def marks(input2):
    for i in input2:

        if i<20:
            print("F")
        elif i>=25 and i<45:
            print("E")
        elif i>=45 and i<50:
            print("D")
        elif i>=50 and i<60:
            print("C")
        elif i>=60 and i<80:
            print("B")
        else:
            print("A")

input1=int(input("enter the mark:"))
res=[input1]
marks(res)