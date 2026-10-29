from collections import defaultdict
from typing import Tuple

class Solution:
    def filter_inputs(self, nums: List[int]) -> List[int]:
        '''
        Filter out numbers that appear more than twice, or zeroes
        that appear more than three times. Because we don't want 
        duplicate results, we don't need more than two of any number,
        or three zeroes.
        '''
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        filtered = []
        for n, count in counts.items():
            max_count = 3 if n == 0 else 2
            filtered.extend([n] * min(max_count, count))
        return filtered


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.filter_inputs(nums)
        n = len(nums)
        results: Set[Tuple[int]] = set()

        # Collect all numbers and their indexes in a dict, for O(1) lookup
        num_indexes = defaultdict(list)
        for i, num in enumerate(nums):
            num_indexes[num].append(i)
        
        # Enumerate all combinations
        for i in range(0,n-1):
            for j in range(i+1, n):
                s = nums[i] + nums[j]

                for k in num_indexes[-s]:
                    if k > j:    
                        ijk: List[int] = sorted([nums[i], nums[j], nums[k]])
                        triplet: tuple[int, int, int] = tuple(ijk)
                        results.add(triplet)
        
        return [list(t) for t in results]

