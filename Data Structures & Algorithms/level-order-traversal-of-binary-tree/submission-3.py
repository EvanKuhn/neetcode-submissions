# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.iterative_solution(root)
        #return self.recursive_solution(root)
    

    def iterative_solution(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque([(1,root)] if root else [])
        result = []

        while stack:
            # Get next node
            level, node = stack.popleft()

            # Extend result list if needed
            if len(result) < level:
                result.append([])
            
            # Add node value
            result[level-1].append(node.val)

            # Add children
            if node.left:
                stack.append((level+1, node.left))
            if node.right:
                stack.append((level+1, node.right))
            
        return result


    def recursive_solution(self, root: Optional[TreeNode]) -> List[List[int]]:
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