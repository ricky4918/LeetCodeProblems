class Solution:
    def letterCombinations(self, digits):

        res = []

        digitToChar = {"2": "abc", 
                       "3": "def", 
                       "4": "ghi", 
                       "5": "jkl", 
                       "6": "mno", 
                       "7": "pqrs", 
                       "8": "tuv", 
                       "9": "wxyz"}

    #digits = "23"
    #Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


        def backtracking(i, curstr):

            if len(curstr) == len(digits):

                res.append(curstr)
                return
            
            for c in digitToChar[digits[i]]:

                backtracking(i+1, curstr + c)

        if digits:
            backtracking(0,"")

    
        return res
                

            



