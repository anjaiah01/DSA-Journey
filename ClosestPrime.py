# Write a function that takes input as an integer number and prints the closest prime integer to that number. 
# The closest prime can be greater or smaller than the passed input integer. 
# If there are equi-distant prime-numbers, print both
#     Example:
#     Input= 4
#     Output= 3


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

def ClosestPrime(n):
    left=n-1
    right=n+1
    while not isPrime(left) and not isPrime(right):
        left-=1
        right+=1
        
    if isPrime(left) and isPrime(right):
        return "These are at equal distance prime Numbers to {}: {} {}".format(n,left,right)
    elif isPrime(left):
        return "Closest Prime Number to {} is : {}".format(n,left)
    return "Closest Prime Number to {} is : {}".format(n,right)

n=int(input())
result=ClosestPrime(n)
print(result)
        