# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Use BFS to get the list of nodes at each level
        # Then just pick off the rightmost value

        if not root:
            return []

        values_per_level = []
        queue = deque([root])

        while queue:
            count = len(queue)
            values = []
            for _ in range(count):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values_per_level.append(values)

        return [vals[-1] for vals in values_per_level]