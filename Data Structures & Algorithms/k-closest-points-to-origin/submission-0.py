import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Construct a max-heap of points, where distance-to-origin is maximized
        # - For now use tuples: (distance, (x,y))
        # - We will remove the max-distance points until only k remain
        heap = []

        for p in points:
            # Compute distance squared. Don't need to sqrt, using for comparison only.
            dist = (p[0] ** 2) + (p[1] ** 2)
            heap.append((dist, p))

        heapq.heapify_max(heap)

        # Get rid of max-distance points until k remain
        while len(heap) > k:
            heapq.heappop_max(heap)
        
        # Get points from heap
        return [x[1] for x in heap]






        