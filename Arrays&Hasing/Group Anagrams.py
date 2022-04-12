class Solution:
    def groupAnagrams(self, strs):
        
        res = collections.defaultdict(list)
        
        for s in strs:
            res[tuple(sorted(s))].append(s)
            
        return res.values()
