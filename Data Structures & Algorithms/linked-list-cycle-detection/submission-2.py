# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast:
            # Search two nodes ahead for the end
            if fast.next is None or fast.next.next is None:
                return False
            
            # Move the fast pointer twice, check if we meet the slow one again
            for _ in range(0,2):
                fast = fast.next
                if fast == slow:
                    return True
                if fast is None:
                    return False

            # Move the slow pointer
            slow = slow.next
            
        return False