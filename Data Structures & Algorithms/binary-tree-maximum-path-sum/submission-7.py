# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

Result = namedtuple('Result', ['max_to_root', 'max_below'])

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode | None) -> Result:
            # Base case
            if not node:
                return Result(-math.inf, -math.inf)

            rl = dfs(node.left)
            rr = dfs(node.right)

            max_to_root = max(
                node.val, 
                node.val + rl.max_to_root, 
                node.val + rr.max_to_root,
            )
            max_below = max(
                node.val, 
                rl.max_below, 
                rr.max_below, 
                rl.max_to_root + node.val, 
                rr.max_to_root + node.val, 
                rl.max_to_root + node.val + rr.max_to_root,
            )

            return Result(max_to_root, max_below)

        r = dfs(root)
        return max(r.max_to_root, r.max_below)

