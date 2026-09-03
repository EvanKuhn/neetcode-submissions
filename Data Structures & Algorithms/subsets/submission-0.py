class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # Base cases
        if n == 0:
            return [[]]

        # Build up the results recursively
        results = []
        value = nums[0]
        rest = nums[1:n]

        # Compute subsets
        rest_subsets = self.subsets(rest)
        value_plus_subsets = [[value] + s for s in rest_subsets]

        # Store subset results
        results.extend(rest_subsets)
        results.extend(value_plus_subsets)

        return results