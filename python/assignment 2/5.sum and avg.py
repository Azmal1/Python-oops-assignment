# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

# def sum_average(num):
#     sum=0
#     avg=0
#     for num in range(1,1+num):
#         if num==0:
#             return 0
#         sum=sum+num
#         avg=sum/num
#     return sum,avg
# input=int(input("enter a no:"))
# res=sum_average(input)
# print(res)

x = input("enter the number:")
num = x.split(',')
for i in range(len(num)):
 num[i] = int(num[i])
sum =sum(num)
avg = sum/len(num)
print("the sum of numbers:",sum)
print("the average of numbers:",avg)

