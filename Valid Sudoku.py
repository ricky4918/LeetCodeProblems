#HashSet
#o(n^2)
    
    
    #   0     1     2
#     1 2 3 4 5 6 7 8 9
#   1
# 0 2
#   3
#   4
# 1 5
#   6
#   7
# 2 8
#   9
        
 
class Solution:
    def isValidSudoku(self, board):
        
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)
        
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
                   
