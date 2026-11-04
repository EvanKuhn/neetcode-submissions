# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

Result = namedtuple('Result', ['height', 'status'])

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode | None) -> Result:
            if not node:
                return Result(0, True)
            rl = dfs(node.left)
            rr = dfs(node.right)
            height = 1 + max(rl.height, rr.height)
            diff = abs(rl.height - rr.height)
            status = rl.status and rr.status and (diff <= 1)
            return Result(height, status)

        return dfs(root).status
        