from collections import Counter


class Solution:

    def topKFrequent(self, nums, k):

        #bucket sort

        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) ==k:
                    return res


p = Solution()
nums = [1,1,1,2,2,5,5,5,5,5,5,5,3]
k = 2
print(p.topKFrequent(nums,k))