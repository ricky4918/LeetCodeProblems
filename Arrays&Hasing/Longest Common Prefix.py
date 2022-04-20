class Solution:
    def longestCommonPrefix(self, strs):


        answer = ""

        for i in zip(*strs):
            if len(set(i)) == 1:
                answer += i[0]
            else:
                break
        return answer
            
            
        
            