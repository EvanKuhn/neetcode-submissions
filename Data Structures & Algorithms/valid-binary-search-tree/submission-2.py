# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

Result = namedtuple('Result', ["is_valid", "minval", "maxval"])

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs_is_valid(node: TreeNode) -> Result:
            minval = node.val
            maxval = node.val

            if node.left:
                result = dfs_is_valid(node.left)
                if not result.is_valid:
                    return Result(False, 0, 0)
                if result.maxval >= node.val:
                    return Result(False, 0, 0)
                minval = result.minval
                
            if node.right:
                result = dfs_is_valid(node.right)
                if not result.is_valid:
                    return Result(False, 0, 0)
                if result.minval <= node.val:
                    return Result(False, 0, 0)
                maxval = result.maxval

            return Result(True, minval, maxval)

        return dfs_is_valid(root).is_valid


