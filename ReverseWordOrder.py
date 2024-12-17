# Given a string which is separated by""."" Print reverse of the string with same order of word without using inbuilt function like
#     Example:
#     Input= iam.ccpb.trainee
#     Output= trainee.ccpb.iam

def reverseWordOrder(s):
    res=""
    currWord=""
    length=len(s)
    for char in s:
        if char==".":
            res=currWord+"."+res
            currWord=""
        else:
            currWord+=char
    res=currWord+"."+res
    return res[:-1]

s="purpose.of.your.life.is.more.important.than.the.emotions"
result=reverseWordOrder(s)
print(result)