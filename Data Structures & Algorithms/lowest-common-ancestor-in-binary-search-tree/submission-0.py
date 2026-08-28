# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while True:
            # Check for ancestor descended from itself
            if p.val == cur.val or q.val == cur.val:
                return cur

            # Both nodes to the left
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # Both nodes to the right
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # One to left and one to right. We found LCA.
            else:
                return cur
            