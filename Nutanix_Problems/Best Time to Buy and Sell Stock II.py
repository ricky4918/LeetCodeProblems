class Solution:
    def maxProfit(self, prices):


        #input : prices = [7,1,5,3,6,4]

        #output : 7 -> 5-1 = 4,  6-3 = 3 
        
        res = 0
        for i in range(1, len(prices)):

            if prices[i] > prices[i-1]:
                res += (prices[i]- prices[i-1])

        return res

