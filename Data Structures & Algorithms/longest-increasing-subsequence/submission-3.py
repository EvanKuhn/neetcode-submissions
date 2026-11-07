import math

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def search(last_val: int, index: int) -> int:
            # Helper function, returns max length of increasing subsequence
            nonlocal nums, memo

            # Base case
            if index == len(nums)-1:
                return 1 if nums[index] > last_val else 0

            key = (last_val, index)
            if key not in memo:
                curnum = nums[index]

                # If we can select the current value, select it and search
                len1 = 0
                if curnum > last_val:
                    len1 = 1 + search(curnum, index+1)

                # We can always skip the current value
                len2 = search(last_val, index+1)

                # Save max result
                memo[key] = max(len1, len2)
            
            return memo[key]

        return search(-math.inf, 0)