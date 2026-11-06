class Solution:
    def rob(self, nums: List[int]) -> int:
        # Money at house i is max of:
        # - Money from house i + max starting at i-2
        # - Money starting at house i-1 (not robbing i)

        memo = {}

        def solve(i: int) -> int:
            nonlocal nums, memo

            if i < 2:
                return max(nums[:i+1])

            if i not in memo:
                res1 = solve(i-1) # Skip house i
                res2 = nums[i] + solve(i-2) # Skip i-1
                memo[i] = max(res1, res2)
            return memo[i]

        return solve(len(nums)-1)