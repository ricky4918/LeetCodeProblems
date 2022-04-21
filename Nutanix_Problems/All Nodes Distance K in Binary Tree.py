# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        graph = collections.defaultdict(list)        
        queue = collections.deque([root])
        
        while queue:
            
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                queue.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)
                
        queue = collections.deque([target])
        distance = 0
        visited = set()
        visited.add(target)
        result = []
        while queue and distance <= k:
            
            for __ in range(len(queue)):
                node = queue.popleft()
                if distance == k:
                   result.append(node.val)
                    
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            
            distance +=1
        return result
                    
                    
                    
                
                
                
                
                