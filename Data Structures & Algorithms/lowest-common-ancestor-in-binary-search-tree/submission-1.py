# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Result is a tuple of:
# - List of target nodes (p, q) found in the subtree searched
# - LCA node, if found
Result = namedtuple('Result', ['found', 'lca'])

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node: TreeNode | None, p: TreeNode, q: TreeNode) -> Result:
            if node is None:
                return Result([], None)
            
            # Search children recursively
            rl = dfs(node.left, p, q)
            rr = dfs(node.right, p, q)

            # If we found the LCA, return it
            if rl.lca:
                return rl
            if rr.lca:
                return rr
            
            # Check what we found, and if we found the LCA
            found = rl.found + rr.found
            if node == p:
                found.append(p)
            if node == q:
                found.append(q)
            lca = node if len(found) == 2 else None
            return Result(found, lca)

        result = dfs(root, p, q)
        return result.lca
