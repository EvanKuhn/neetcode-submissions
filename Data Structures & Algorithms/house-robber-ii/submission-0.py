class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def solve(i: int, last_selected: bool) -> int:
            nonlocal memo, nums

            # Base cases
            if i == 0:
                return 0 if last_selected else nums[0]
            if i == 1:
                return max(
                    nums[1],
                    0 if last_selected else nums[0],
                )
                
            # Calculate result and cache it. Must take 
            # last_selected into account in cache key.
            key = (i, last_selected)
            if key not in memo:
                r1 = solve(i-1, last_selected)
                r2 = solve(i-2, last_selected)
                if i < len(nums)-1 or last_selected:
                    r2 += nums[i]
                memo[key] = max(r1, r2)
            return memo[key]

        n = len(nums)
        return max(solve(n-1, True), solve(n-1, False))
