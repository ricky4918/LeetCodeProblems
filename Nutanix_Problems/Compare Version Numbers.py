''' 
    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.   
'''



class Solution:
    def compareVersion(self, version1: str, version2: str):

        v1 = version1.split(',')
        v2 = version2.split(',')


        for i in range(max(len(v1), len(v2))):

            n1 = 0 if i >= len(v1) else int(v1[i])
            n2 = 0 if i >= len(v2) else int(v2[i])


            if n1 > n2:
                return 1
            
            elif n2> n1:
                return -1
        
        return 0


        


        