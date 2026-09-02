import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Maintain a max-heap
        heapq.heapify_max(stones)

        while stones:
            # Check for stopping point: single stone remaining
            if len(stones) == 1:
                return stones[0]

            # Smash the next two largest stones
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            z = x - y
            assert z >= 0

            # Add back the remains
            if z > 0:
                heapq.heappush_max(stones, z)
        
        return 0
        