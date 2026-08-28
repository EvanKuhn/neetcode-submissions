# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Start from root. Travel down the right children until you hit a leaf
        # - Record your path in a stack, with values (level, node)
        # - Record each value seen in a results array, only if you don't already have a value for that level
        # Once you hit a leaf, go to the previous node (in the stack), 
        #   travel to it's left child, and then down again to right children.

        path: List[Tuple[int,TreeNode]] = []
        result: List[int] = []
        cur: Tuple[int,TreeNode] = (1, root)  # level, node


        while cur:
            cur_level, cur_node = cur

            # If we reach a nonexistent node, go up the path to the last parent and try its left child
            if cur_node is None:
                if path:
                    parent_level, parent_node = path.pop()
                    cur = (parent_level+1, parent_node.left)
                else:
                    cur = None  # We are done processing the tree
                continue

            # If we don't have a result for this level, record this node's value
            if len(result) < cur_level:
                result.append(cur_node.val)

            # Go to the right child
            path.append(cur)
            cur = (cur_level+1, cur_node.right)

        return result

        