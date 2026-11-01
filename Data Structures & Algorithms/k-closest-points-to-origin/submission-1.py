import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []

        for p in points:
            x, y = p
            dist = x*x + y*y  # No need to sqrt, for sorting only
            entry = (dist, (x,y))

            # Push entry to heap, sorted by distance. If heap size is larger 
            # than k, pop the top element (farthest from origin).
            heapq.heappush_max(maxheap, entry)
            if len(maxheap) > k:
                heapq.heappop_max(maxheap)
            
        return [list(x[1]) for x in maxheap]

