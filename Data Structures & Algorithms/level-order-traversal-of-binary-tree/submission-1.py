# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def recurse(node: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
            # Base case: no node
            if node is None:
                return

            # If we need to extend the result list, add more empty-list elements
            elems_needed = (level + 1) - len(result)
            if elems_needed > 0:
                result += [[]] * elems_needed

            # Append value to correct list, by level
            result[level].append(node.val)

            # Recurse to left and right
            recurse(node.left, level + 1, result)
            recurse(node.right, level + 1, result)

        recurse(root, 0, result)
        return result