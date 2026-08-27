# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None  # We'll return this
        tail = None  # Append to this node

        while list1 or list2:
            # Pick the next node to move
            if ((list1 and list2) and list1.val < list2.val) or not list2:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next

            # Append the 'curr' node to the list
            if not head:
                head = curr
                tail = curr
            else:
                tail.next = curr
                tail = curr
            
            curr.next = None
            
        return head            

        