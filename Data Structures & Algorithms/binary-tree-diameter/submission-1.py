# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def get_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(get_depth(root.left), get_depth(root.right))



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth_l = get_depth(root.left)
        depth_r = get_depth(root.right)

        print(f"depth_l: {depth_l}")
        print(f"depth_r: {depth_r}")

        diam_l = self.diameterOfBinaryTree(root.left)
        diam_r = self.diameterOfBinaryTree(root.right)


        print(f"diam_l: {diam_l}")
        print(f"diam_r: {diam_r}")


        return max(depth_l+depth_r, diam_l, diam_r)





        