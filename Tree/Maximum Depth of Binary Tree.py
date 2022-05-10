# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return 1 + max(self.maxDepthDFS(root.left), self.maxDepthDFS(root.right))
        
        
        
        
        
        
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        level = 1
        q  = collections.deque([root])
        
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level += 1
        return level
            
        
        
        
        
        
   
                        
        
        
        
        
        
    
        
