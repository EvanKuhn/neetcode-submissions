"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(curnode: 'Node') -> 'Node':
            # If we visited this node, return the copy
            if curnode in old_to_new:
                return old_to_new[curnode]

            # Copy this node and save it to the Dict
            newnode = Node(curnode.val)
            old_to_new[curnode] = newnode

            # Copy all neighbors via recursive calls
            for nb in curnode.neighbors:
                newnode.neighbors.append(dfs(nb))

            # Return the copied node
            return newnode


        return dfs(node) if node else None
