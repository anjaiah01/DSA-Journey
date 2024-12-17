# Write the programme for Fibonacci numbers in given input?
#     Example:
#     Input= 8
#     Output= 0,1,1,2,3,5,8,13


def FibonacciSeries(n):
    if n<=0:
        return []
    
    series=[0,1]
    while series[-1]<=n:
        fib=series[-1]+series[-2]
        series.append(fib)   
    return series
            
            
n=int(input())
series=FibonacciSeries(n)
print("{} Fibonacci Numbers: {}".format(n,series))