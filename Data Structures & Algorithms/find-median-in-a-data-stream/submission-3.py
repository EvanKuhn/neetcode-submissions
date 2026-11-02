class MedianFinder:

    def __init__(self):
        self.minheap_of_largest = []
        self.maxheap_of_smallest = []
        self.median: float | None = None
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count == 0:
            # Finder is empty. Incoming num is the median
            # print(f"setting median = {num} when count={self.count}")
            self.median = num
        elif self.count % 2 == 0:
            # Even number of elements in the finder. Incoming num is the median
            # print(f"setting median = {num} when count={self.count}")
            if num > self.minheap_of_largest[0]:
                self.median = heapq.heappop(self.minheap_of_largest)
                heapq.heappush(self.minheap_of_largest, num)
            elif num < self.maxheap_of_smallest[0]:
                self.median = heapq.heappop_max(self.maxheap_of_smallest)
                heapq.heappush_max(self.maxheap_of_smallest, num)
            else:
                self.median = num
        else:
            # print(f"setting median (complex)")
            # Odd number of elements in the finder.
            # - Take existing (old) median and put it into one of the heaps
            # - Take incoming number and add it to one of the heaps
            assert self.median is not None
            if num > self.median:
                to_largest = num
                to_smallest = self.median
            else:
                to_largest = self.median
                to_smallest = num
            heapq.heappush(self.minheap_of_largest, to_largest)
            heapq.heappush_max(self.maxheap_of_smallest, to_smallest)
            self.median = None
        
        self.count += 1

    def findMedian(self) -> float:
        
        if self.count % 2 == 1:
            assert self.median is not None
            # print(f"findMedian returning {self.median}")
            return self.median
        else:
            # print(f"findMedian complex")
            # print(f"- minheap_of_largest = {self.minheap_of_largest}")
            # print(f"- maxheap_of_smallest = {self.maxheap_of_smallest}")
            return (self.minheap_of_largest[0] + self.maxheap_of_smallest[0]) / 2.0
        
        