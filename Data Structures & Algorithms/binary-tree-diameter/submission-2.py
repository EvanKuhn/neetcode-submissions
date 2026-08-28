# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def get_child_depths(root: Optional[TreeNode]) -> Tuple[int,int]:
    """
    Return a tuple of max depths (left-subtree, right-subtree)
    """
    l, r = -1, -1
    if root:
        l = 1 + max(get_child_depths(root.left))
        r = 1 + max(get_child_depths(root.right))
    return (l,r)



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depths_l = get_child_depths(root.left)
        depths_r = get_child_depths(root.right)

        max_l = 1 + max(depths_l)
        max_r = 1 + max(depths_r)

        return max(max_l + max_r, sum(depths_l), sum(depths_r))


# def get_depth(root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0
#     return 1 + max(get_depth(root.left), get_depth(root.right))



# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         depth_l = get_depth(root.left)
#         depth_r = get_depth(root.right)

#         print(f"depth_l: {depth_l}")
#         print(f"depth_r: {depth_r}")

#         diam_l = self.diameterOfBinaryTree(root.left)
#         diam_r = self.diameterOfBinaryTree(root.right)


#         print(f"diam_l: {diam_l}")
#         print(f"diam_r: {diam_r}")


#         return max(depth_l+depth_r, diam_l, diam_r)





        