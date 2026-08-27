# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Reverse a list in-place. Return the new head of the list.
        - Runs in O(n) time using O(1) space.
        '''
        # Pointers
        before = None
        cur = head

        # Operate on each node
        while cur:
            temp = cur.next
            cur.next = before
            before = cur
            cur = temp
            
        return before

        