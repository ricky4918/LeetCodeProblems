from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        
       
        if k == len(nums):
            return nums
        
      
        count = Counter(nums)
        
        #nlargets(k,iterable,key=)
        return heapq.nlargest(k, count.keys(), key=count.get) 


        #heapq.heapify(list)
        #heapq.heappush(list,value)
        #heapq.heappop(list, value)
        #heapq.heappushpop(list, value)
