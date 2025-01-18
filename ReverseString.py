# Reverse the given string (not use inbuilt functions)?
#     Example
#     Input= “string”
#     Output=”gnirts”

def reverse(s):
    s=list(s)
    length=len(s)
    start=0
    end=length-1
    while(start<end):
        temp=s[end]
        s[end]=s[start]
        s[start]=temp
        start+=1
        end-=1
    return "".join(s)


s="Vjablaks"
result=reverse(s)
print(result)