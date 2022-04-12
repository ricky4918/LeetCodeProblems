
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

from collections import deque
class Solution(object):

    def cloneGraph(self, node):
       
        # adjList = [[2,4],[1,3],[2,4],[1,3]]

        # we have to initialize ref node

        visited = {} # value: node itself
        if not node: return None

        def dfs(node, visited):

            new_node = Node(node.val)
            visited[node.val] = new_node
            new_neighbors = []

            for n in node.neighbors:
                if n.val not in visited:
                    new_neighbors.append(dfs(n, visited))

                else:
                    new_neighbors.append(visited[n.val])

            new_node.neighbors = new_neighbors
            return new_node

        return dfs(node,visited)

