def isPower(base,num):
    if num%base!=0:
        return False
    
    while num%base==0:
        num/=base
    return  num==1

def powersOfNumbers(base,num):
    res=[]
    for i in range(len(num)):
        if isPower(base,num[i]):
            res.append(num[i])
    return res

base=5
num=[3,4,5,9,27,81,34]
res=powersOfNumbers(base,num)
print(res)
            
    