# Print sum of non prime numbers in a given array
#     Example:
#     Input= [4,2,5,7,1]
#     Output= 2+5+7= 14
import math
def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True 
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True 


def SumNonPrime(n):
    total=0
    for i in range(1,n+1):
        if isPrime(i):
            total+=i
    return total 

n=int(input())
result=SumNonPrime(n)
print("Sum of Non-Prime Numbers: {}".format(result))
    
        