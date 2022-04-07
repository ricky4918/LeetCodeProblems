class Solution:
    def checkInclusion(self, s1, s2):
        
        #s1 = ab
        #s2 = eidbaooo

        if len(s1) > len(s2):
            return False
        
        
        length_of_s1 = len(s1)
        s1_counter = Counter(s1) # {a: 1 b: 1}
        window_counter = Counter() #{          }
        
        for i,c in enumerate(s2):
            
            window_counter[c] += 1 
            
                        #2
            if i >= length_of_s1:
                element_from_left = s2[i-length_of_s1] 
                
                if window_counter[element_from_left] == 1:
                    del window_counter[element_from_left]
                else: 
                    window_counter[element_from_left] -=1
            
            if window_counter == s1_counter:
                return True
        
        return False
