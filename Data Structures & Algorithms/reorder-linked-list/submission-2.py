# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def print_list(name: str, head: Optional[ListNode]) -> None:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(f"{name}: {vals}")


def split(head: Optional[ListNode]) -> Tuple(Optional[ListNode], Optional[ListNode]):
    """
    Given the head of a list, return a tuple of the first half
    of the list, and the second half.
    """
    if not head:
        return (None, None)

    slow, fast = head, head

    while True:
        if fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        else:
            break

    result = (head, slow.next)
    slow.next = None
    return result

def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list in place
    """
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def merge(a: Optional[ListNode], b: Optional[ListNode]) -> None:
    """
    Given two lists, merge them into a single list, with head = a
    """
    while a and b:
        a_next = a.next
        b_next = b.next
        a.next = b
        b.next = a_next
        b = b_next
        a = a_next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # print_list("head", head)

        if not head:
            return 

        a, b = split(head)
        # print_list("a", a)
        # print_list("b", b)

        b = reverse(b)
        # print_list("b", b)

        merge(a, b)
        # print_list("head", head)
        