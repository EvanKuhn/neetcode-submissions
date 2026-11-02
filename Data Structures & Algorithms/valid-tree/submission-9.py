# Need to check for:
# - Cycles
# - Disconnected trees

from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Collect edges
        node_to_edges = defaultdict(list)
        for entry in edges:
            # Save edges in both directions!
            a, b = entry
            node_to_edges[a].append(b)
            node_to_edges[b].append(a)

        # Keep track of visited nodes
        visited = set()

        # Queue of nodes to visit
        # - Assumes 0 is the root
        # - Stores tuples of (node_to_visit, prev_node_to_ignore)
        to_visit = deque([(0,0)])
        
        while to_visit:
            # Get current node to visit, and its previous node
            entry = to_visit.popleft()
            node, prev = entry

            # Check if node was already visited. If not, mark it.
            if node in visited:
                return False
            visited.add(node)

            # Visit each adjacent node (edge) EXCEPT the previous node
            for e in node_to_edges[node]:
                if e != prev:
                    to_visit.append((e, node))

        # If we visited all nodes, we were successful
        return len(visited) == n
