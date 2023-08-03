
# 2) Write a Python program to sort a list of tuples using Lambda. 
# Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



Original_list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_list=sorted(Original_list, key=lambda x:x[1])
print(Original_list)
print(sorted_list)  