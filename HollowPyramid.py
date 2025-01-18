def hollowPyramid(n):
    for i in range(n):
        left_spaces =(n-i-1)*" "
        if i==0:
            print(left_spaces+"*")
        else:
            hollow_spaces = (2*i-1)*" "
            print(left_spaces+"*"+hollow_spaces+"*")
    print((n)*"* ")
n=int(input())
hollowPyramid(n)