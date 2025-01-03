class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26   // to store the frequency of characters
        maxFreq=0   // maximum frequency in the current window
        maxLen=0
        
        left=0
        for right in range(len(s)):
            count[ord(str(s[right]))-ord("A")]+=1
            maxFreq=max(maxFreq,count[ord(s[right])-ord("A")])
            
            //current window length
            windowLen=right-left+1

            
            if windowLen-maxFreq>k:
                count[ord(s[left])-ord("A")]-=1
                left+=1
            windowLen=right-left+1
            maxLen=max(maxLen,windowLen)
        return maxLen
            
            
