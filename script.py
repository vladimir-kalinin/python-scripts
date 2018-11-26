import numpy

def factorial(a):
    if a == 1:
        return 1
    else:
        return a*factorial(a-1)

def fact(a):
    s = 1
    for i in range(1,a+1):
        s = s*i
    return s

# print(factorial(100))
print(fact(1000))