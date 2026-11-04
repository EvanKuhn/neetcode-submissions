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
        # I think for each subtree, you want to return:
        # - Max value of path in subtree, _not_ ending at subroot
        # - Max value of path in subtree _ending_ in subroot
        # This way when considering subtree results, you can take the max of:
        # - Left subtree max_path_no_root
        # - Left subtree max_path_with_root
        # - Left subtree max_path_with_root + cur_value
        # - (And same three for right subtree)
        # Then 

        if not root:
            return 0


        def dfs(node: TreeNode | None) -> Result:
            # Base case
            if not node:
                return Result(-math.inf, -math.inf)

            # if not node.left and not node.right:
            #     return Result(node.val, node.val)

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

            # if node.val == -2 and node.left and node.right:
            #     print("At node -2")
            #     print(f"rl = {rl}")
            #     print(f"rr = {rr}")
            #     print(f"max_to_root = {max_to_root}")
            #     print(f"max_below = {max_below}")

            # if node == root:
            #     print("At root 1")
            #     print(f"rl = {rl}")
            #     print(f"rr = {rr}")
            #     print(f"max_to_root = {max_to_root}")
            #     print(f"max_below = {max_below}")

            return Result(max_to_root, max_below)

        r = dfs(root)
        return max(r.max_to_root, r.max_below)

