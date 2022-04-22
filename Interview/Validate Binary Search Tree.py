# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode):

        return self.isValidBSTHelper(root, float('-inf'), float('inf'))



    def isValidBSTHelper(self, n, min, max):

        if not n:

            return True

        if ((n.val > min and n.val < max) and
            self.isValidBSTHelper(n.left, min, n.val)and
            self.isValidBSTHelper(n.right, n.val, max)):
            return True

        return False



        
    

    

