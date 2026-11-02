# Need to check for:
# - Cycles
# - Disconnected trees

from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Collect edges
        node_to_edges = defaultdict(list)
        for entry in edges:
            a, b = entry
            node_to_edges[a].append(b)
            node_to_edges[b].append(a)

            # node = min(a, b)
            # adj = max(a, b)
            # node_to_edges[node].append(adj)
        print(node_to_edges)

        visited = set()
        to_visit = deque([(0,0)])  # tuple of (node_to_visit, prev_node_to_ignore)
        

        # Can we assume that 0 is the root?

        while to_visit:
            entry = to_visit.popleft()
            #print(f"entry = {entry}")
            node, prev = entry

            # Check if node was already visited. If not, mark it.
            if node in visited:
                return False
            visited.add(node)

            # Visit each edge
            for e in node_to_edges[node]:
                if e != prev:
                    to_visit.append((e, node))

        return len(visited) == n
        #return True
