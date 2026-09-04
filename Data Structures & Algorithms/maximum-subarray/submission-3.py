class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = nums[0]

        for n in nums:
            cursum += n
            if cursum > maxsum:
                maxsum = cursum
            if cursum < 0:
                cursum = 0

        return maxsum
        