# 7) Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. 
# Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
#  Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]] 

asc_sort=lambda x:sorted(x)
Original_Matrix1= [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
Original_Matrix2= [[1, 2, 3], [-2, 4, -5], [1, -1, 1]] 
res=asc_sort(Original_Matrix1)
res1=asc_sort(Original_Matrix2)
print(res,res1)