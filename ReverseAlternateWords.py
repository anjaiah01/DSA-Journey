# Reverse the alternative words in dot separated string without using inbuilt functions
#     Example:
#     Input= i.like.this.programme.very.much
#     Output= i.ekil.this.emmargorp.very.hcum
####     AVOID USing IN-BUILT funtions

def reverseAltWords(s):
    res=""
    length=len(s)
    currWord=""
    dots=0
    for char in s:
        if char=="." and dots%2==0:
            res+=currWord+"."
            currWord=""
            dots+=1
        elif char=="." and dots%2!=0:
            res+=currWord[::-1]+"."
            currWord=""
            dots+=1
        else:
            currWord+=char
    res+=currWord
    return res

s="motivation.is.emotion.and.action.is.pain"
result=reverseAltWords(s)
print(result)
    