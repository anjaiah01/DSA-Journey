# Write a function that takes input as string.The function should remove the alternate words in the string.Words are separated by dots".".(Avoid using inbuilt functions)
# Example:
#     Input= i.like.this.programme.very.much
#     output: i.this.very
#######  AVOID in-built Functions ########
def alternateWords(s):
    length=len(s)
    res=""
    dots=0
    temp=""
    for char in s:
        if char=="." and dots%2==0:
            res+=temp+"."
            temp=""
            dots+=1
        elif char=="." and dots%2!=0:
            temp=""
            dots+=1
        else:
            temp+=char
    return res[:-1]

s="pain.is.invitable.suffering.and.emotions.are.optional"
result=alternateWords(s)
print(result)
    
    