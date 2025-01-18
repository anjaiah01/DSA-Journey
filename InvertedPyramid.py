def invertedPyramid(n):
    for i in range(n,-1,-1):
        left_spaces = (n-i)*" "
        stars = (2*i-1)*"*"
        if i==n:
            print((2*n-1)*"*")
        else:
            print(left_spaces+stars)
n=int(input())
invertedPyramid(n)
            