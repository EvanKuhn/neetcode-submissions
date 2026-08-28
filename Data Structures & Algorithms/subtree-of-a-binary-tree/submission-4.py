# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

def print_tree(name: str, root) -> None:
    nodes = deque([root]) if root else deque()
    values = []

    while nodes:
        cur = nodes.popleft()
        if cur is None:
            values.append(None)
        else:
            values.append(cur.val)
            nodes.append(cur.left)
            nodes.append(cur.right)

    while values and values[-1] is None:
        values.pop()

    print(f"{name}: {values}")


def trees_equal(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None and b is None:
        return True
    if (a and not b) or (b and not a):
        return False
    if a.val != b.val:
        return False
    if not trees_equal(a.left, b.left):
        return False
    if not trees_equal(a.right, b.right):
        return False
    return True


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print_tree("root", root)
        print_tree("subroot", subRoot)

        # Base cases
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False

        # Check for trees equal
        if trees_equal(root, subRoot):
            return True

        # Recursive calls to check left and right subtrees
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True

        # No dice
        return False
        