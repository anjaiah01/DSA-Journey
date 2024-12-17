def addLists(list_a,list_b):
    res=[]
    smallLen=min(len(list_a),len(list_b))
    
    i=0
    while i<smallLen:
        res+=[list_a[i]]
        res+=[list_b[i]]
        i+=1
    while(i<len(list_a)):
        res+=[list_a[i]]
        i+=1
    while i<len(list_b):
        res+=[list_b[i]]
        i+=1 
    
    return res


list_a=[1,2,3,4,5]
list_b=[11,12,13,14,15]
result=addLists(list_a,list_b)
print(result)




def addLists(list_a, list_b):
    # Interleave elements from both lists using zip
    res = [x for pair in zip(list_a, list_b) for x in pair]
    # Add remaining elements from the longer list
    res.extend(list_a[len(list_b):] or list_b[len(list_a):])
    return res

list_a = [1, 2, 3, 4, 5]
list_b = [11, 12, 13, 14, 15]
result = addLists(list_a, list_b)
print(result)
