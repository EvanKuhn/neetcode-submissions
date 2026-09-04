class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        cursum = 0
        maxsum = nums[0]

        while j < n:
            cursum += nums[j]
            #print(f"cursum={cursum}")

            if cursum > maxsum:
                maxsum = cursum
                #print(f"maxsum={maxsum}")
            if cursum < 0:
                cursum = 0
            j += 1

        return maxsum
        