import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        for i in range(0,k-1):
            heapq.heappop_max(heap)
        return heap[0]