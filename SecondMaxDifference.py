# Write a function that takes an array of integers as input and prints the second-maximum difference 
# between any two elements from an array.

#     Example:
#     int arr[]={14, 12, 70, 15, 95, 65, 22, 30};
#     output:
#     First max-difference = 95-12=83
#     Second max-difference = 95 -14 = 81

def secondMaxDiff(arr):
    n=len(arr)
    largest=arr[0]
    small=arr[0]
    secSmall=float('inf')
    
    for num in arr:
        largest = max(largest,num)
        if num < small:
            secSmall=small
            small=num
        elif num>small and num<secSmall:
            secSmall=num
            
    maxDiff = largest-secSmall
    return maxDiff

arr= [14, 12, 70, 15, 95, 65, 22, 30]
result = secondMaxDiff(arr)
print(result)