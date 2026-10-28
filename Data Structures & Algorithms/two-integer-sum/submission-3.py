from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index_map = defaultdict(list)
        for i, n in enumerate(nums):
            num_to_index_map[n].append(i)
        
        for i, n in enumerate(nums):
            diff = target - n
            indexes = num_to_index_map[diff]
            for other_index in indexes:
                if other_index != i:
                    return [i, other_index]

