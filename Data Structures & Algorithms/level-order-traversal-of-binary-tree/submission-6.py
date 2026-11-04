# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use BFS to build up a solution.
        # - Start at root
        # - Loop:
        #   - Read all nodes in queue. This is one level of nodes.
        #   - Add all children of those nodes to the queue.
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            count = len(queue)
            level = []

            for i in range(0,count):
                node: TreeNode = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result

