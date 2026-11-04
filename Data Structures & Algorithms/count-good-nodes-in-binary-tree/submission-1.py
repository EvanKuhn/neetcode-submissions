# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode | None, max_value_above: int, results: List[int]) -> None:
            if not node:
                return
            if node.val >= max_value_above:
                results.append(node.val)
            max_val = max(max_value_above, node.val)
            dfs(node.left, max_val, results)
            dfs(node.right, max_val, results)

        results = []
        dfs(root, root.val, results)
        return len(results)