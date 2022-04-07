# sliding window
# not containning any duplicates
# abcabcbb
# 1. set for substring
# 1. remove a and keep going
    #bca 3 bcbb
# 2. remove b and keep going 
    #cab 3  cbb
# 3. remove c and keep going
    #abc  3  bb
#  4. remove left character untill b appear
    #cb  2 b
#  5. remove left character untill b appear
    #b   1
    
    
#time : O(n)
  


class Solution:
    def lengthOfLongestSubstring(self, s):
        
        charSet = set()
        l = 0
        
        res = 0
        
        for r in range(len(s)):
            
            while s[r] in charSet:
                
                charSet.remove(s[l])
                l+=1
                    
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
        
        
