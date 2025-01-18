def nonRepeatingChars(s):
    chars={}
    res=""
    for char in s:
        chars[char]=chars.get(char,0)+1
    for char,count in chars.items():
        if count==1:
            res+=char
    return res
    
s="daddy"
result=nonRepeatingChars(s)
print(result)