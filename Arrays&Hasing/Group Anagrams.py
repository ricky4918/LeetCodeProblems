import collections
class Solution:
    def groupAnagrams(self, strs):
        
        res = collections.defaultdict(list)
        
        for s in strs:
            res[tuple(sorted(s))].append(s)

        return res
        #return res.values()
    
    def groupAnagrams2(self, strs):
        
        res = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1   # e a t 1 1 1 


            res[tuple(count)].append(s)
        return res
        #return res.values()
        



strs = ["eat","tea","tan","ate","nat","bat"]
p = Solution()

print(p.groupAnagrams(strs))
print(p.groupAnagrams2(strs))
