import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):

        if not k:
            return [target.val]

        
        graph  = collections.defaultdict(list)
        queue = collections.deque([root])


        while queue:

            node = queue.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)

                queue.append(node.left)
