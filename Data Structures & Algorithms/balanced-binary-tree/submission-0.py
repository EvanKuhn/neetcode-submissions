# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(depth(root.left), depth(root.right))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        dl = depth(root.left)
        dr = depth(root.right)
        return abs(dl - dr) <= 1

