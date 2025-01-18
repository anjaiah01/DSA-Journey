def pyramid(n):
    for i in range(n):
        left_spaces = n-i 
        print(left_spaces*" "+(2*i+1)*"*")
    
    

n=int(input())
pyramid(n)