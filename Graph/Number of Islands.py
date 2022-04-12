import collections
class Solution:
    def numIslands(self, grid):
        
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        q = collections.deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def bfs(r,c):
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if( r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r, c) in visit):
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
                
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
                    #dfs(r,c)
        return islands
        

        
        
        
    
        
