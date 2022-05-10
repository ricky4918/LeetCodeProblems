from collections import deque
from textwrap import shorten


class Solution:
    def shortestPath(self, grid, k):
        
        
        m, n = len(grid), len(grid[0])
        # x, y, obstacles, steps
        q = deque([(0,0,k,0)])
        visited = set()
        while q:
            x, y, left, steps = q.popleft()
            
            if (x, y, left) in visited or left <0: 
                continue
            if (x,y) == (m-1,n-1):
                return steps
            visited.add((x,y,left))
                
            if grid[x][y] == 1: 
                left -=1
            
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and  0<= new_y < n:
                    q.append((new_x,new_y, left, steps+1))
                    
        return -1
        
        

        
                    


p = Solution()
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
print(p.shortestPath(grid, k))


#  0 0 0 
#  1 1 0
#  0 0 0 
#  0 1 1 
#  0 0 0