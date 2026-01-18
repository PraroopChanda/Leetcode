"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen={}
        def dfs(node):
            if node in seen:
                return seen[node]

            copy_node=Node(node.val)
            seen[node]=copy_node

            for neigh in node.neighbors:
                copy_node.neighbors.append(dfs(neigh))

            return copy_node      

        if node is None:
            return None
        else:
            return dfs(node)    
            

        
        