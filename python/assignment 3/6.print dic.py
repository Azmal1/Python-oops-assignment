
# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def sqr(n):
    d={n:n*n for n in range(1,x+1)}
    return d
x=10
res=sqr(x)
print(res)