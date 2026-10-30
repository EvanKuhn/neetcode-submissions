import heapq

class Window:
    def __init__(self, nums: List[int], k: int) -> None:
        self._maxheap = []
        self._to_remove = []
        for i in range(0, k):
            self.add(nums[i])

    def add(self, n: int) -> None:
        heapq.heappush_max(self._maxheap, n)
        # print(f"Adding {n}, new max is {self.max()}")

    def remove(self, n: int) -> None:
        # If removing the current max, just remove it
        if self._maxheap[0] == n:
            heapq.heappop_max(self._maxheap)
            # Then check if we can remove any of the previously-removed numbers
            # that weren't max at the time.
            while self._to_remove and self._to_remove[0] == self._maxheap[0]:
                heapq.heappop_max(self._maxheap)
                heapq.heappop_max(self._to_remove)
        else:
            # Not removing the current max. Save the number for later.
            heapq.heappush_max(self._to_remove, n)

    def max(self) -> int:
        assert self._maxheap
        return self._maxheap[0]



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win = Window(nums, k)
        maxes = [win.max()]
        
        for i in range(1, len(nums)-k+1):
            # Drop last number
            win.remove(nums[i-1])

            # Add next number
            win.add(nums[i+k-1])

            # Save current max
            maxes.append(win.max())

        return maxes