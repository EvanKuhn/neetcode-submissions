class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create map from number to its index
        num_to_index_map = {}
        for i, n in enumerate(nums):
            num_to_index_map[n] = i
        
        # For each number, compute the second number and check
        # if we have it.
        for i, n in enumerate(nums):
            # Find the other number (o) and its index (j)
            o = target - n
            if o in num_to_index_map:
                j = num_to_index_map[o]
                if i != j:
                    return [i, j]

        assert(f"No pair of numbers found to sum to {target}")

        