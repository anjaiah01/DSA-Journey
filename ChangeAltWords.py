# Given an string with dot(.) separated .print alternative words with ""xyz"" in between of them
#     Example:
#     Input: "i.will.learn.python.easily"
#     Output: "i.xyz.learn.xyz.easily.xyz"


def changeAltWords(s):
    res=""
    dots=0
    currWord=""
    for char in s:
        if char=="." and dots%2==0:
            res+=currWord+"."
            dots+=1
            currWord=""
        elif char=="." and dots%2!=0:
            res+="xyz"+"."
            currWord=""
            dots+=1
        else:
            currWord+=char
    
    if dots%2!=0:
        res=res+"xyz"
    else:
        res+=currWord
    return res

s="self.decipline.is.the.only.key.to.success.hi"
result=changeAltWords(s)
print(result)
        