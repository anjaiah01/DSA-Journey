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

def sumPrime(n):
    totalSum=0
    primes=[]
    for i in range(n+1):
        if isPrime(i):
            primes+=[i]
            totalSum+=i 
    print(primes)
    return totalSum

n=10
result = sumPrime(n)
print(result)
