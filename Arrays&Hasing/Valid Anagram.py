import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # time O(n),  space O(s+t)
        if len(s) != len(t):
            return False

        countS, countT = {}, {}


        for i in range(len(s)):

            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS:
            if countS[c] != countT[c]:
                return False

            else:
                return True

    def isAnagramCheating(self, s, t):
        return collections.Counter(s) == collections.Counter(t)

    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)
  
s = "anagram"
t = "nagaram"
res = Solution()
print(res.isAnagram(s,t))
print(res.isAnagramCheating(s,t))
print(res.isAnagram2(s,t))
