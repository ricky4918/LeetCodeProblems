# time O(n)



#ABABBA k =2


#1. set L and R pointer at 0
#2. A : 1  B : 0 (hasmap)
#3. window length - count(mostfrequentcharacter) 
#4  move R + 1
#5 if  window length - count(mostfrequentcharacter)  not <= k 
#6 if window size - mfc > 2  decrement mfc count -1 move L + 1


#res : longest substring with same letter


class Solution:
    def characterReplacement(self, s, k):
        
        count = {}
        res = 0
        
        L = 0
        maxf = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R],0)
            maxf = max(maxf, count[s[R]])
            while (R-L + 1) - maxf > k:
                count[s[L]] -=1
                L+=1
            res = max(res, R - L + 1)
        return res
            
            
        
        
