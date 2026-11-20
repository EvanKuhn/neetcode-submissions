"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Initialize a map from old node to new node
        old_to_new_node_map = {}
        cur = head
        while cur:
            old_to_new_node_map[cur] = Node(cur.val)
            cur = cur.next

        # For each old node, populate the next and random pointers
        cur_old = head
        while cur_old:
            cur_new = old_to_new_node_map[cur_old]
            next_new = None if cur_old.next is None else old_to_new_node_map[cur_old.next]
            random_new = None if cur_old.random is None else old_to_new_node_map[cur_old.random]

            cur_new.next = next_new
            cur_new.random = random_new

            cur_old = cur_old.next

        return old_to_new_node_map[head]
