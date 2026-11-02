class Solution:
    def has_cycle(self, edges: List[List[int]]) -> bool:

        # Collect edges
        node_to_edges = defaultdict(set)
        for i, edge in enumerate(edges):
            a, b = edge
            node_to_edges[a].add(b)
            node_to_edges[b].add(a)

        # Keep track of visited and nodes to visit next
        visited = set()
        to_visit = deque([(edges[0][0], -1)])  # Queue of (next_node, prev_node) pairs

        while to_visit:
            entry = to_visit.popleft()
            node, prev = entry
            #print(f"visited: {prev} => {node}")

            # If we visited this node, save this edge and loop
            if node in visited:
                #print(f"- loop detected: {node},{prev}")
                return True

            # Record that we visited this node
            visited.add(node)

            # Visit adjecent nodes except the previous node
            for e in node_to_edges[node]:
                if e != prev:
                    to_visit.append((e, node))
        

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cur_edges = []
        for e in edges:
            cur_edges.append(e)
            if self.has_cycle(cur_edges):
                answer = cur_edges[-1]
                return answer

        




    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     answer = []
    #     node_to_edges = defaultdict(set)

    #     # Collect edges
    #     for i, edge in enumerate(edges):
    #         a, b = edge
    #         node_to_edges[a].add(b)
    #         node_to_edges[b].add(a)
    #     print(node_to_edges)

    #     # Keep track of visited and nodes to visit next
    #     visited = set()
    #     to_visit = deque([(edges[0][0], -1)])  # Queue of (next_node, prev_node) pairs
        
    #     while to_visit:
    #         entry = to_visit.popleft()
    #         node, prev = entry
    #         print(f"visited: {prev} => {node}")

    #         # If we visited this node, save this edge and loop
    #         if node in visited:
    #             print(f"- loop detected: {node},{prev}")
    #             answer = [node, prev]
    #             continue

    #         # Record that we visited this node
    #         visited.add(node)

    #         # Visit adjecent nodes except the previous node
    #         for e in node_to_edges[node]:
    #             if e != prev:
    #                 to_visit.append((e, node))

    #     return answer





