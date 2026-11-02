from typing import Tuple
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def copy_all_nodes(self, node: 'Node') -> Tuple[List['Node'], Dict[int, 'Node']]:
        """
        Returns a tuple of:
        - List of existing Node objects
        - Dict of copied Node objects, *without* neighbors populated
        """
        existing_nodes = []
        copies = {}
        to_visit = deque([node])

        while(to_visit):
            curnode = to_visit.pop()
            if(curnode.val in copies):
                continue
            newnode = Node(val=curnode.val)
            existing_nodes.append(curnode)
            copies[newnode.val] = newnode
            to_visit.extend(curnode.neighbors)

        return existing_nodes, copies

            
            
            



    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        existing_nodes, copied_nodes = self.copy_all_nodes(node)

        for curnode in existing_nodes:
            # Get the corresponding copied node
            copied_node: 'Node' = copied_nodes[curnode.val]

            # Populate neighbors
            for nb in curnode.neighbors:
                copied_node.neighbors.append(copied_nodes[nb.val])
            
        return copied_nodes[node.val]



