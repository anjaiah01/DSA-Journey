def ConsVowelCounts(s):
    vowels=set("aeiouAEIOU")
    vowelsCount=0
    consCounts={}
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowelsCount+=1
            else:
                consCounts[char]=consCounts.get(char,0)+1
    
    print("Vowles: {}".format(vowelsCount))
    print(consCounts)
    
s="Its working Fine no need to check!"
ConsVowelCounts(s)