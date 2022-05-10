# Definition for a binary tree node.
from collections import deque
from textwrap import shorten

class TreeNode:
    
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        q = deque()
        q.append(root)
        
        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                if node is not None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
                
        return res

    

        