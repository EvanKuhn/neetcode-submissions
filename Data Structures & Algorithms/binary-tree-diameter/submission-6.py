# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def dfs(node: Optional[TreeNode]) -> tuple[int,int]:
            """Run DFS, return tuple of (height, max_diam) of subtree"""
            if not node:
                return (0,0)
            # print(f"visiting node {node.val}")
            hl, dl = dfs(node.left)
            hr, dr = dfs(node.right)
            curdiam = hl + hr
            maxdiam = max(curdiam, dl, dr)
            # print(f"node {node.val} hl={hl} hr={hr}")
            return (1 + max(hl, hr), maxdiam)

        height, maxdiam = dfs(root)
        return maxdiam
