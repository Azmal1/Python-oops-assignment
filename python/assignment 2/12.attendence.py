
# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

Number_of_classes_held=int(input("enter the Number_of_classes_held:"))
Number_of_classes_attended=int(input("Number_of_classes_attended:"))
percentage=(
Number_of_classes_attended/Number_of_classes_held)*100
print(percentage)
if percentage>=75:
    print('Allowed to sit')
else:
    print("not allowed to sit in exam")