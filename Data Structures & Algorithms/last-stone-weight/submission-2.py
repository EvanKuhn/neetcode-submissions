import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create heap
        maxheap = []
        for w in stones:
            heapq.heappush_max(maxheap, w)

        while True:
            print(maxheap)

            # Check for termination states
            if len(maxheap) == 1:
                return maxheap[0]
            if len(maxheap) == 0:
                return 0

            # Pop next two stones to smash
            x = heapq.heappop_max(maxheap)
            y = heapq.heappop_max(maxheap)

            # Add remaining stone weight after smash smash
            if x > y:
                heapq.heappush_max(maxheap, x-y)



            


