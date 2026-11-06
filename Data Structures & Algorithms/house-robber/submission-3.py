class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        results = [0] * n
        
        # Base cases
        if n == 1:
            return nums[0]
        results[0] = nums[0]
        results[1] = max(nums[:2])

        # Iterate
        for i in range(2,n):
            r1 = results[i-1]
            r2 = nums[i] + results[i-2]
            results[i] = max(r1, r2)
        
        return results[n-1]
        