# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Run BFS
        # At each iteration, nodes in the queue = nodes at that level
        # For each node:
        # - output its value, or "none"
        # - append its children to the queue (if node is not None)
        queue = deque([root])
        tokens = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    tokens.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    tokens.append("none")
        
        encoded = str(tokens)
        #print(f"encoded = {encoded}")
        return encoded



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print(f"deserializing: {data}")

        # Process string into list of values
        assert(data[0] == "[")
        assert(data[-1] == "]")
        data = data[1:-1]
        data = data.replace("'", "")
        strvals = data.split(', ')
        values = deque([None if v == "none" else int(v) for v in strvals])
        # print(f"transformed to: {values}")

        # Check for empty try
        if not values:
            return None
        rootval = values.popleft()
        if rootval is None:
            return None

        # Construct tree from values
        root = TreeNode(rootval)
        queue = deque([root])

        while queue:
            curnode = queue.popleft()
            lval = values.popleft()
            rval = values.popleft()

            if lval is not None:
                curnode.left = TreeNode(lval)
                queue.append(curnode.left)
            if rval is not None:
                curnode.right = TreeNode(rval)
                queue.append(curnode.right)

        return root
