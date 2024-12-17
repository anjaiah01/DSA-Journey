# Write a function that takes a number as input if the number is a fibonacci number print the number else 
# print the sum of even fibonacci numbers below the number?
#     Example:
#     Input= 8
#     Output= (0,1,1,2,3,5,8)- 2+8 = 10

# Property:
# A number n is a Fibonacci number if and only if one or both of the following expressions is a perfect square:
# 1. 5(n*n)+4
# 2. 5(n*n)-4

# Explanation:
# This property is derived from the closed-form expression of Fibonacci numbers (Binet's formula) and the discriminant of the quadratic equation.

import math
sumEven=0

def isPerfectSqr(n):
    s=math.sqrt(n)
    return s*s==n

def isFibonacci(n):
    if n<0:
        return False
    return isPerfectSqr(5*n*n+4) or isPerfectSqr(5*n*n-4)


def sumEvenFib(n):
    global sumEven
    if n<=0:
        return 0
    a=0
    b=1
    fib=[0,1]
    while a<=n:
        third=a+b
        fib+=[third]
        if a%2==0:
            sumEven+=a 
        print("Before {} {}".format(a,b))
        a,b=b,a+b
        print("After {} {}".format(a,b))
    return fib
    
    
n=input()
n=int(n)
result=isFibonacci(n)
if result=="True":
    print(n)
else:
    res=sumEvenFib(n)
    print("Fibonacci Series: {}".format(res))
    print("Sum of Even Fibonacci Numbers: {}".format(sumEven))
    