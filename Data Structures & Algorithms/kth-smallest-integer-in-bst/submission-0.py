# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        
        def collect(node: TreeNode | None, values: List[int]):
            if not node:
                return
            collect(node.left, values)
            values.append(node.val)
            collect(node.right, values)

        collect(root, values)
        return values[k-1]