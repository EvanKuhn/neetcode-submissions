# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_length(head: Optional[ListNode]) -> int:
    """Return the length of the list"""
    n = 0
    while head:
        n += 1
        head = head.next
    return n


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Determine the total number of nodes, and the number to skip
        list_len = get_length(head)
        to_skip = list_len - n

        # Move pointers to the node we want to remove
        curr = head
        prev = None

        while to_skip:
            prev = curr
            curr = curr.next
            to_skip -= 1
        
        # Remove the node
        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        return head

        

        